from datetime import date
from typing import Dict

from pydantic import BaseModel


class Cashflows(BaseModel):
    cashflows: Dict[date, float]

def total_cashflows(cf: Cashflows) -> float:
    return sum(cf.cashflows.values())
