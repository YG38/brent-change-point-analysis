# Interim Report: Brent Oil Price Change Point Analysis

## 1. Project Overview
This report outlines the planned approach for analyzing how major geopolitical and economic events impact Brent crude oil prices using Bayesian change point analysis. The project aims to identify significant structural breaks in the price series and correlate them with known historical events.

## 2. Data Analysis Workflow

### 2.1 Data Collection & Preparation
- **Data Source**: Historical daily Brent crude oil prices (05/20/1987 - 09/30/2022)
- **Data Cleaning**:
  - Handle missing values using appropriate imputation
  - Convert date formats
  - Check for and remove duplicates
  - Handle outliers using robust statistical methods

### 2.2 Exploratory Data Analysis (EDA)
- **Time Series Visualization**:
  - Plot raw price series
  - Visualize rolling statistics (mean, std)
  - Identify visible trends and seasonality
- **Statistical Analysis**:
  - Test for stationarity (ADF, KPSS tests)
  - Analyze distribution of returns
  - Examine autocorrelation and partial autocorrelation functions

### 2.3 Change Point Detection
- **Model Selection**: Bayesian Change Point Model using PyMC3
- **Key Components**:
  - Define priors for change points
  - Model mean and volatility regimes
  - Implement MCMC sampling
- **Implementation Steps**:
  1. Define model structure
  2. Sample from posterior distributions
  3. Analyze trace plots for convergence
  4. Identify most probable change points

### 2.4 Event Correlation Analysis
- **Event Data Collection**:
  - Compile major geopolitical/economic events
  - Include OPEC decisions, conflicts, economic crises
  - Document event dates and expected impact
- **Correlation Analysis**:
  - Compare change points with event timeline
  - Quantify price impacts around events
  - Assess statistical significance

## 3. Key Events (Tabdata)

| Date       | Event Type          | Description | Expected Impact |
|------------|---------------------|-------------|-----------------|
| 1990-08-02 | Gulf War           | Iraq invades Kuwait | Sharp price increase |
| 2001-09-11 | Terrorism          | 9/11 Attacks | Market uncertainty |
| 2008-07-11 | Economic Crisis    | Global Financial Crisis | Price collapse |
| 2014-11-27 | OPEC Decision      | OPEC maintains production | Price decline |
| 2016-11-30 | OPEC Decision      | First production cut in 8 years | Price recovery |
| 2020-03-09 | Demand Shock       | COVID-19 pandemic | Historic price drop |
| 2020-04-20 | Market Structure   | Negative oil prices | Unprecedented market conditions |
| 2021-11-04 | Geopolitical       | OPEC+ maintains gradual output increase | Price stability |
| 2022-02-24 | Geopolitical       | Russia-Ukraine conflict | Price volatility |

## 4. Assumptions and Limitations

### 4.1 Key Assumptions
1. **Market Efficiency**: Prices reflect all available information
2. **Event Impact**: Major events cause observable structural breaks
3. **Data Quality**: Historical prices are accurate and complete
4. **Model Suitability**: Bayesian change point model is appropriate for this analysis

### 4.2 Limitations
1. **Correlation vs. Causation**: Identified change points may correlate with events but don't prove causation
2. **Multicollinearity**: Events may be correlated, making it hard to isolate individual impacts
3. **Data Limitations**: Limited to available historical data (1987-2022)
4. **Model Limitations**: Assumes a fixed number of change points
5. **External Factors**: Other unobserved variables may influence prices

## 5. Communication Plan

### 5.1 Deliverables
1. **Interactive Dashboard**:
   - Time series visualization with change points
   - Event timeline overlay
   - Key statistics and metrics

2. **Final Report**:
   - Executive summary
   - Methodology
   - Key findings
   - Business implications
   - Technical appendix

### 5.2 Target Audience
- **Primary**: Energy market analysts, investors, policymakers
- **Secondary**: Academic researchers, students

### 5.3 Communication Channels
1. **Interactive Web Application** (Flask/React)
2. **Technical Report** (PDF)
3. **Presentation Slides** (for stakeholder briefings)
4. **Jupyter Notebooks** (for technical audience)

## 6. Next Steps
1. Complete data cleaning and preprocessing
2. Implement Bayesian change point model
3. Analyze results and validate findings
4. Develop interactive visualizations
5. Prepare final report and presentation
