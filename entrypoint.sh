#!/bin/bash
set -eo pipefail
shopt -s nullglob
uvicorn main:app --host 0.0.0.0 --port 80 --reload