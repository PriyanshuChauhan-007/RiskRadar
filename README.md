# RiskRadar

RiskRadar is a production-style, explainable transaction fraud-risk scoring platform built for a B.Tech final-year project and portfolio demonstration.

It is designed to accept transaction data, validate it, generate behavioral features, score fraud risk, explain predictions, persist prediction history, create alerts, and monitor input drift.

> **Responsible-use note:** RiskRadar uses public and/or synthetic transaction data. It is an educational and research prototype, not a real banking fraud-detection system and not a financial decision-making product.

## Project status

The repository is being built incrementally. Each milestone is implemented with tests, measured evaluation, and documentation rather than placeholder metrics or hard-coded demo results.

## Planned capabilities

- Data validation and reproducible feature engineering
- Comparison of interpretable and tree-based fraud models
- Imbalance-aware precision, recall, F1, ROC-AUC, and PR-AUC evaluation
- Cost-sensitive decision-threshold selection
- Real-time and batch prediction APIs
- Explainable prediction results
- PostgreSQL-backed transaction, prediction, and alert history
- Model version tracking
- Analyst dashboard with search and filtering
- Basic data-drift and application monitoring
- Authentication and role-based access
- Docker Compose development environment

## Development principles

- No invented performance numbers: evaluation results are generated from actual runs.
- Time-aware validation is preferred where the data supports it.
- Training and inference share the same feature pipeline.
- Model explanations are attribution signals, not claims of causality.
- Dependencies are added only when they solve a demonstrated problem.

## Planned stack

- Python, FastAPI, Pandas, NumPy, scikit-learn
- PostgreSQL
- React
- Pytest
- Docker Compose

## Documentation

- [Architecture and roadmap](docs/architecture.md)
- [Project roadmap](docs/roadmap.md)
- [Architecture decisions](docs/decisions.md)
- [Data model](docs/data-model.md)
- [API contract](docs/api-contract.md)

## Local development

Create a virtual environment, install the project with development tools, and run the API:

```bash
python -m venv .venv
python -m pip install -e ".[dev]"
uvicorn backend.app.main:app --reload
```

The initial system check is available at `http://127.0.0.1:8000/health`.

Run the current quality checks with:

```bash
ruff check .
pytest
```

## License

This project is intended for educational and portfolio use. A formal license will be added before the first public release.
