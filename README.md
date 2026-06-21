# 🏠 Ames Housing Linear Regression Analysis

[![Workflow Guide](https://img.shields.io/badge/Pro--Guide-pro--analytics--02-green)](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](./pyproject.toml)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Professional Python project: linear regression and predictive analytics.


## 📝 Project Overview
This project introduces the core ideas of linear regression, a fundamental statistical technique used to model relationships between variables and make predictions based on data. In simple terms, linear regression fits a straight line through a cloud of data points in a way that best represents the overall trend.

To explore these concepts in a real‑world context, this project applies simple linear regression to the well‑known Ames Housing dataset, which contains detailed information about nearly 3,000 residential properties sold in Ames, Iowa. The goal is to understand how specific home features influence sale price and to evaluate whether a straight‑line model is an appropriate description of those relationships.
Two regressions were completed:
***Gr Liv Area → SalePrice***
***Overall Qual → SalePrice***
Each regression includes:
- A fitted-line plot
- A residual plot
- R² and RMSE metrics
- A summary of findings
These results help determine whether a straight-line model is a fair description of the relationship between each feature and home sale price.

## 📌 How to Run the Project
From the project root directory:
```shell
python src/datafun/ames_regression.py
```
This script automatically runs both regressions and saves plots to: `docs/images/`

## 📈 Regression 1: Gr Liv Area → SalePrice
| Metric | Value | Interpretation |
| --- | --- | --- |
| **R²** | 0.4995 | About 50 % of the variation in sale price is explained by above‑ground living area. That’s moderate — size matters, but other factors (quality, neighborhood, etc.) also influence price. |
| **RMSE** | $56 504.88 | On average, predictions differ from actual sale prices by roughly $56 500. That’s a realistic spread for housing data. |

### Interpretation
- The scatterplot should show a clear upward trend — larger homes tend to cost more.
- The residual plot likely shows a funnel shape (variance increases for larger homes).
- Because residuals aren’t perfectly random, a straight line is a reasonable but imperfect description.
- This model is useful for understanding general price trends, not precise predictions.

The relationship between above‑ground living area and sale price is positive and moderately strong. Larger homes tend to sell for more, and the fitted-line plot shows a clear upward trend.

An R² of 0.4995 means that about 50% of the variation in sale price can be explained by the size of the home alone. This is meaningful, but it also indicates that other factors (quality, neighborhood, condition, etc.) play a major role.

The RMSE of $56,504.88 indicates that predictions from this simple model typically differ from actual sale prices by around $56k. This is reasonable for housing data, where prices vary widely.

## Residual Analysis
The residual plot shows increasing spread as home size increases — a funnel shape. This suggests:
- Variance is not constant (heteroscedasticity).
- A straight line is a reasonable but imperfect description.
- Larger homes have more unpredictable prices.

## Conclusion
Gr Liv Area is a useful predictor of sale price, but the linear model does not capture all the complexity. This regression provides valuable insight but should be supplemented with additional features or transformations for improved accuracy.

### 📈 Regression 2: Overall Qual → SalePrice
| Metric | Value | Interpretation |
| --- | --- | --- |
| **R²** | 0.6388 | About 64 % of the variation in sale price is explained by overall quality rating — a strong linear relationship. |
| **RMSE** | $48 002.35 | Average prediction error is around $48 000, smaller than the first model, meaning better fit. |

### Interpretation
- The fitted‑line plot should show a steep, clean upward trend — higher‑quality homes sell for more.
- Residuals are likely more evenly scattered, meaning the linear model fits well.
- A straight line is a fair description of this relationship.
- This model is stronger and more reliable than the Gr Liv Area model.

Overall Quality is one of the strongest predictors of home sale price in the Ames dataset. The fitted-line plot shows a clear, steep upward trend: as the quality rating increases, sale price increases sharply.

An R² of 0.6388 means that about 64% of the variation in sale price can be explained by the quality rating alone. This is a strong linear relationship, especially for a single‑feature model.

The RMSE of $48,002.35 is lower than the RMSE from the Gr Liv Area model, indicating that this regression produces more accurate predictions.

## Residual Analysis
The residuals appear more evenly scattered compared to the Gr Liv Area model. This suggests:
- Variance is more consistent across quality levels
- The linear model fits the data well
- There is less curvature or funneling in the residuals
This makes Overall Qual a better candidate for linear regression.

## Conclusion
Overall Quality is a strong, reliable predictor of sale price. A straight-line model is a fair and effective description of this relationship. This regression provides clearer insight and stronger predictive power than the Gr Liv Area model.

## 📌 Next Steps for Further Analysis
1. **Explore Additional Predictive Features**
The Ames dataset contains many numerical variables that may have stronger or complementary relationships with SalePrice. Features such as Total Basement Area, Garage Area, 1st Floor SF, and Year Built often show meaningful linear patterns. Testing these variables individually can help identify which characteristics of a home contribute most to its market value. This step also helps determine whether size‑related features or age‑related features provide better predictive power.

2. **Apply Transformations to Improve Linearity**
Some relationships become more linear after applying mathematical transformations. For example, taking the logarithm of SalePrice can stabilize variance and reduce the impact of extreme values. Similarly, applying log or square‑root transformations to skewed features (like Gr Liv Area or Total Bsmt SF) can produce cleaner residual patterns. This step helps determine whether a straight‑line model is appropriate or whether the raw data needs adjustment.

3. **Build Multivariate Regression Models**
Simple linear regression examines one feature at a time, but home prices are influenced by multiple factors simultaneously. A multivariate model that includes both Gr Liv Area and Overall Qual, along with other strong predictors, can significantly improve accuracy. This step allows you to evaluate how features interact and how much each contributes when controlling for others. It also moves the project closer to real‑world predictive modeling.

4. **Compare Models Using a Summary Table**
Once multiple models are built, it is helpful to compare them side‑by‑side using metrics such as R², RMSE, and residual behavior. A summary table makes it easy to see which model performs best and why. This comparison also highlights trade‑offs between interpretability and predictive power. Including such a table strengthens the analytical depth of the project and provides a clear justification for model selection.

5. **Investigate Non‑Linear or Tree‑Based Models**
If residual plots show curvature or patterns that a straight line cannot capture, it may be appropriate to explore more flexible models. Techniques such as polynomial regression, decision trees, or random forests can model complex relationships without requiring strict linearity. While these models are more advanced, they can reveal structure in the data that simple linear regression misses. This step demonstrates awareness of modern modeling approaches and provides a path for future project expansion.

For data suggestions, please see [data/raw/README.md](data/raw/README.md).

## Instructions

Follow the
[step-by-step workflow guide](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to complete:

## Success
```shell
========================
Executed successfully!
========================
```

## Command Reference

<details>
<summary>Show command reference</summary>

### In a machine terminal (open in your `Repos` folder)

After you get a copy of this repo in your own GitHub account,
open a machine terminal in your `Repos` folder:

```shell
# Replace username with YOUR GitHub username.
git clone https://github.com/justicetefera/datafun-07-regression

cd datafun-07-regression
code .
```

### In a VS Code terminal

```shell
uv self update
uv python pin 3.14
uv lock --upgrade
uv sync --extra dev --extra docs --upgrade

uvx pre-commit install

git add -A
uvx pre-commit run --all-files
# repeat if changes were made
uvx pre-commit run --all-files

# run the penguin example: is there a linear relationship?
uv run python -m datafun.app_penguins_case

# run the co2 example: is there a linear relationship?
# the line fits poorly; why?  what would you change?
uv run python -m datafun.app_co2_case

# do chores
uv run python -m pyright
uv run python -m pytest
uv run python -m zensical build

# save progress
git add -A
git commit -m "update"
git push -u origin main
```

</details>

## Script outcome

```shell
2026-06-21 04:16:55 | INFO | JT | === RUN START ===
2026-06-21 04:16:55 | INFO | JT | project=REGRESSION
2026-06-21 04:16:55 | INFO | JT | repo_dir=datafun-07-regression
2026-06-21 04:16:55 | INFO | JT | python=3.14.5
2026-06-21 04:16:55 | INFO | JT | os=Windows 11
2026-06-21 04:16:55 | INFO | JT | shell=powershell
2026-06-21 04:16:55 | INFO | JT | cwd=.
2026-06-21 04:16:55 | INFO | JT | github_actions=False
2026-06-21 04:16:55 | INFO | JT | Loading dataset: housing
2026-06-21 04:16:55 | INFO | JT | Loaded: 2930 rows, 83 columns
2026-06-21 04:16:55 | INFO | JT | Creating modeling view (dropping rows missing feature or target)
2026-06-21 04:16:55 | INFO | JT | Original rows: 2930
2026-06-21 04:16:55 | INFO | JT | Model rows:    2930
2026-06-21 04:16:55 | INFO | JT | Rows dropped:  0
2026-06-21 04:16:55 | INFO | JT | Building feature matrix X and target vector y
2026-06-21 04:16:55 | INFO | JT | Fitting linear regression model
2026-06-21 04:16:55 | INFO | JT | Fitted line: SalePrice = 111.694 * Gr Liv Area + 13289.6
2026-06-21 04:16:55 | INFO | JT | Computing fitted values
2026-06-21 04:16:55 | INFO | JT | R-squared: 0.4995
2026-06-21 04:16:55 | INFO | JT | RMSE: 56,504.88
2026-06-21 04:16:55 | INFO | JT | Computing residuals
2026-06-21 04:16:55 | INFO | JT | Creating scatter plot with fitted line
2026-06-21 04:16:56 | INFO | JT | Creating residual plot
2026-06-21 04:16:57 | INFO | JT | ========================
2026-06-21 04:16:57 | INFO | JT | SUMMARY
2026-06-21 04:16:57 | INFO | JT | ========================
2026-06-21 04:16:57 | INFO | JT | Dataset: housing
2026-06-21 04:16:57 | INFO | JT | Feature (x): Gr Liv Area
2026-06-21 04:16:57 | INFO | JT | Target  (y): SalePrice
2026-06-21 04:16:57 | INFO | JT | Original rows: 2930
2026-06-21 04:16:57 | INFO | JT | Model rows:    2930
2026-06-21 04:16:57 | INFO | JT | Fitted line: SalePrice = 111.694 * Gr Liv Area + 13289.6
2026-06-21 04:16:57 | INFO | JT | ========================
2026-06-21 04:16:57 | INFO | JT | === RUN START ===
2026-06-21 04:16:57 | INFO | JT | project=REGRESSION: Overall Qual vs SalePrice
2026-06-21 04:16:57 | INFO | JT | repo_dir=datafun-07-regression
2026-06-21 04:16:57 | INFO | JT | python=3.14.5
2026-06-21 04:16:57 | INFO | JT | os=Windows 11
2026-06-21 04:16:57 | INFO | JT | shell=powershell
2026-06-21 04:16:57 | INFO | JT | cwd=.
2026-06-21 04:16:57 | INFO | JT | github_actions=False
2026-06-21 04:16:57 | INFO | JT | Loading dataset: housing
2026-06-21 04:16:57 | INFO | JT | Loaded: 2930 rows, 83 columns
2026-06-21 04:16:57 | INFO | JT | Original rows: 2930
2026-06-21 04:16:57 | INFO | JT | Model rows:    2930
2026-06-21 04:16:57 | INFO | JT | Rows dropped:  0
2026-06-21 04:16:57 | INFO | JT | Fitted line: SalePrice = 45251 * Overall Qual + -95003.6
2026-06-21 04:16:57 | INFO | JT | R-squared: 0.6388
2026-06-21 04:16:57 | INFO | JT | RMSE: 48,002.35
2026-06-21 04:16:58 | INFO | JT | ========================
2026-06-21 04:16:58 | INFO | JT | SUMMARY
2026-06-21 04:16:58 | INFO | JT | ========================
2026-06-21 04:16:58 | INFO | JT | Dataset: housing
2026-06-21 04:16:58 | INFO | JT | Feature (x): Overall Qual
2026-06-21 04:16:58 | INFO | JT | Target  (y): SalePrice
2026-06-21 04:16:58 | INFO | JT | Original rows: 2930
2026-06-21 04:16:58 | INFO | JT | Model rows:    2930
2026-06-21 04:16:58 | INFO | JT | Fitted line: SalePrice = 45251 * Overall Qual + -95003.6
2026-06-21 04:16:58 | INFO | JT | ========================
```

## Findings and Visuals



Update these figures to present interesting results from your custom project:


## World Data: Is there a linear relationship? How can you improve the analysis?


## Project Documentation

Additional instructions, terms, and project notes:

[docs/index.md](docs/index.md)

## Citation

[CITATION.cff](./CITATION.cff)

## License

[MIT](./LICENSE)
