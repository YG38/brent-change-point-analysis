import json

# Define the notebook structure
notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Brent Oil Price Analysis - Initial Exploration\n",
                "\n",
                "This notebook contains the initial exploration of the Brent crude oil price data and event correlations."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Import required libraries\n",
                "import pandas as pd\n",
                "import numpy as np\n",
                "import matplotlib.pyplot as plt\n",
                "import seaborn as sns\n",
                "from pathlib import Path\n",
                "\n",
                "# Set style\n",
                "sns.set(style='whitegrid')\n",
                "plt.rcParams['figure.figsize'] = [14, 6]"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 1. Load and Inspect Data"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Define file paths\n",
                "data_dir = Path('../data')\n",
                "raw_data_path = data_dir / 'raw/BrentOilPrices.csv'\n",
                "events_path = data_dir / 'raw/events_tabdata.csv'\n",
                "\n",
                "# Load data\n",
                "prices_df = pd.read_csv(raw_data_path, parse_dates=['Date'], dayfirst=True)\n",
                "events_df = pd.read_csv(events_path, parse_dates=['event_date'])\n",
                "\n",
                "# Display basic info\n",
                "print(\\\"\\\\nBrent Oil Prices Data:\\\")\n",
                "print(\\\"=\\\" * 50)\n",
                "prices_df.info()\n",
                "\n",
                "print(\\\"\\\\n\\\\nEvents Data:\\\")\n",
                "print(\\\"=\\\" * 50)\n",
                "events_df.info()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 2. Initial Data Visualization"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Plot price time series\n",
                "plt.figure(figsize=(16, 8))\n",
                "plt.plot(prices_df['Date'], prices_df['Price'], label='Daily Price', alpha=0.7)\n",
                "plt.title('Brent Crude Oil Prices (1987-2022)', fontsize=16)\n",
                "plt.xlabel('Year', fontsize=12)\n",
                "plt.ylabel('Price (USD/barrel)', fontsize=12)\n",
                "plt.grid(True, alpha=0.3)\n",
                "\n",
                "# Add event markers\n",
                "for _, event in events_df.iterrows():\n",
                "    plt.axvline(x=event['event_date'], color='red', alpha=0.3, linestyle='--')\n",
                "    plt.text(event['event_date'], plt.ylim()[1]*0.9, event['event_name'], \n",
                "             rotation=90, va='top', ha='right', alpha=0.7)\n",
                "\n",
                "plt.legend()\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 3. Basic Statistics and Data Quality"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Basic statistics\n",
                "print(\\\"Brent Oil Prices - Basic Statistics\\\")\n",
                "print(\\\"=\\\" * 50)\n",
                "print(prices_df['Price'].describe().round(2))\n",
                "\n",
                "# Check for missing values\n",
                "print(\\\"\\\\nMissing Values:\\\")\n",
                "print(\\\"=\\\" * 50)\n",
                "print(prices_df.isnull().sum())"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 4. Next Steps for Analysis"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "1. **Data Preprocessing**:\\n",
                "   - Handle any missing values\\n",
                "   - Check for and handle outliers\\n",
                "   - Create additional features (e.g., rolling statistics, returns)\\n",
                "\\n",
                "2. **Time Series Analysis**:\\n",
                "   - Test for stationarity (ADF, KPSS tests)\\n",
                "   - Analyze autocorrelation and partial autocorrelation\\n",
                "   - Decompose the time series into trend, seasonality, and residuals\\n",
                "\\n",
                "3. **Change Point Detection**:\\n",
                "   - Implement Bayesian change point detection\\n",
                "   - Identify significant structural breaks\\n",
                "   - Correlate with known events\\n",
                "\\n",
                "4. **Impact Analysis**:\\n",
                "   - Quantify price impacts around change points\\n",
                "   - Compare pre- and post-event statistics\\n",
                "   - Build interactive visualizations"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.8.0"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

# Write the notebook to a file
with open('notebooks/01_initial_analysis.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=2, ensure_ascii=False)
