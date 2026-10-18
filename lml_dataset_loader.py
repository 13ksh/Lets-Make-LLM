import os
import json

class DatasetLoader:
    def __init__(self, file_path):
        # Set dataset file path
        self.file_path = file_path

    def load_data(self):
        # Validate dataset file existence
        if not self.file_path or not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Dataset file not found. Please verify the path: {self.file_path}")

        data = []
        try:
            # Read JSONL file line by line and load into a list
            with open(self.file_path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        data.append(json.loads(line))
            return data
        except Exception as e:
            raise IOError(f"Error occurred while reading dataset file ({self.file_path}): {e}")
