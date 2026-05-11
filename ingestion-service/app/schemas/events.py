from pydantic import BaseModel


class EventResponse(BaseModel):
    event_type :str
    ingested_at :str
    source: str
    status: str