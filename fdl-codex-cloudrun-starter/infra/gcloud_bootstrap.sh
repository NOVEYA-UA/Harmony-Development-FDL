#!/usr/bin/env bash
# Bootstrap GCP project for Σ-FDL-CODEX starter
set -euo pipefail
PROJECT_ID="${1:?PROJECT_ID required}"
REGION="${2:-europe-west4}"
FIRESTORE_LOCATION="${3:-eur3}"

echo "Enabling APIs for $PROJECT_ID ..."
gcloud services enable       run.googleapis.com       aiplatform.googleapis.com       pubsub.googleapis.com       firestore.googleapis.com       bigquery.googleapis.com       storage.googleapis.com       artifactregistry.googleapis.com       cloudbuild.googleapis.com

echo "Creating Storage bucket (if missing) ..."
BUCKET="gs://${PROJECT_ID}-fdl-artifacts"
if ! gsutil ls "$BUCKET" >/dev/null 2>&1; then
  gsutil mb -l "$REGION" "$BUCKET"
fi

echo "Creating BigQuery dataset (if missing) ..."
if ! bq --location="$REGION" ls --datasets "$PROJECT_ID" | grep -q "fdl_logs"; then
  bq --location="$REGION" mk -d --description "FDL logs & audit" "fdl_logs"
fi

echo "Creating Firestore database (if missing) ..."
if ! gcloud firestore databases describe --database="(default)" --project="$PROJECT_ID" >/dev/null 2>&1; then
  gcloud firestore databases create --location="$FIRESTORE_LOCATION" --type=firestore-native
fi

echo "Creating Pub/Sub topic and a push subscription (OIDC) ..."
TOPIC="fdl-events"
SUB="fdl-codex-push"
SERVICE="fdl-codex"

# Create topic if missing
if ! gcloud pubsub topics describe "$TOPIC" >/dev/null 2>&1; then
  gcloud pubsub topics create "$TOPIC"
fi

# Create service account for push auth
SA="fdl-codex-push@${PROJECT_ID}.iam.gserviceaccount.com"
if ! gcloud iam service-accounts describe "$SA" >/dev/null 2>&1; then
  gcloud iam service-accounts create fdl-codex-push --display-name="FDL Codex PubSub Pusher"
fi

# Grant run.invoker to SA (so Pub/Sub can call the service via OIDC)
gcloud run services add-iam-policy-binding "$SERVICE"       --region="$REGION"       --member="serviceAccount:${SA}"       --role="roles/run.invoker" || true

# Create/replace push subscription (requires service already deployed)
SVC_URL="$(gcloud run services describe "$SERVICE" --region="$REGION" --format='value(status.url)' || true)"
if [[ -n "$SVC_URL" ]]; then
  PUSH_URL="${SVC_URL}/pubsub/push"
  if gcloud pubsub subscriptions describe "$SUB" >/dev/null 2>&1; then
    gcloud pubsub subscriptions delete "$SUB" || true
  fi
  gcloud pubsub subscriptions create "$SUB"         --topic="$TOPIC"         --push-endpoint="$PUSH_URL"         --push-auth-service-account="$SA"
  echo "Push subscription created to $PUSH_URL"
else
  echo "NOTE: Deploy service first (./deploy.sh), then re-run this script to create the push subscription."
fi

echo "Bootstrap complete."
