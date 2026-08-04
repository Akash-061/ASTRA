import platform
import psutil
from datetime import datetime


def get_system_info():
    return {
        "os": platform.system(),
        "cpu": psutil.cpu_percent(interval=1),
        "ram": psutil.virtual_memory().percent,
        "time": datetime.now().strftime("%I:%M %p"),
    }