# 📚Project Documentation
This project demonstrates how to apply simple linear regression to real‑world housing data.
Using the Ames Housing dataset (≈2,930 homes), the project examines how individual home features relate to SalePrice.

## 📈Regression 1: Gr Liv Area → SalePrice
| Metric | Value | Interpretation |
| --- | --- | --- |
| **R²** | 0.4995 | About 50% of the variation in sale price is explained by above‑ground living area — a moderate linear relationship. |
| **RMSE** | $56 504.88 | Predictions differ from actual sale prices by roughly $56k on average, a realistic spread for housing data. |

### 🔎Interpretation
The fitted‑line plot shows a clear upward trend: larger homes tend to sell for more. This relationship is meaningful but not perfect. The residual plot displays a funnel shape, where prediction errors increase for larger homes. This indicates heteroscedasticity — the variance of sale prices grows as square footage increases.

This model captures the general trend that size influences price, but it cannot fully account for the wide variability among large homes. Factors such as quality, neighborhood, renovations, and lot size also play major roles. As a result, the linear model is useful for understanding broad pricing patterns but is not highly precise for individual predictions.

## 📉Residual Analysis
The residual plot reveals:
- **Increasing spread** as home size increases
- **Non‑constant variance**, suggesting heteroscedasticity
- **Greater unpredictability** among large homes

This means:

- A straight line is a reasonable but imperfect fit
- Size alone cannot fully explain price differences
- Additional features would improve predictive accuracy

### 📈Regression 2: Overall Qual → SalePrice
| Metric | Value | Interpretation |
| --- | --- | --- |
| **R²** | 0.6388 | About 64% of the variation in sale price is explained by overall quality — a strong linear relationship. |
| **RMSE** | $48 002.35 | Predictions differ from actual sale prices by about $48k on average, indicating better accuracy than the Gr Liv Area model. |

### 🔎Interpretation
Overall Quality is one of the strongest predictors of home sale price in the Ames dataset. The fitted‑line plot shows a steep, clean upward trend: higher‑quality homes consistently sell for more. Compared to Gr Liv Area, this relationship is tighter, more linear, and more stable.

The residuals are more evenly scattered around zero, indicating that the linear model fits this predictor well. Buyers place significant value on materials, craftsmanship, and finish level, which explains why this feature produces the highest R² among the three regressions.

## 📉Residual Analysis

The residual plot shows:

- **More consistent variance** across quality levels
- **Less curvature or funneling**
- **A strong linear fit**

This suggests:

- Quality is a **reliable and stable** predictor
- The linear model captures the relationship well
- This regression provides **stronger predictive power** than Gr Liv Area

## 📈 Regression 3: Year Built → SalePrice
| Metric | Value | Interpretation |
| --- | --- | --- |
| **R²** | 0.3118 | About 31 % of the variation in sale price is explained by the year the home was built — the weakest linear relationship of the three models. |
| **RMSE** | $66 259.04 | Predictions differ from actual sale prices by roughly $66k on average, the largest error among the three regressions. |

## 🔎 Interpretation

The fitted‑line plot shows a clear positive trend — newer homes tend to sell for more. However, this relationship is noticeably weaker than the patterns observed for Gr Liv Area and Overall Qual. The residuals display substantial spread, especially among older homes, indicating that age alone is not a reliable predictor of price.

A major reason for this weaker relationship is the presence of historic and antique homes in the dataset. The oldest home in the data was built in 1872, and properties from the late 1800s and early 1900s behave very differently from modern homes. Some are fully restored and command premium prices, while others require major repairs and sell for much less. Renovations, neighborhood effects, and architectural uniqueness all disrupt the simple “newer = more expensive” pattern.

This explains why the R² is lower and the RMSE is higher than the other models:
Year Built captures long‑term trends, but it cannot account for the wide variability introduced by historic homes and remodels.

## 📉 Residual Analysis

The residual plot for Year Built reveals:

- Wide scatter for older homes, especially those built before 1930
- More consistent predictions for homes built after ~1980
- No strong curvature, but clear variability across age groups

These patterns suggest:

- Age matters, but not as strongly as size or quality
- Renovations and remodels significantly alter a home’s effective age
- A simple linear model is acceptable, but not highly predictive

## 📊 Overall Findings (All Three Regressions)
| Feature | R² | RMSE | Strength |
| --- | --- | --- | --- |
| **Overall Qual** | 0.6388 | $48k | Strongest predictor |
| **Gr Liv Area** | 0.4995 | $56k | Moderate predictor |
| **Year Built** | 0.3118 | $66k | Weakest predictor |

## Key Insights

- **Quality** explains the most variation in price — craftsmanship and materials matter greatly.
- **Size** is important but less consistent, especially for large homes.
- **Age** influences price, but historic homes and remodels weaken the linear pattern.

Together, these models show that no single feature fully explains home prices, but each contributes a different piece of the story.

## 🧠 Conclusion
The expanded analysis confirms that home prices in Ames are shaped by multiple factors, each with different levels of predictive power. Overall Quality is the strongest single predictor, reflecting how buyers value materials, craftsmanship, and finish level. Gr Liv Area also plays a major role, capturing the general trend that larger homes tend to sell for more, though with greater variability at higher square footages.

Year Built provides insight into long‑term market trends, but its predictive power is limited by the presence of historic homes and the impact of renovations. Homes built in the late 1800s and early 1900s introduce substantial variability, making age a weaker standalone predictor.

These results highlight the importance of combining structural features (size), qualitative assessments (quality), and temporal characteristics (age) to understand housing prices. While simple linear regression provides valuable insight into individual relationships, a more complete predictive model would incorporate multiple features simultaneously to capture the full complexity of the housing market.

