#!/usr/bin/env bash
TARGET="http://web-server:8080/"
INTERVAL=${INTERVAL:-5}


while true; do
    echo "[requester] $(date -u +%Y-%m-%dT%H:%M:%SZ) -> requesting $TARGET"
    curl -sS --max-time 4 "$TARGET" || echo "[requester] falha ao alcançar $TARGET"
    echo
    sleep "$INTERVAL"
done