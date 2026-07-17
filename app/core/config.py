from pathlib import Path
import json


class Config:

    def __init__(self):

        self.root = Path(__file__).resolve().parents[2]

        self.file = self.root / "config.json"

        with open(self.file, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    @property
    def api(self):
        return self.data["api"]

    @property
    def excel(self):
        return self.data["excel"]