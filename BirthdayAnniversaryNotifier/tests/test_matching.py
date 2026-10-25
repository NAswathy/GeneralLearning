from datetime import date

from birthday_anniversary_agent.matching import celebrations_on
from birthday_anniversary_agent.models import Employee


def test_matches_birthday_and_completed_work_anniversary_on_day():
    employees = [
        Employee("Avery", date(1990, 9, 28), date(2021, 9, 28)),
        Employee("Jordan", date(1994, 9, 29), date(2025, 9, 28)),
    ]

    celebrations = celebrations_on(employees, date(2026, 9, 28))

    assert [(item.name, item.kind, item.years) for item in celebrations] == [
        ("Avery", "anniversary", 5),
        ("Jordan", "anniversary", 1),
        ("Avery", "birthday", None),
    ]


def test_february_29_only_matches_february_29():
    employee = Employee("Casey", date(2000, 2, 29), None)

    assert celebrations_on([employee], date(2026, 2, 28)) == []
    assert len(celebrations_on([employee], date(2028, 2, 29))) == 1