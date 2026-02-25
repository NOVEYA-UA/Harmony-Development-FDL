#!/usr/bin/env bash
set -euo pipefail
PROJECT_ID="${1:-$(gcloud config get-value project)}"
REGION="${2:-europe-west4}"
IMAGE_HOST="${3:-europe-west4-docker.pkg.dev}"
REPO="fdl-codex"
IMAGE="${IMAGE_HOST}/${PROJECT_ID}/${REPO}/fdl-codex:latest"

echo "Project: $PROJECT_ID  Region: $REGION"
gcloud config set project "$PROJECT_ID"

# Create Artifact Registry repo if missing
if ! gcloud artifacts repositories describe "$REPO" --location="$REGION" >/dev/null 2>&1; then
  gcloud artifacts repositories create "$REPO" --repository-format=DOCKER --location="$REGION"
fi

# Build and push
gcloud builds submit --region="$REGION" --config=cloudbuild.yaml       --substitutions=_REGION="$REGION",_AR_HOST="$IMAGE_HOST",_TAG="latest"

# Print service URL
gcloud run services describe fdl-codex --region="$REGION" --format='value(status.url)'
