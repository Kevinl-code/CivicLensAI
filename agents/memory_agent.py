import json
import os

class MemoryAgent:

    FILE = "memory/users.json"

    def save(self, record):

        if os.path.exists(self.FILE):

            with open(self.FILE, "r") as f:
                data = json.load(f)

        else:
            data = []

        data.append(record)

        with open(self.FILE, "w") as f:
            json.dump(data, f, indent=2)

    def load_all(self):

        if not os.path.exists(self.FILE):
            return []

        with open(self.FILE, "r") as f:
            return json.load(f)