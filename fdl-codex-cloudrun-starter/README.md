# Σ-FDL-CODEX — Cloud Run Orchestrator (Starter)

Minimal starter to deploy a FastAPI service to **Google Cloud Run** with a Gemini (Vertex AI) client,
Pub/Sub push endpoint, and example Firestore/BigQuery hooks.

## One-line chips
Google Cloud Run, Google Cloud Pub/Sub, Firestore, BigQuery, Cloud Storage, Vertex AI (Gemini 1.5, Gemma), Google Agent Development Kit (ADK), Python, FastAPI, Docker, OpenAPI/Swagger, Cloud Build, GitHub Actions

## Quick start (Cloud Shell)
```bash
# 1) Clone your repo and copy this folder's contents into it, or upload the ZIP from ChatGPT
export PROJECT_ID="$(gcloud config get-value project)"
export REGION="europe-west4"
export FIRESTORE_LOCATION="eur3"   # Firestore is multi-region; eur3 covers Europe

./infra/gcloud_bootstrap.sh "$PROJECT_ID" "$REGION" "$FIRESTORE_LOCATION"
./deploy.sh "$PROJECT_ID" "$REGION"
```

## Endpoints
- `GET /health` — liveness check
- `POST /try` — { "query": "text" } → calls Gemini and returns a response
- `POST /pubsub/push` — Pub/Sub push target (verifies JWT audience, decodes message)
- `GET /docs` — Swagger UI

## Notes
- Make sure the **Vertex AI API** is enabled and your service has permission to call it.
- Replace the model name via env `GEMINI_MODEL` if needed (default: `gemini-1.5-flash`).
- Firestore creation may take a minute; it must be created **once per project**.
