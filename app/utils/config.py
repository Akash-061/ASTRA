import json
from pathlib import Path


def load_apps():
    """
    Load all applications from config/apps.json
    """

    config_path = Path("config/apps.json")

    with open(config_path, "r") as file:
        apps = json.load(file)

    return apps