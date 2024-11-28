# Copper Price Forecasting Using Machine Learning

## Overview
This project focuses on forecasting monthly copper prices by employing advanced machine learning techniques. The project was undertaken to address the volatile nature of the copper market, enabling companies like **MetalliQ Resources Inc.** to make informed decisions for strategic planning, budgeting, and risk management.

## Objective
To build a robust machine learning model capable of forecasting copper prices with high accuracy by analyzing historical data on commodity prices and exchange rates.

## Dataset

### Source
- **Investing.com** and other reputable financial platforms.
- Validated against multiple sources to ensure data reliability.

### Features
- **Copper Prices**: Target variable for forecasting.
- **Related Commodities**: Iron, gold, crude oil prices.
- **Exchange Rates**: USD-AUD, USD-CLP, USD-CNY, USD-PEN.
- **Time-Dependent Features**: Month encoded using cyclical transformations (sine/cosine).

### Timeframe
- **1991–2023**
- Approximately **400 rows** of data due to alignment across multiple datasets.

### Preprocessing Steps
1. **Data Cleaning**:
   - Handled missing values using **interpolation techniques**.
   - Removed outliers to ensure model accuracy.
   - Aligned features to a common timeframe and standardized currencies to USD.

2. **Normalization**:
   - Applied **Min-Max Scaling** with a range of -1 to 1.
   - Ensured separate scaling for training and testing datasets to prevent data leakage.

3. **Feature Selection**:
   - Selected essential attributes: `Price` for each commodity and currency pair, alongside date information.
   - Reduced dimensionality to focus on predictive variables.

4. **Cyclical Encoding**:
   - Transformed the `Month` feature into sine and cosine components to capture seasonal patterns effectively.

5. **Dataset Splitting**:
   - Non-random **80:20 train-test split** to preserve time-series data integrity.

---

## Machine Learning Models

### Implemented Models
1. **GA-ANN**: Genetic Algorithm-optimized Artificial Neural Network.
2. **GA-SVM**: Support Vector Machine with genetic tuning.
3. **GA-KNN**: K-Nearest Neighbors enhanced with genetic optimization.
4. **GA-GBT**: Gradient Boosting Tree.
5. **GA-RF**: Random Forest.

### Why These Models?
- Captures the **non-linear relationships** between variables (GA-ANN, GA-SVM).
- Handles high-dimensional and complex data (GA-SVM, GA-GBT, GA-RF).
- Identifies patterns in time-series data (GA-ANN, GA-KNN).

### Hyperparameter Tuning
- Used **Distributed Evolutionary Algorithms in Python (DEAP)** for fine-tuning:
  - Parameters: population size, number of generations, mutation rate, crossover rate.
  - Custom fitness functions optimized for project-specific goals (minimizing RMSE and MSE).

### Validation
- Applied **10-fold time-series cross-validation** to rigorously evaluate model robustness.
- Metrics Used:
  - Root Mean Squared Error (RMSE)
  - Mean Squared Error (MSE)
  - Mean Absolute Error (MAE)
  - Coefficient of Determination (R²)

---

## My Contributions

### 1. Dataset Acquisition and Preprocessing
- **Dataset Sourcing**: Researched, identified, and compiled datasets from reliable sources.
- **Data Cleaning**:
  - Aligned features from multiple datasets to a common timeframe.
  - Normalized data for consistent scaling across models.
  - Interpolated missing values and addressed data outliers.
- **Feature Engineering**:
  - Applied Min-Max scaling and cyclical encoding for seasonal variables.
  - Reduced dimensionality to focus on predictive variables.

### 2. Model Development
- **Artificial Neural Network (ANN)**:
  - Implemented and tuned the **GA-ANN** model for optimal performance.
  - Fine-tuned hyperparameters using **genetic algorithms**.
  - Conducted rigorous validation through time-series cross-validation.
- **Testing**:
  - Compared model performance using RMSE, MSE, MAE, and R² metrics.
  - Ensured the model generalized well to unseen test data.

### 3. Data Analysis Techniques
- **Exploratory Data Analysis (EDA)**:
  - Conducted correlation analysis to identify key relationships between features.
  - Performed regression analysis on copper prices vs. exchange rates.
  - Visualized principal components to reduce dimensionality and uncover patterns.
- **Performance Evaluation**:
  - Evaluated and compared models based on statistical metrics and hypothesis testing.
  - Ranked models using metrics to identify the best-performing solution.

---

## Results

### Best Model
- **Genetic Algorithm-Optimized Artificial Neural Network (GA-ANN)**:
  - **RMSE**: 0.1040 (Lowest among models)
  - **MSE**: 0.0108 (Lowest among models)
  - **R²**: 0.9171 (Highest among models)
  - Ranked second in **MAE**: 0.0824

### Comparative Metrics Table
| Metric | GA-ANN | GA-SVM | GA-KNN | GA-GBT | GA-RF |
|--------|--------|--------|--------|--------|--------|
| RMSE   | **0.1040** | 0.1041 | 0.1912 | 0.128 | 0.126 |
| MSE    | **0.0108** | 0.0109 | 0.0366 | 0.0162 | 0.0160 |
| MAE    | 0.0824 | **0.0811** | 0.1497 | 0.1209 | 0.1007 |
| R²     | **0.9171** | 0.9168 | 0.7200 | 0.8180 | 0.8775 |

### Recommendations
- Deploy the **GA-ANN model** for forecasting copper prices due to its superior performance across multiple metrics.
- Incorporate additional features like GDP growth, inflation, and unemployment rates to improve prediction accuracy.

---

## Tools and Technologies
- **Programming**: Python (pandas, numpy, sklearn, DEAP)
- **Data Manipulation**: Excel for feature selection and alignment
- **Validation**: 10-fold cross-validation for time-series data
- **Visualization**: Matplotlib, PCA visualizations

---

## Future Enhancements

1. **Feature Expansion**:
   - Incorporate macroeconomic indicators like GDP growth, inflation, and interest rates.
2. **Scalability**:
   - Leverage cloud platforms for real-time forecasting and increased dataset size.
3. **Deployment**:
   - Build a user-friendly interface for business stakeholders to utilize the forecasting model.

