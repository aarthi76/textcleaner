from typing import List
import json

class TextCleanerConfig:
    def __init__(self, config_path: str = "config.json"):
        self.allowed_emojis: List[str] = []
        self.load_config(config_path)

    def load_config(self, path: str):
        try:
            with open(path) as f:
                config = json.load(f)
                self.allowed_emojis = config.get("allowed_emojis", [])
        except FileNotFoundError:
            pass