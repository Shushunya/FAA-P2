# The Project for the Machine Learning Fundamentals Course, 2025-2026

Topic: Explainable AI (XAI) for the basic ML problem
ML problem: House price prediction (Boston dataset)

Contributors: Bruno Gomes (103320) and Oleksandra Chernenko (131239), Universidade de Aveiro

Project structure:

Directories & notebooks:

- `data`: contains the dataset and model performance dataset
- `models`: saved best model files `.pkl`
- `notebooks`: all of the jupyter notebooks relevant to this project
  - `modeling`: notebooks with modeling stages for each of the algorithm selected (Linear Regression, Random Forest Regressor and XGBoost Regressor)
  - `xai`: notebooks with xai exploration on the tree-based models
  - `eda.ipynb`
  - `modeling.ipynb`: comparison of the best models
  - `preprocessing.ipynb`
- `src`: configuration file with all of the constants

Project configuration files: `src\faa_p2\config.py`, `pyproject.toml` (dependecies)

The project was done with the use of:

- libraries:
  - `pandas`, `scikit-learn`, `shap`, `lime`, `xgboost`
  - visualizations: `matplotlib` and `seaborn`

- project/dependency manager: `uv`
