#!/bin/bash
set -Eeuo pipefail

LOG="/home/ubuntu/backup-logs/backup.log"
KEY="/home/ubuntu/.ssh/id_ed25519_vmbox_b"
DEST="ubuntu@192.168.1.185:/var/backups/viikko2/backup-$(date +%Y%m%d-%H%M%S)/"

exec >> "$LOG" 2>&1

echo "========================================"
echo "Backup started: $(date)"

if rsync -a \
    -e "ssh -i $KEY -o BatchMode=yes" \
    /var/www/html/ "$DEST"; then
    echo "SUCCESS: Backup completed"
else
    echo "ERROR: Backup failed"
    exit 1
fi

echo "Backup finished: $(date)"
