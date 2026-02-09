# Regime Detection for Ethereum Market Activity

eth-regimes is a small machine-learning project that identifies market "regimes" in Ethereum (ETH) time-series using clustering on volume and market cap. The goal is to label days (or periods) into interpretable regimes such as:
- Low activity / Bearish periods
- Stable / Consolidation phases
- Bullish / Accumulation phases
- High volatility / Event-driven days

The repo contains feature engineering for daily ETH market data, clustering pipelines, visualizations, and a Streamlit dashboard to explore regimes and associated business/analysis insights.

---

## Demo


https://github.com/user-attachments/assets/adf2500b-d6ec-4e49-8597-a8ae3000b608


## Key features

- Ingests daily Ethereum market data (price, volume, market cap) — CSV 
- Unsupervised clustering 
- Interpretability: per-regime summary statistics
- Streamlit dashboard to explore regimes interactively

---

## Contributing

Contributions welcome. Suggested workflow:
1. Open an issue describing the feature or bug
2. Fork the repo and create a feature branch
3. Add tests and update docs
4. Open a pull request
