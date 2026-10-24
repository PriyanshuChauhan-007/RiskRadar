# RiskRadar architecture

## Product boundary

RiskRadar is an educational fraud-risk scoring platform. It does not connect to payment networks, make bank decisions, or process real customer financial data.

## Initial architecture

RiskRadar starts as a modular monolith so that the data pipeline, model lifecycle, API, persistence, and dashboard remain easy to test and understand. Services will only be split if a measured operational requirement justifies the added complexity.

```text
Transaction client
        |
        v
FastAPI validation layer
        |
        v
Feature engineering pipeline
        |
        v
Active versioned model ---- Model registry
        |
        v
Risk score + explanation
        |
        +--> PostgreSQL: transactions, predictions, alerts
        |
        +--> Monitoring: latency, errors, data drift
        |
        v
React analyst dashboard
```

## Core boundaries

### Data layer

Responsible for dataset provenance, schema checks, cleaning, temporal splitting, and reproducible artifacts.

### ML layer

Responsible for feature generation, preprocessing, model training, evaluation, threshold selection, explanations, and model metadata.

### Application layer

Responsible for request validation, scoring orchestration, persistence, alert rules, authentication, and API behavior.

### Presentation layer

Responsible for transaction search, alert review, prediction explanations, model metadata, and monitoring views.

## Key design decisions

1. **Modular monolith first:** avoids premature distributed-system complexity.
2. **Time-aware evaluation:** better represents deployment than random splitting when timestamps are available.
3. **PR-AUC and operational costs:** fraud data is imbalanced; accuracy is insufficient.
4. **Immutable model versions:** every prediction must identify the exact model and threshold used.
5. **Shared feature pipeline:** training and inference must not implement separate feature logic.
6. **Synthetic/public data only:** the project demonstrates engineering patterns without claiming production banking validity.

## Core persistence entities

- `users`
- `transactions`
- `predictions`
- `alerts`
- `model_versions`
- `drift_reports`
- `audit_events`

## Request lifecycle

1. Receive a transaction.
2. Validate the schema and business constraints.
3. Enforce transaction-idempotency rules.
4. Generate the versioned feature vector.
5. Load the active compatible model.
6. Produce probability, risk score, level, decision, and explanation.
7. Persist the transaction and prediction.
8. Create an alert when configured conditions are met.
9. Return a traceable response containing model version and threshold.
