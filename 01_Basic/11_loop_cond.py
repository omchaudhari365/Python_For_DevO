log_file = [
    "INFO: System started",
    "WARNING: Low memory",
    "INFO: User logged in",
    "WARNING: Disk space low"
]

for i in log_file:
    if "WARNING" in i:
        print(i)