from pathlib import Path
import subprocess

shortcut = Path(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")

subprocess.Popen(shortcut)