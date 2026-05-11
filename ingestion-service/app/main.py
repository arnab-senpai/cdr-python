from fastapi import FastAPI
from app.schemas.cdr import CDR
from app.schemas.events import EventResponse

from uuid import uuid4
from datetime import datetime

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message":"New app for CDR ingestion"
    }


@app.post("/api/v1/cdr", response_model = EventResponse)
async def ingest_cdr(cdr: CDR):

    event = EventResponse(
        event_type =str(uuid4()),
        ingested_at = datetime.utcnow().isoformat(),
        source ="fast-api-ingestion-point",
        status ="Accepted"
    )

    return event