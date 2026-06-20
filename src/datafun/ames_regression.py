"""ames_regression.py - Regression Module (Ames Housing)

Author: Justice Tefera
Date: 2026-06
"""

# === IMPORTS ===

import logging
import random
from typing import Final

from datafun_toolkit.logger import get_logger, log_header
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# === LOGGER ===

LOG: logging.Logger = get_logger("JT", level="DEBUG")
log_header(LOG, "JT")

# === GLOBAL CONSTANTS ===

DATASET_NAME: Final[str] = "housing"

FEATURE_COL: Final[str] = "Gr Liv Area"
TARGET_COL: Final[str] = "SalePrice"

FEATURE_LABEL: Final[str] = "Above-ground living area (sq ft)"
TARGET_LABEL: Final[str] = "Sale Price (USD)"

EXAMPLE_FEATURE_VALUE: Final[float] = 2000.0

pd.set_option("display.max_columns", 50)
pd.set_option("display.width", 120)

# === SECTION 2: LOAD DATA ===


def load_data() -> pd.DataFrame:
    LOG.info(f"Loading dataset: {DATASET_NAME}")
    df = pd.read_csv(f"data/raw/{DATASET_NAME}.csv")
    LOG.info(f"Loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    return df


# === SECTION 3: MODELING VIEW ===


def make_model_view(df: pd.DataFrame) -> pd.DataFrame:
    LOG.info("Creating modeling view (dropping rows missing feature or target)")
    cols_required = [FEATURE_COL, TARGET_COL]

    df_model = df.dropna(subset=cols_required).copy()

    LOG.info(f"Original rows: {df.shape[0]}")
    LOG.info(f"Model rows:    {df_model.shape[0]}")
    LOG.info(f"Rows dropped:  {df.shape[0] - df_model.shape[0]}")

    return df_model


# === SECTION 4: BUILD X AND Y ===


def build_x_and_y(df_model: pd.DataFrame):
    LOG.info("Building feature matrix X and target vector y")
    X = df_model[[FEATURE_COL]].to_numpy()
    y = df_model[TARGET_COL].to_numpy()
    return X, y


# === SECTION 5: FIT LINE ===


def fit_line(X: np.ndarray, y: np.ndarray) -> LinearRegression:
    LOG.info("Fitting linear regression model")

    model = LinearRegression()
    model.fit(X, y)

    slope = float(model.coef_[0])
    intercept = float(model.intercept_)

    LOG.info(
        f"Fitted line: {TARGET_COL} = {slope:.6g} * {FEATURE_COL} + {intercept:.6g}"
    )

    return model


# === SECTION 6: PREDICT ===


def predict(model: LinearRegression, X: np.ndarray):
    LOG.info("Computing fitted values")
    y_hat = model.predict(X)
    return y_hat


# === SECTION 7: EXAMINE FIT ===


def examine_fit(
    model: LinearRegression, X: np.ndarray, y: np.ndarray, y_hat: np.ndarray
):
    LOG.info("Computing residuals")
    residuals = y - y_hat
    return residuals


# === SECTION 8: PLOTS ===


def make_plots(
    df_model: pd.DataFrame, y_hat: np.ndarray, residuals: np.ndarray
) -> None:

    feature_values = df_model[FEATURE_COL].to_numpy()
    target_values = df_model[TARGET_COL].to_numpy()

    # === Scatter plot ===
    LOG.info("Creating scatter plot with fitted line")
    plt.figure()

    # Random red, white, and blue dots
    colors_scatter = [
        random.choice(["#FF0000", "#FFFFFF", "#0000FF"]) for _ in range(len(df_model))
    ]

    plt.scatter(
        feature_values,
        target_values,
        c=colors_scatter,
        edgecolors="black",
        linewidths=0.3,
    )

    # Fitted line (black)
    order = np.argsort(feature_values)
    plt.plot(feature_values[order], y_hat[order], color="black", linewidth=2)

    plt.xlabel(FEATURE_LABEL)
    plt.ylabel(TARGET_LABEL)
    plt.title(f"{FEATURE_LABEL} vs {TARGET_LABEL} with fitted line")

    plt.savefig("docs/images/scatter_with_line.png", dpi=300, bbox_inches="tight")

    # === Residual plot ===
    LOG.info("Creating residual plot")
    plt.figure()

    # Random red, white, and blue dots
    colors_resid = [
        random.choice(["#FF0000", "#FFFFFF", "#0000FF"]) for _ in range(len(df_model))
    ]

    plt.scatter(
        feature_values, residuals, c=colors_resid, edgecolors="black", linewidths=0.3
    )

    # Horizontal line (black)
    plt.axhline(0, color="black", linewidth=2)

    plt.xlabel(FEATURE_LABEL)
    plt.ylabel("Residuals")
    plt.title(f"Residuals vs {FEATURE_LABEL}")

    plt.savefig("docs/images/residuals_plot.png", dpi=300, bbox_inches="tight")


# === SECTION 9: SUMMARY ===


def summarize(
    df: pd.DataFrame, df_model: pd.DataFrame, model: LinearRegression
) -> None:
    slope = float(model.coef_[0])
    intercept = float(model.intercept_)

    LOG.info("========================")
    LOG.info("SUMMARY")
    LOG.info("========================")
    LOG.info(f"Dataset: {DATASET_NAME}")
    LOG.info(f"Feature (x): {FEATURE_COL}")
    LOG.info(f"Target  (y): {TARGET_COL}")
    LOG.info(f"Original rows: {df.shape[0]}")
    LOG.info(f"Model rows:    {df_model.shape[0]}")
    LOG.info(
        f"Fitted line: {TARGET_COL} = {slope:.6g} * {FEATURE_COL} + {intercept:.6g}"
    )
    LOG.info("========================")


# === MAIN ===


def main():
    log_header(LOG, "REGRESSION")

    df = load_data()
    df_model = make_model_view(df)
    X, y = build_x_and_y(df_model)
    model = fit_line(X, y)
    y_hat = predict(model, X)
    residuals = examine_fit(model, X, y, y_hat)
    make_plots(df_model, y_hat, residuals)
    summarize(df, df_model, model)

    plt.show()


if __name__ == "__main__":
    main()
