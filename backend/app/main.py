from fastapi import FastAPI
from datetime import datetime, timezone
from typing import List
from uuid import UUID, uuid4
from pydantic import BaseModel, ConfigDict, Field

app = FastAPI()

#
# In-memory storage (Milestone: Incidents API skeleton)
#
INCIDENTS: list["IncidentOut"] = []


class IncidentCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=120)
    description: str | None = Field(default=None, max_length=2000)
    severity: int = Field(..., ge=1, le=5, description="1 (low) - 5 (critical)")


class IncidentOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    title: str
    description: str | None = None
    severity: int
    created_at: datetime


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Pulse API is running"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}


@app.post("/incidents", response_model=IncidentOut, status_code=201)
def create_incident(payload: IncidentCreate) -> IncidentOut:
    incident = IncidentOut(
        id=uuid4(),
        title=payload.title,
        description=payload.description,
        severity=payload.severity,
        created_at=datetime.now(timezone.utc),
    )
    INCIDENTS.append(incident)
    return incident


@app.get("/incidents", response_model=List[IncidentOut])
def list_incidents() -> List[IncidentOut]:
    return list(reversed(INCIDENTS))