# Custom Project

# 🧱Basis
For this project, I began with the example regression workflow provided in the course, specifically the CO₂ case study that demonstrated how to load a dataset, prepare a modeling view, fit a linear regression model, compute fitted values, examine residuals, and generate visualizations. Using that workflow as a foundation, I applied the same structure to the Ames Housing dataset. My input data came from `data/raw/housing.csv`, which contains 2,930 rows and 83 columns describing residential properties in Ames, Iowa. I used the example script as a guide for organizing my functions, logging steps, and producing a complete regression analysis.

# 🛠️Phase 4 Modifications
For Phase 4, I made a small but meaningful technical modification to my regression script. I added a new function that computes R‑squared and RMSE using scikit‑learn’s `r2_score` and `mean_squared_error`. I chose this modification because the example script emphasized the importance of evaluating model performance, and adding these metrics made my analysis more complete. I also customized the scatter plot visuals by assigning **red**, **white**, and **blue** colors to the points, which improved readability and aligned with my preferred visualization style. I verified that the modification worked by running the script, checking that the metrics appeared in the logs, and confirming that the updated plots were saved correctly in the `docs/images` folder.

# 🎯Phase 5 Custom Project
In Phase 5, I extended the workflow to analyze **multiple predictors** of SalePrice: Gr Liv Area, Overall Qual, and Year Built. I built a complete regression pipeline that loads the dataset, prepares a modeling view, fits the model, computes metrics, generates scatter and residual plots, and saves all visualizations automatically.

## 📄What I Learned

- Different features produce very different model performances.
- Quality is the strongest predictor, size is moderate, and age is the weakest.
- Residual plots are essential for diagnosing model fit.
- Historic homes (as early as 1872) significantly affect age‑based models.

This project applied nearly every skill from the module: data loading, cleaning, feature engineering, modeling, visualization, logging, and documentation.

## 🏛️Executive Summary
This project uses a complete simple linear regression workflow to analyze the Ames, Iowa Housing dataset and determine how individual home features influence sale price. Through a structured and repeatable analytics pipeline, the analysis evaluates three key predictors — Gr Liv Area, Overall Qual, and Year Built — and compares their performance using numerical metrics and residual diagnostics.

The results reveal a clear hierarchy of predictive strength. Overall Quality is the strongest single predictor of SalePrice, explaining approximately 64% of the variation and producing the cleanest residual patterns. Gr Liv Area shows a moderate relationship, capturing broad pricing trends but exhibiting increasing variability for larger homes. Year Built is the weakest predictor, largely due to the presence of historic homes — some built as early as 1872 — which introduce substantial variability and disrupt the linear trend between age and price.

Residual analysis played a critical role in diagnosing model behavior. Funnel shapes, uneven variance, and wide scatter among older homes highlighted where linear assumptions held and where they broke down. These visual diagnostics provided insight beyond R² and RMSE, revealing why certain models performed better and where simple linear regression reached its limitations.

Throughout the project, nearly every core data analytics skill was applied: loading and inspecting raw data, cleaning and engineering features, constructing modeling views, fitting regression models, computing performance metrics, generating visualizations, interpreting residuals, and writing clear documentation. The workflow demonstrates how to move from raw data to meaningful statistical insight using a transparent, reproducible process.

Overall, the project shows that while simple linear regression provides valuable first‑step understanding of individual relationships, housing prices are influenced by multiple interacting factors. A more complete predictive model will require combining features, applying transformations, and exploring more flexible modeling techniques.

## 📌Next Steps for Further Analysis
1. **Build a Multivariate Regression Model**

A natural next step is to move beyond single‑feature models and build a multivariate regression that includes Gr Liv Area, Overall Qual, Year Built, and other strong predictors. This approach allows the model to account for multiple influences simultaneously, improving accuracy and revealing how features interact when controlling for one another. A multivariate model will also help determine which features remain significant once others are included.

2. **Explore Additional Predictive Features**

The Ames dataset contains many numerical variables that may provide stronger or complementary predictive power. Features such as Total Basement Area, Garage Area, 1st Floor SF, and Lot Area often show meaningful linear relationships with SalePrice. Testing these variables individually and in combination can help identify which characteristics contribute most to home value and whether structural, qualitative, or age‑related features dominate.

3. **Analyze Decade‑Level Trends and Historic Home Effects**

Since the dataset includes homes built as early as 1872, age‑related patterns are not linear. Grouping homes by decade (e.g., 1900s, 1910s, 1920s, …) can reveal clearer temporal trends and help isolate the impact of historic homes. This analysis can show whether certain eras consistently command higher or lower prices and whether remodels or architectural styles influence value differently across time periods.

4. **Apply Transformations to Improve Linearity**

Some relationships become more linear after applying mathematical transformations. Taking the logarithm of SalePrice can stabilize variance and reduce the influence of extreme values. Similarly, applying log or square‑root transformations to skewed predictors (such as Gr Liv Area or Total Bsmt SF) can produce cleaner residual patterns. This step helps determine whether linear regression is appropriate or whether the raw data needs adjustment.

5. **Investigate Non‑Linear and Tree‑Based Models**

If residual plots continue to show curvature or inconsistent variance, more flexible models may be appropriate. Techniques such as polynomial regression, decision trees, random forests, or gradient boosting can capture complex relationships that simple linear regression cannot. These models can reveal structure in the data that linear models miss and provide a more realistic representation of how multiple housing features interact.

[⭐ **Workflow: Apply Example**](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to get these projects running on your machine.
