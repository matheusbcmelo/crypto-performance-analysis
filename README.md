# Crypto Performance Analysis

This repository provides tools and Jupyter Notebooks for analyzing historical price and on-chain data of major cryptocurrencies such as BTC, ETH, BNB, SOL, XRP and AVAX.

The analysis leverages Python and popular data science libraries to fetch, process, and visualize market and tokenomics data from sources like Binance and CoinGecko.

## Features
- Fetch historical price data from Binance
- Retrieve and analyze tokenomics data from CoinGecko
- Visualize market performance and on-chain metrics
- Ready-to-use Jupyter Notebooks for interactive analysis

## Project Structure
```
notebooks/
    crypto_market_analysis.ipynb
    crypto_onchain_data.ipynb
    plots/
        html/
        png/
scripts/
    fetch_binance_data.py
requirements.txt
```

## Getting Started
1. Clone the repository.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Open the notebooks in Jupyter and follow the instructions.

## Requirements
- Python 3.8+
- Jupyter Notebook
- pandas, plotly, ccxt, requests, etc. (see requirements.txt)