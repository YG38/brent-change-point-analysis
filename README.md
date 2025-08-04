# Brent Oil Price Change Point Analysis

## Project Overview
This project analyzes how major geopolitical and economic events impact Brent crude oil prices using Bayesian change point analysis. The goal is to identify significant structural breaks in the price series and correlate them with known historical events.

## Repository Structure
```
brent-change-point-analysis/
├── data/                    # Data files
│   └── raw/                # Original data (Brent_Spot_Price.csv)
│   └── processed/          # Processed data
├── docs/                   # Documentation
│   └── interim_report.md   # Interim submission report
├── notebooks/              # Jupyter notebooks for analysis
├── src/                    # Source code
│   ├── data/               # Data processing scripts
│   ├── models/             # Model definitions
│   └── visualization/      # Visualization utilities
├── .gitignore
└── README.md
```

## Setup
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run Jupyter notebooks in the `notebooks/` directory

## Data
- **Brent_Spot_Price.csv**: Daily Brent crude oil prices from 1987-05-20 to 2022-09-30
- **events_tabdata.csv**: Key geopolitical/economic events affecting oil markets

## License
MIT License
