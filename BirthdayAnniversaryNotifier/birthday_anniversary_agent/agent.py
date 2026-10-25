import json
import logging
import os
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from dotenv import load_dotenv

from .graph_mailer import GraphMailer
from .matching import celebrations_on
from .workbooks import load_employees, load_recipients

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Settings:
    events_workbook: Path
    recipients_workbook: Path
    events_sheet: str
    recipients_sheet: str
    name_column: str
    birthday_column: str
    hire_date_column: str
    email_column: str
    timezone: str
    notification_time: str
    state_file: Path
    dry_run: bool
    tenant_id: str
    client_id: str
    client_secret: str
    sender: str

    @classmethod
    def from_environment(cls) -> "Settings":
        load_dotenv()
        return cls(
            events_workbook=Path(os.getenv("EVENTS_WORKBOOK", "data/WorkAnniversary_BirthdayReminderAgent.xlsx")),
            recipients_workbook=Path(os.getenv("RECIPIENTS_WORKBOOK", "data/WorkAnniversary_BirthdayReminderAgent_EmailList.xlsx")),
            events_sheet=os.getenv("EVENTS_SHEET", "Sheet1"),
            recipients_sheet=os.getenv("RECIPIENTS_SHEET", "Sheet1"),
            name_column=os.getenv("NAME_COLUMN", "Name"),
            birthday_column=os.getenv("BIRTHDAY_COLUMN", "Birthday"),
            hire_date_column=os.getenv("HIRE_DATE_COLUMN", "Hire Date"),
            email_column=os.getenv("EMAIL_COLUMN", "Email"),
            timezone=os.getenv("TIMEZONE", "UTC"),
            notification_time=os.getenv("NOTIFICATION_TIME", "08:00"),
            state_file=Path(os.getenv("STATE_FILE", "data/sent_notifications.json")),
            dry_run=os.getenv("DRY_RUN", "true").casefold() == "true",
            tenant_id=os.getenv("AZURE_TENANT_ID", ""),
            client_id=os.getenv("AZURE_CLIENT_ID", ""),
            client_secret=os.getenv("AZURE_CLIENT_SECRET", ""),
            sender=os.getenv("GRAPH_SENDER", ""),
        )


def _message(day: date, celebrations) -> tuple[str, str]:
    subject = f"Today's birthdays and work anniversaries - {day:%B} {day.day}"
    lines = [f"Celebrations for {day:%B} {day.day}:"]
    lines.extend(f"- {item.description}" for item in celebrations)
    return subject, "\n".join(lines)


def run_for_date(settings: Settings, day: date) -> None:
    employees = load_employees(
        settings.events_workbook,
        settings.events_sheet,
        settings.name_column,
        settings.birthday_column,
        settings.hire_date_column,
    )
    celebrations = celebrations_on(employees, day)
    if not celebrations:
        logger.info("No birthdays or work anniversaries for %s", day)
        return

    recipients = load_recipients(settings.recipients_workbook, settings.recipients_sheet, settings.email_column)
    if not recipients:
        raise ValueError("The email-list workbook contains no recipients")

    sent_key = day.isoformat()
    try:
        sent_state = json.loads(settings.state_file.read_text(encoding="utf-8"))
    except FileNotFoundError:
        sent_state = {}
    if not isinstance(sent_state, dict):
        raise ValueError(f"State file must contain a JSON object: {settings.state_file}")
    already_sent = set(sent_state.get(sent_key, []))
    subject, body = _message(day, celebrations)

    if settings.dry_run:
        logger.info("DRY RUN: would notify %d recipient(s):\n%s", len(recipients), body)
        return
    if not all((settings.tenant_id, settings.client_id, settings.client_secret, settings.sender)):
        raise ValueError("Set AZURE_TENANT_ID, AZURE_CLIENT_ID, AZURE_CLIENT_SECRET, and GRAPH_SENDER before sending")

    mailer = GraphMailer(settings.tenant_id, settings.client_id, settings.client_secret, settings.sender)
    for recipient in recipients:
        if recipient.casefold() in {address.casefold() for address in already_sent}:
            continue
        mailer.send(recipient, subject, body)
        already_sent.add(recipient)
        sent_state[sent_key] = sorted(already_sent, key=str.casefold)
        settings.state_file.parent.mkdir(parents=True, exist_ok=True)
        settings.state_file.write_text(json.dumps(sent_state, indent=2) + "\n", encoding="utf-8")
        logger.info("Sent celebration notice to %s", recipient)