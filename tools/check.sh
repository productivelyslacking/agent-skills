#!/usr/bin/env bash
# Runs every check CI runs, layout-check first. Stops at the first failure.
set -euo pipefail
cd "$(dirname "$0")/.."
tools/layout-check .
python3 tools/check.py
python3 tools/check_requirements.py
python3 tools/check_private.py
python3 -m unittest discover -s tests -q
