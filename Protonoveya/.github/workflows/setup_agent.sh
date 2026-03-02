#!/bin/bash
# This script installs Python dependencies for the NOVEYA code interpreter.

set -e

echo "Updating pip..."
python -m pip install --upgrade pip

echo "Installing required packages..."
# asana: official Asana Python client
# PyGithub: GitHub API client
# requests: HTTP client used by utility functions
# n8n-client: interface for interacting with n8n via its API (optional for automation)
pip install --no-cache-dir asana PyGithub requests n8n-client

echo "Installation complete."