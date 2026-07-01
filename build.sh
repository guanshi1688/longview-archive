#!/bin/bash
set -e

# 读取 site_mode.txt 中第一行非空、非注释内容
MODE=$(grep -v '^[[:space:]]*#' site_mode.txt | grep -v '^[[:space:]]*$' | head -n 1 | tr -d '[:space:]')

echo "Current site mode: $MODE"

if [ "$MODE" = "maintenance" ]; then
  echo "Building maintenance site..."
  mkdocs build -f mkdocs.maintenance.yml
elif [ "$MODE" = "normal" ]; then
  echo "Building normal site..."
  mkdocs build
else
  echo "ERROR: Unknown site mode: $MODE"
  echo "Use one of:"
  echo "  normal"
  echo "  maintenance"
  exit 1
fi
