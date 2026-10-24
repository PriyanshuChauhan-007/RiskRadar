"""HTTP application entry point for RiskRadar."""

from fastapi import FastAPI


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="RiskRadar API",
        version="0.1.0",
        description=(
            "Educational fraud-risk scoring API using public or synthetic transaction data."
        ),
    )

    @app.get("/health", tags=["system"])
    def health() -> dict[str, str]:
        """Report that the HTTP process is available."""
        return {"status": "ok", "service": "riskradar-api"}

    return app


app = create_app()
