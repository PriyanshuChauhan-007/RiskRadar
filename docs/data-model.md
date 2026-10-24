# RiskRadar data model

The persistence model is designed around traceability: an analyst should be able to identify the input transaction, the exact model and threshold used, the resulting prediction, and any alert created from it.

## Entities

### `users`

Stores application users. Passwords are stored only as slow password hashes; plaintext passwords are never persisted.

Key fields: `id`, `email`, `password_hash`, `role`, `is_active`, `created_at`.

Roles are `admin`, `analyst`, and `viewer`.

### `transactions`

Stores the validated input event. `transaction_id` is the external idempotency key and must be unique.

Key fields: `id`, `transaction_id`, `customer_id`, `amount`, `currency`, `merchant_category`, `merchant_country`, `customer_country`, `ip_country`, `device_id`, `payment_method`, `occurred_at`, `ingested_at`, `payload_hash`.

The raw payload is not stored by default. This limits unnecessary retention of potentially sensitive data while keeping a hash for replay detection.

### `predictions`

Stores one scoring result and its provenance.

Key fields: `id`, `transaction_id`, `model_version_id`, `fraud_probability`, `risk_score`, `risk_level`, `decision`, `threshold_used`, `explanation`, `latency_ms`, `created_at`.

`model_version_id` is required so historical results remain interpretable after a new model becomes active.

### `alerts`

Represents an analyst workflow item created from a prediction.

Key fields: `id`, `prediction_id`, `severity`, `status`, `reason`, `assigned_to`, `resolution_note`, `created_at`, `resolved_at`.

Supported statuses: `open`, `investigating`, `resolved`, and `dismissed`.

### `model_versions`

Stores immutable model metadata rather than only a filename.

Key fields: `id`, `name`, `algorithm`, `version`, `artifact_uri`, `feature_schema_hash`, `dataset_hash`, `metrics`, `threshold`, `status`, `created_at`.

Only one compatible model version should be active for the scoring path at a time.

### `drift_reports`

Stores comparisons between a reference feature distribution and a current observation window.

Key fields: `id`, `feature_name`, `reference_window`, `current_window`, `metric`, `value`, `status`, `created_at`.

## Integrity rules

1. A prediction cannot exist without a transaction and model version.
2. An alert cannot exist without a prediction.
3. `transaction_id` is unique and supports idempotent ingestion.
4. Prediction records are append-only from the scoring path.
5. Model versions are immutable after registration; activation is a separate state change.
6. All timestamps are stored in UTC.
7. JSON fields contain structured metadata, not unbounded request payloads.
