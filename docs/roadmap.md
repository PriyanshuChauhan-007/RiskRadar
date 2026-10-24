# RiskRadar implementation roadmap

The project is divided into focused sessions. Each session should produce a reviewable change, meaningful tests or measurements, and a concise commit. No metric is published until it is produced by an actual evaluation run.

## Phase 0 — Foundation

1. Repository initialization and engineering standards
2. Architecture and system-design documentation
3. Reproducible local development environment

## Phase 1 — Data engineering

4. Dataset acquisition and provenance
5. Reproducible synthetic transaction generator
6. Data validation and quality reporting
7. Temporal splitting and leakage prevention

## Phase 2 — Machine learning

8. Interpretable feature engineering
9. Shared preprocessing pipeline
10. Logistic-regression baseline
11. Tree-based model comparison
12. Class-imbalance experiments
13. Cost-sensitive threshold selection
14. Probability calibration
15. Local and global explainability
16. Model registry and reproducibility metadata

## Phase 3 — Backend platform

17. Database schema and migrations
18. FastAPI foundation
19. Transaction validation endpoint
20. Real-time scoring endpoint
21. Batch scoring
22. Alert management
23. Authentication and authorization
24. Transaction search and filtering

## Phase 4 — Dashboard

25. React dashboard foundation
26. Risk overview dashboard
27. Transaction investigation view
28. Alert management interface
29. Model and monitoring interface

## Phase 5 — Production polish

30. Data-drift monitoring
31. Error logging and observability
32. Test and quality gates
33. Security and privacy review
34. Deployment packaging
35. Final measured evaluation report
36. Resume, portfolio, and demo preparation

## Definition of done for each session

- The requested behavior exists in the codebase.
- Tests or an appropriate measurement verify it.
- Documentation reflects the real behavior.
- No unrelated placeholder infrastructure is added.
- A focused commit explains the change.
