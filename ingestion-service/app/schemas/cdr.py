from pydantic import BaseModel,Field
from typing import Literal
from datetime import datetime

class CDR(BaseModel):
    call_id: str = Field(..., description="Unique identifier for the call")
    caller: str = Field(..., description="Phone number of the caller")
    callee: str = Field(..., description="Phone number of the callee")
    start_time: datetime = Field(..., description="Start time of the call in ISO 8601 format")
    end_time: datetime = Field(..., description="End time of the call in ISO 8601 format")
    duration: int = Field(..., gt=0,description="Duration of the call in seconds")
    call_type: Literal['incoming', 'outgoing'] = Field(..., description="Type of the call")