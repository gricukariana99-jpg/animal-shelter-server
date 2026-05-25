#!/usr/bin/env python3
import subprocess

DB_NAME = "dolibarr_db"
DB_USER = "dolibarr_user"
DB_PASSWORD = "dolibarr_password"

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

print("New adoption requests:")
subprocess.run(command, check=True)
