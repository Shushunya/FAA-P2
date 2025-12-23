from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Directories
DATA_DIR = PROJECT_ROOT / "data"

# Filenames
RAW_DATA_FILE = DATA_DIR / "BostonHousing.csv"
CLEAN_DATA_FILE = DATA_DIR / "processed_housing.csv"
