from pathlib import Path

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor

PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Directories
DATA_DIR = PROJECT_ROOT / "data"
MODEL_DIR = PROJECT_ROOT / "models"

# Filenames
RAW_DATA_FILE = DATA_DIR / "BostonHousing.csv"
CLEAN_DATA_FILE = DATA_DIR / "processed_housing.csv"
MODEL_RESULTS_FILE = DATA_DIR / "models.csv"

# ----------- MODELING ---------------

RANDOM_STATE = 1
DATA_SPLIT_RATIO = 0.2


# Model keynames
LR, RFR, XGBR = "lr", "rfr", "xgbr"
KEYS = [LR, RFR, XGBR]

# Descriptive names mapping
MODEL_NAMES = {
    LR: "Linear Regression",
    RFR: "Random Forest Regressor",
    XGBR: "XGBRegressor",
}

MODEL_CLASSES = {LR: LinearRegression, RFR: RandomForestRegressor, XGBR: XGBRegressor}

# Model config
MODELS = {
    key: {
        "name": MODEL_NAMES[key],
        "filename": MODEL_DIR / f"{key}.pkl",
        "class": MODEL_CLASSES[key],
    }
    for key in KEYS
}

# SHAP
SAMPLE_IND = 15
MAX_SAMPLE = 0
MIN_SAMPLE = 0
