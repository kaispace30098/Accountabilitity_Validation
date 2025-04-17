#!/bin/bash

# Push to GitHub
git push origin dev

# Create PR; this triggers the workflow defined in .github/workflows
gh pr create --base main --head dev --title "CI Test" --body "Run CI on dev branch"

# Wait for the CI check to pass before merging
# Poll until CI passes or fails
while true; do
  STATUS=$(gh pr view --json status -q .status)

  if [[ "$STATUS" == "SUCCESS" ]]; then
    echo "CI passed!"
    break
  elif [[ "$STATUS" == "ERROR" || "$STATUS" == "FAILURE" ]]; then
    echo "CI failed, exiting script."
    exit 1
  else
    echo "CI still running..."
    sleep 5
  fi
done

# Check for merge conflicts
CONFLICT_STATUS=$(gh pr status --json conflict-status -q .conflictStatus)
if [[ "$CONFLICT_STATUS" != "none" ]]; then
  echo "Merge conflicts detected: $CONFLICT_STATUS"
  exit 1
fi

# Auto-merge when CI passes and no conflicts
gh pr merge --auto --squash


# Sync main locally and push to Azure
git checkout main
git pull origin main
git push azure main