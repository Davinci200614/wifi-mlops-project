import json
from pathlib import Path
from typing import Any


DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "budget_data.json"


def load_budget_data() -> dict[str, Any]:
    if not DATA_FILE.exists():
        return {"departments": [], "expenses": []}
    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_budget_data(data: dict[str, Any]) -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
