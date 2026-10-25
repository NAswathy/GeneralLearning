from datetime import date
from collections.abc import Iterable

from .models import Celebration, Employee


def celebrations_on(employees: Iterable[Employee], day: date) -> list[Celebration]:
    celebrations: list[Celebration] = []
    for employee in employees:
        if employee.birthday and (employee.birthday.month, employee.birthday.day) == (day.month, day.day):
            celebrations.append(Celebration(employee.name, "birthday"))

        if employee.hire_date and (employee.hire_date.month, employee.hire_date.day) == (day.month, day.day):
            years = day.year - employee.hire_date.year
            if years > 0:
                celebrations.append(Celebration(employee.name, "anniversary", years))

    return sorted(celebrations, key=lambda item: (item.kind, item.name.casefold()))