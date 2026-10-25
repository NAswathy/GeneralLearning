from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Employee:
    name: str
    birthday: date | None
    hire_date: date | None


@dataclass(frozen=True)
class Celebration:
    name: str
    kind: str
    years: int | None = None

    @property
    def description(self) -> str:
        if self.kind == "birthday":
            return f"{self.name}'s birthday"
        return f"{self.name}'s {self.years}-year work anniversary"