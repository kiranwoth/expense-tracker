from datetime import datetime, timezone
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel


class ExpenseBase(BaseModel):
    cost: float
    description: Optional[str] = None
    category: str = "Misc"


class ExpenseCreate(ExpenseBase):
    pass


class ExpenseUpdate(BaseModel):
    cost: Optional[float] = None
    description: Optional[str] = None
    category: Optional[str] = None


class Expense(ExpenseBase):
    id: UUID = uuid4()
    time_created: datetime = datetime.now(tz=timezone.utc)
