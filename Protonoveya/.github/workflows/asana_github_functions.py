"""
Utility functions for interacting with Asana and GitHub using direct API calls.

These functions avoid web interfaces by using HTTP requests.  They are intended
to be executed within the NOVEYA project’s sandbox environment.

Before using these functions:
  - Set environment variables or pass parameters with your personal access
    tokens (PAT) for Asana and GitHub.  Do **not** hard‑code secrets in your code.
  - Ensure that your tokens have the correct scopes: Asana PAT should allow
    task creation; GitHub PAT should allow repo content creation.

Note: These functions return the JSON response from the API.  Use the
returned data to log IDs or error messages.
"""
import base64
import os
import requests
from typing import List, Optional, Dict, Any


def create_asana_task(
    pat: str,
    workspace_gid: str,
    project_gid: str,
    name: str,
    notes: str,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Create a task in Asana.

    Args:
        pat: Personal access token for Asana.
        workspace_gid: The workspace or organization GID where the task will be created.
        project_gid: The project GID to associate the task with.
        name: The task name.
        notes: The task description/notes.
        tags: Optional list of tag GIDs to apply to the task.

    Returns:
        The JSON response from Asana API.
    """
    headers = {
        "Authorization": f"Bearer {pat}",
        "Content-Type": "application/json",
    }
    payload = {
        "data": {
            "name": name,
            "notes": notes,
            "workspace": workspace_gid,
            "projects": [project_gid],
        }
    }
    if tags:
        payload["data"]["tags"] = tags
    response = requests.post(
        "https://app.asana.com/api/1.0/tasks", headers=headers, json=payload
    )
    response.raise_for_status()
    return response.json()


def commit_file_github(
    pat: str,
    owner: str,
    repo: str,
    path: str,
    content: str,
    message: str,
    branch: str = "main",
) -> Dict[str, Any]:
    """Create or update a file in a GitHub repository.

    Args:
        pat: Personal access token for GitHub.
        owner: Repository owner (username or organization).
        repo: Repository name.
        path: File path within the repository (e.g. "docs/example.md").
        content: The text content to commit.
        message: Commit message.
        branch: Branch name to commit to (default "main").

    Returns:
        The JSON response from GitHub API.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    headers = {
        "Authorization": f"token {pat}",
        "Accept": "application/vnd.github+json",
    }
    # Check if file exists to include its SHA for update
    get_resp = requests.get(url, headers=headers, params={"ref": branch})
    if get_resp.status_code == 200:
        sha = get_resp.json().get("sha")
    else:
        sha = None
    encoded_content = base64.b64encode(content.encode("utf-8")).decode("utf-8")
    payload = {
        "message": message,
        "content": encoded_content,
        "branch": branch,
    }
    if sha:
        payload["sha"] = sha
    put_resp = requests.put(url, headers=headers, json=payload)
    put_resp.raise_for_status()
    return put_resp.json()


if __name__ == "__main__":
    # Example usage: create a task or commit a file.  These commands are for
    # demonstration and should be replaced with actual values or moved into
    # scripts that read from environment variables.
    asana_token = os.environ.get("ASANA_PAT")
    github_token = os.environ.get("GITHUB_PAT")
    if asana_token and github_token:
        print("Tokens found in environment. You can call the helper functions.")
    else:
        print("Set ASANA_PAT and GITHUB_PAT environment variables to use this module.")