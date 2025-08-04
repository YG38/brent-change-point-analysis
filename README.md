# Brent Oil Price Change Point Analysis

## Project Overview
This project analyzes how major geopolitical and economic events impact Brent crude oil prices using Bayesian change point analysis. The analysis identifies significant structural breaks in the price series and correlates them with historical events to provide actionable insights for investors and policymakers.

## Final Submission

### Key Deliverables
1. **Final Report**: Comprehensive analysis document (`docs/final_report.md`)
2. **Jupyter Notebooks**:
   - `01_initial_analysis.ipynb`: Initial data exploration
   - `02_final_analysis.ipynb`: Complete Bayesian change point analysis
3. **Interactive Dashboard**: Streamlit app for exploring results (`dashboard.py`)
4. **Data**:
   - Raw data in `data/raw/`
   - Processed datasets in `data/processed/`

### How to Use

#### 1. Setup Environment
```bash
# Clone the repository
git clone https://github.com/YG38/brent-change-point-analysis.git
cd brent-change-point-analysis

# Create and activate virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements-final.txt
```

#### 2. Run the Analysis
```bash
# Launch Jupyter Lab
jupyter lab

# Or run the Streamlit dashboard
streamlit run dashboard.py
```

#### 3. Explore the Results
- View the final report: `docs/final_report.md`
- Run the Jupyter notebooks in the `notebooks/` directory
- Interact with the dashboard: http://localhost:8501

## Repository Structure
```
brent-change-point-analysis/
├── data/                    # Data files
│   ├── raw/                # Original data
│   └── processed/          # Processed data
├── docs/                   # Documentation
│   ├── interim_report.md   # Interim submission
│   └── final_report.md     # Final analysis report
├── notebooks/              # Jupyter notebooks
│   ├── 01_initial_analysis.ipynb
│   └── 02_final_analysis.ipynb
├── dashboard.py            # Interactive dashboard
├── requirements-final.txt  # Python dependencies
└── README.md
```

## Key Findings
1. **Change Points**: Identified 5 major structural breaks in the price series
2. **Event Impact**: Quantified the impact of key events on oil prices
3. **Volatility Analysis**: Documented patterns in price volatility
4. **Predictive Insights**: Developed framework for anticipating price movements

## License
MIT License
