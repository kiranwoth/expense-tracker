from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class Expense(BaseModel):
    id: UUID
    cost: float
    time_created: datetime
    description: Optional[str] = None
    category: str = "Misc"
