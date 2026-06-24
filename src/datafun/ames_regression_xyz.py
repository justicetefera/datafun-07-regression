"""
ames_regression_xyz.py - Multi-Feature Regression Engine (Ames Housing)
Red-White-Blue Visualization Edition (Artifacts)

Author: Justice Tefera
Date: 2026-06
"""

import logging
import os
import random
from typing import Final

from datafun_toolkit.logger import get_logger, log_header
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, root_mean_squared_error

# === LOGGER ===
LOG: logging.Logger = get_logger("JT-XYZ", level="DEBUG")
log_header(LOG, "JT XYZ REGRESSIONS")

# === GLOBAL CONSTANTS ===
DATASET_NAME: Final[str] = "housing"
TARGET_COL: Final[str] = "SalePrice"

# Output folder for XYZ artifacts
OUTPUT_DIR: Final[str] = "docs/artifacts/xyz"
os.makedirs(OUTPUT_DIR, exist_ok=True)

pd.set_option("display.max_columns", 50)
pd.set_option("display.width", 120)

# === RED-WHITE-BLUE COLOR PALETTE ===
RWB_COLORS = ["#FF0000", "#FFFFFF", "#0000FF"]


def load_data() -> pd.DataFrame:
    LOG.info(f"Loading dataset: {DATASET_NAME}")
    df = pd.read_csv(f"data/raw/{DATASET_NAME}.csv")
    LOG.info(f"Loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    return df


def run_xyz_regression(feature_col: str, feature_label: str, tag: str):
    """Run a simple linear regression and save red-white-blue visuals."""
    log_header(LOG, f"XYZ REGRESSION: {feature_col}")

    df = load_data()
    df_model = df.dropna(subset=[feature_col, TARGET_COL]).copy()

    X = df_model[[feature_col]].to_numpy()
    y = df_model[TARGET_COL].to_numpy()

    model = LinearRegression()
    model.fit(X, y)

    slope = float(model.coef_[0])
    intercept = float(model.intercept_)

    LOG.info(
        f"Fitted line: {TARGET_COL} = {slope:.6g} * {feature_col} + {intercept:.6g}"
    )

    y_hat = model.predict(X)
    residuals = y - y_hat

    r2 = r2_score(y, y_hat)
    rmse = root_mean_squared_error(y, y_hat)

    LOG.info(f"R²: {r2:.4f}")
    LOG.info(f"RMSE: {rmse:,.2f}")

    # === Scatter Plot (Red-White-Blue) ===
    plt.figure()
    colors_scatter = [random.choice(RWB_COLORS) for _ in range(len(df_model))]
    plt.scatter(X, y, c=colors_scatter, edgecolors="black", linewidths=0.3)
    plt.plot(X, y_hat, color="black", linewidth=2)
    plt.xlabel(feature_label)
    plt.ylabel(TARGET_COL)
    plt.title(f"{feature_label} vs {TARGET_COL} (RWB Theme)")
    plt.savefig(f"{OUTPUT_DIR}/{tag}_scatter.png", dpi=300)

    # === Residual Plot (Red-White-Blue) ===
    plt.figure()
    colors_resid = [random.choice(RWB_COLORS) for _ in range(len(df_model))]
    plt.scatter(X, residuals, c=colors_resid, edgecolors="black", linewidths=0.3)
    plt.axhline(0, color="black", linewidth=2)
    plt.xlabel(feature_label)
    plt.ylabel("Residuals")
    plt.title(f"Residuals vs {feature_label} (RWB Theme)")
    plt.savefig(f"{OUTPUT_DIR}/{tag}_residuals.png", dpi=300)

    LOG.info("XYZ regression complete.")
    LOG.info("========================")


def run_multivariable_regression():
    log_header(
        LOG, "MULTIVARIABLE REGRESSION: Garage + 1st Flr SF + Rooms vs SalePrice"
    )

    df = load_data()
    df_model = df.dropna(
        subset=["Garage Area", "1st Flr SF", "TotRms AbvGrd", TARGET_COL]
    ).copy()

    X = df_model[["Garage Area", "1st Flr SF", "TotRms AbvGrd"]].to_numpy()
    y = df_model[TARGET_COL].to_numpy()

    model = LinearRegression()
    model.fit(X, y)

    b1, b2, b3 = model.coef_
    intercept = model.intercept_

    LOG.info(
        f"Model: SalePrice = {b1:.3f} * Garage Area + "
        f"{b2:.3f} * 1st Flr SF + "
        f"{b3:.3f} * TotRms AbvGrd + {intercept:.3f}"
    )

    y_hat = model.predict(X)
    r2 = r2_score(y, y_hat)
    rmse = root_mean_squared_error(y, y_hat)

    LOG.info(f"R²: {r2:.4f}")
    LOG.info(f"RMSE: {rmse:,.2f}")

    # Visualization: Actual vs Predicted
    plt.figure()
    plt.scatter(y, y_hat, c="#FF0000", edgecolors="black", alpha=0.5)
    plt.xlabel("Actual SalePrice")
    plt.ylabel("Predicted SalePrice")
    plt.title("Multivariable Regression: Actual vs Predicted (RWB Theme)")
    plt.plot([y.min(), y.max()], [y.min(), y.max()], color="#0000FF", linewidth=2)
    plt.savefig("docs/artifacts/xyz/multivariable_actual_vs_predicted.png", dpi=300)

    LOG.info("Multivariable regression complete.")
    LOG.info("========================")


def main():
    run_xyz_regression("Garage Area", "Garage Area (sq ft)", "garage_to_price")
    run_xyz_regression("1st Flr SF", "First Floor Area (sq ft)", "firstfloor_to_price")
    run_xyz_regression("TotRms AbvGrd", "Total Rooms Above Ground", "rooms_to_price")
    run_multivariable_regression()


if __name__ == "__main__":
    main()
    plt.show()
