#!/usr/bin/env bash
# Bootstrap the composer-instrument-guide skill in a fresh environment.
# Idempotent — safe to run repeatedly.
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"

echo "[1/2] Installing Python deps..."
pip install -r requirements.txt --break-system-packages 2>&1 | tail -3

echo "[2/2] Installing Node deps..."
npm install --silent 2>&1 | tail -3

echo "✓ composer-instrument-guide ready."
