# Architecture decision records

## ADR-001: Start with a modular monolith

RiskRadar begins as a modular monolith because the project is primarily demonstrating a complete ML product lifecycle. Splitting into microservices before measuring a need would increase operational complexity without improving the learning outcome.

## ADR-002: Use a simple model registry first

The initial registry will store immutable model metadata and artifact references in a controlled local structure and database. MLflow can be evaluated later if experiment-management requirements exceed the simple registry.

## ADR-003: Treat threshold selection as a business decision

The classification threshold will be selected using explicit false-positive and false-negative costs plus operational alert-volume constraints. The default probability threshold of 0.5 will not be treated as automatically correct.
