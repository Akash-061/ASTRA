from pathlib import Path

START_MENU_PATHS = [
    Path(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs"),
    Path.home() / r"AppData\Roaming\Microsoft\Windows\Start Menu\Programs",
]


def discover_apps():
    

    apps = {}

    for path in START_MENU_PATHS:
        for shortcut in path.rglob("*.lnk"):
            apps[shortcut.stem.lower()] = shortcut

    return apps


