from datetime import date

from openpyxl import Workbook

from birthday_anniversary_agent.workbooks import load_employees, load_recipients


def test_loads_employee_dates_and_deduplicated_recipients(tmp_path):
    events_path = tmp_path / "events.xlsx"
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "People"
    sheet.append(["Full name", "Date of birth", "Start date"])
    sheet.append(["Avery", date(1990, 9, 28), date(2021, 9, 28)])
    sheet.append([None, None, None])
    workbook.save(events_path)

    recipients_path = tmp_path / "recipients.xlsx"
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Notify"
    sheet.append(["Email address"])
    sheet.append(["team@example.com"])
    sheet.append(["team@example.com"])
    workbook.save(recipients_path)

    employees = load_employees(events_path, "People", "Full name", "Date of birth", "Start date")
    recipients = load_recipients(recipients_path, "Notify", "Email address")

    assert [(item.name, item.birthday, item.hire_date) for item in employees] == [
        ("Avery", date(1990, 9, 28), date(2021, 9, 28))
    ]
    assert recipients == ["team@example.com"]