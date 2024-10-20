import sys
from pathlib import Path

def local_path() -> Path:
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        return Path(sys._MEIPASS).resolve()  # NOQA
    return Path('.').resolve()