# 📚Project Documentation
This project demonstrates how to apply simple linear regression to real‑world housing data.
Using the Ames Housing dataset (≈2,930 homes), the project examines how individual home features relate to SalePrice.

## 📈Regression 1: Gr Liv Area → SalePrice
| Metric | Value | Interpretation |
| --- | --- | --- |
| **R²** | 0.4995 | About 50 % of the variation in sale price is explained by above‑ground living area. That’s moderate — size matters, but other factors (quality, neighborhood, etc.) also influence price. |
| **RMSE** | $56 504.88 | On average, predictions differ from actual sale prices by roughly $56 500. That’s a realistic spread for housing data. |

### 🔎Interpretation
- The scatterplot should show a clear upward trend — larger homes tend to cost more.
- The residual plot likely shows a funnel shape (variance increases for larger homes).
- Because residuals aren’t perfectly random, a straight line is a reasonable but imperfect description.
- This model is useful for understanding general price trends, not precise predictions.

The relationship between above‑ground living area and sale price is positive and moderately strong. Larger homes tend to sell for more, and the fitted-line plot shows a clear upward trend.

An R² of 0.4995 means that about 50% of the variation in sale price can be explained by the size of the home alone. This is meaningful, but it also indicates that other factors (quality, neighborhood, condition, etc.) play a major role.

The RMSE of $56,504.88 indicates that predictions from this simple model typically differ from actual sale prices by around $56k. This is reasonable for housing data, where prices vary widely.

## 📉Residual Analysis
The residual plot shows increasing spread as home size increases — a funnel shape. This suggests:
- Variance is not constant (heteroscedasticity).
- A straight line is a reasonable but imperfect description.
- Larger homes have more unpredictable prices.


### 📈Regression 2: Overall Qual → SalePrice
| Metric | Value | Interpretation |
| --- | --- | --- |
| **R²** | 0.6388 | About 64 % of the variation in sale price is explained by overall quality rating — a strong linear relationship. |
| **RMSE** | $48 002.35 | Average prediction error is around $48 000, smaller than the first model, meaning better fit. |

### 🔎Interpretation
- The fitted‑line plot should show a steep, clean upward trend — higher‑quality homes sell for more.
- Residuals are likely more evenly scattered, meaning the linear model fits well.
- A straight line is a fair description of this relationship.
- This model is stronger and more reliable than the Gr Liv Area model.

Overall Quality is one of the strongest predictors of home sale price in the Ames dataset. The fitted-line plot shows a clear, steep upward trend: as the quality rating increases, sale price increases sharply.

An R² of 0.6388 means that about 64% of the variation in sale price can be explained by the quality rating alone. This is a strong linear relationship, especially for a single‑feature model.

The RMSE of $48,002.35 is lower than the RMSE from the Gr Liv Area model, indicating that this regression produces more accurate predictions.

## 📉Residual Analysis
The residuals appear more evenly scattered compared to the Gr Liv Area model. This suggests:
- Variance is more consistent across quality levels
- The linear model fits the data well
- There is less curvature or funneling in the residuals
This makes Overall Qual a better candidate for linear regression.

## 🧠 Conclusion
Overall Quality and Gr Liv Area both help explain variation in home prices, but they do so with different levels of strength and reliability. Gr Liv Area is a useful predictor because larger homes generally sell for more, and the linear model captures this broad trend. However, the relationship shows increasing spread at higher square footages, indicating that size alone cannot fully account for price differences. This suggests that while the model provides meaningful insight, it does not capture the full complexity of the housing market and should be supplemented with additional features or nonlinear transformations to improve accuracy.

In contrast, Overall Quality demonstrates a much stronger and more consistent relationship with SalePrice. The linear model fits this predictor more cleanly, with less variability in the residuals and a noticeably higher R² value. This indicates that buyers place significant value on construction quality, materials, and craftsmanship—factors that influence price more directly and reliably than size alone. As a result, the Overall Quality regression offers clearer insight and stronger predictive power.

Taken together, these results show that while physical size contributes to home value, qualitative characteristics of the home play an even more important role. A comprehensive predictive model should therefore incorporate both structural attributes (like square footage) and qualitative assessments (like overall quality) to more accurately reflect the factors that drive housing prices.

## 📊 Overall Findings
Both regressions reveal meaningful relationships between home features and sale price. However:
- Overall Qual provides a stronger linear fit
- Gr Liv Area shows more variability
- Both models highlight important aspects of home valuation

Both regressions confirm that individual home features meaningfully influence sale price, but they differ in how strongly they explain that variation. Overall Quality produces a cleaner, more reliable linear relationship, with tighter residuals and stronger predictive performance. Gr Liv Area also shows a positive trend, but the wider spread in its residuals indicates greater variability and less consistent predictive power. Together, the models show that while size contributes to home value, quality captures a larger share of what drives price differences in the Ames housing market.

Simple linear regression is useful, but more advanced models may capture additional complexity.

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

See
[⭐ **Workflow: Apply Example**](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to get these projects running on your machine.
