from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = APP_DIR.parent

DATA_DIR = PROJECT_DIR / "data"
PROCESSED_DATA_DIR = PROJECT_DIR / "processed_data"

def ensure_directories():
    """
    Ensure that necessary directories exist.
    """
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)