#!/usr/bin/env python3
import os
import subprocess
from datetime import datetime

DB_NAME = "dolibarr_db"
DB_USER = "dolibarr_user"
DB_PASSWORD = "dolibarr_password"
BACKUP_DIR = "/mnt/backups/animal-shelter"

os.makedirs(BACKUP_DIR, exist_ok=True)

date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_file = f"{BACKUP_DIR}/dolibarr_db_{date}.sql"

command = [
    "mysqldump",
    "-u", DB_USER,
    f"-p{DB_PASSWORD}",
    DB_NAME
]

with open(backup_file, "w") as f:
    subprocess.run(command, stdout=f, check=True)

print(f"Backup created: {backup_file}")
