#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="${HOME}/.claude/skills/psychotherapy-skills-universal"
mkdir -p "$DEST"
cp -R "$ROOT"/. "$DEST"/
echo "Installed to $DEST"
