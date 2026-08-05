import os
from pathlib import Path

shortcut = Path(
    r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"
)

os.startfile(shortcut)