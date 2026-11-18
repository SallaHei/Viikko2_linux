# Automated Backup Scheduling

## Cron configuration

The website backup runs automatically once every hour.

Cron entry:

0 * * * * /home/ubuntu/bin/backup-html-to-b.sh

## Backup script

/home/ubuntu/bin/backup-html-to-b.sh

## Backup source

/var/www/html/

## Backup destination

Server B:
ubuntu@192.168.1.185:/var/backups/viikko2/

Each backup is stored in a separate timestamped directory.

## Logging

/home/ubuntu/backup-logs/backup.log

## Verification

On 18 November 2026, seven successful hourly backup runs were recorded.

The seven corresponding timestamped backup directories were verified on Server B.

A separate restore test was completed successfully, and the SHA-256 checksums matched.
