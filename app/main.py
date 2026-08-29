from fastapi import FastAPI

app = FastAPI(title="Task Manager API")


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Liveness check used by infra probes."""
    return {"status": "ok"}
