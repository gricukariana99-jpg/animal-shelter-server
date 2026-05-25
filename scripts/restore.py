#!/usr/bin/env python3
import sys
import subprocess
import os

DB_NAME = "dolibarr_db"
DB_USER = "dolibarr_user"
DB_PASSWORD = "dolibarr_password"

if len(sys.argv) != 2:
    print("Usage: sudo ./scripts/restore.py /path/to/backup.sql")
    sys.exit(1)

backup_file = sys.argv[1]

if not os.path.exists(backup_file):
    print(f"Backup file not found: {backup_file}")
    sys.exit(1)

command = [
    "mysql",
    "-u", DB_USER,
    f"-p{DB_PASSWORD}",
    DB_NAME
]

with open(backup_file, "r") as f:
    subprocess.run(command, stdin=f, check=True)

print(f"Database restored from: {backup_file}")
