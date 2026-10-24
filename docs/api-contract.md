# RiskRadar API contract

The public API is versioned under `/api/v1`. Error responses use a consistent shape so clients can handle validation and operational failures predictably.

## Error shape

```json
{
  "error": {
    "code": "validation_error",
    "message": "amount must be greater than zero",
    "request_id": "req_01H...",
    "details": []
  }
}
```

## System endpoints

```http
GET /health
GET /api/v1/health/readiness
```

`/health` reports process availability. Readiness additionally checks required dependencies such as the database and active model.

## Authentication

```http
POST /api/v1/auth/login
GET  /api/v1/auth/me
```

Protected routes use the authenticated user and role. Viewer users can read data but cannot activate models or change alert state.

## Scoring

```http
POST /api/v1/transactions/score
POST /api/v1/predictions/batch
GET  /api/v1/predictions/batch/{job_id}
```

The scoring response must include:

- `transaction_id`
- `fraud_probability`
- `risk_score`
- `risk_level`
- `decision`
- `model_version`
- `threshold_used`
- `explanation`
- `alert_created`

## Search and investigation

```http
GET /api/v1/transactions
GET /api/v1/transactions/{transaction_id}
GET /api/v1/alerts
GET /api/v1/alerts/{alert_id}
PATCH /api/v1/alerts/{alert_id}
```

Search endpoints are paginated and support filters for date range, risk level, alert status, merchant category, amount, and country mismatch.

## Models and monitoring

```http
GET  /api/v1/models
GET  /api/v1/models/{model_version}
POST /api/v1/models/{model_version}/activate
GET  /api/v1/monitoring/summary
GET  /api/v1/monitoring/drift
```

## Idempotency

The transaction's external `transaction_id` is the first idempotency boundary. Replaying an already-scored transaction must return the existing prediction or a clearly documented conflict; it must not create duplicate alerts.

## API design principles

- Requests are validated before feature generation.
- Responses identify the model and threshold used.
- Business errors are distinct from server errors.
- Pagination is mandatory for history endpoints.
- Sensitive values are not returned unless needed for investigation.
