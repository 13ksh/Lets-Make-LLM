import os
import datetime

class Logger:
    @staticmethod
    def log(message, log_dir="."):
        # Validate if the specified log directory exists; raise error if not
        if not os.path.exists(log_dir):
            raise FileNotFoundError(f"Log directory not found. Specified path: {log_dir}")

        # Generate log filename (e.g., 2026-08-11-lml.log)
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
        filename = f"{date_str}-lml.log"
        filepath = os.path.join(log_dir, filename)

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"

        # Write log entry to file
        with open(filepath, "a", encoding="utf-8") as f:
            f.write(log_entry)
