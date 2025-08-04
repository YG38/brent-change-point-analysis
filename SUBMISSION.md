# Interim Submission: Brent Oil Price Change Point Analysis

## Submission Overview
This document outlines the interim submission for the Brent Oil Price Change Point Analysis project. The submission includes:

1. **Interim Report**: Detailed plan and methodology
2. **Event Data**: Structured dataset of key events
3. **Initial Analysis**: Jupyter notebook with preliminary exploration
4. **Project Structure**: Organized directory layout

## How to Review This Submission

### 1. Review the Interim Report
Location: `docs/interim_report.md`
- Project overview and objectives
- Detailed data analysis workflow
- Key events and their expected impacts
- Assumptions and limitations
- Communication plan

### 2. Examine the Event Data
Location: `data/raw/events_tabdata.csv`
- 13 key geopolitical and economic events
- Event dates, types, and expected impacts
- Impact direction and sources

### 3. Explore the Initial Analysis
Location: `notebooks/01_initial_analysis.ipynb`
- Data loading and inspection
- Initial visualizations
- Basic statistics and data quality checks
- Next steps for analysis

### 4. Project Structure
```
brent-change-point-analysis/
├── data/                    # Data files
│   ├── raw/                # Original data (BrentOilPrices.csv, events_tabdata.csv)
│   └── processed/          # Processed data (to be added)
├── docs/                   # Documentation
│   └── interim_report.md   # Interim submission report
├── notebooks/              # Jupyter notebooks
│   └── 01_initial_analysis.ipynb
└── README.md               # Project overview
```

## Next Steps
1. **Data Preprocessing**: Clean and prepare the data for analysis
2. **Time Series Analysis**: Explore trends, seasonality, and stationarity
3. **Change Point Detection**: Implement Bayesian change point model
4. **Impact Analysis**: Correlate change points with events
5. **Dashboard Development**: Create interactive visualizations

## Dependencies
All required Python packages are listed in `requirements.txt`. Install them using:
```bash
pip install -r requirements.txt
```

## Questions?
For any questions about this submission, please contact the project team.
