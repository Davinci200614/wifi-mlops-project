from dataclasses import dataclass


@dataclass
class Department:
    name: str
    budget: float


@dataclass
class Expense:
    department: str
    category: str
    amount: float
    description: str = ""
