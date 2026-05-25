#!/usr/bin/env python3
import subprocess
from datetime import datetime

DB_NAME = "dolibarr_db"
DB_USER = "dolibarr_user"
DB_PASSWORD = "dolibarr_password"
LOG_FILE = "/mnt/backups/animal-shelter/new_requests.log"

query = """
SELECT ref, subject, message
FROM llx_ticket
ORDER BY rowid DESC
LIMIT 5;
"""

command = [
    "mysql",
    "-u", DB_USER,
    f"-p{DB_PASSWORD}",
    DB_NAME,
    "-e", query
]

result = subprocess.run(command, capture_output=True, text=True, check=True)

log_text = (
    "\n"
    "==== New adoption requests check ====\n"
    f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    f"{result.stdout.replace('\\\\n', chr(10))}\n"
)

print(log_text)

with open(LOG_FILE, "a") as f:
    f.write(log_text)

print(f"Notification log updated: {LOG_FILE}")
