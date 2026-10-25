# Birthday and Work Anniversary Notifier

A Python agent that reads employee dates and notification recipients from Excel, then sends a private email to each recipient when there are celebrations for the day. APScheduler runs the check daily; Microsoft Graph sends mail using Microsoft Entra client-credentials OAuth.

## Workbook layout

The default employee workbook is `data/WorkAnniversary_BirthdayReminderAgent.xlsx`. Its first row must contain `Name`, `Birthday`, and `Hire Date` columns. Use Excel date cells where possible; ISO (`YYYY-MM-DD`) and numeric month/day strings are also accepted. Birthday and hire date can be blank. The work-anniversary date is derived from the hire date, and only completed years are announced.

The default recipient workbook is `data/WorkAnniversary_BirthdayReminderAgent_EmailList.xlsx`. Its first row must contain an `Email` column. Each following row is emailed separately, so recipients do not see one another's addresses.

Sheet names and column labels are configurable in `.env`. Copy both workbooks into `data/`, or set `EVENTS_WORKBOOK` and `RECIPIENTS_WORKBOOK` to their locations. The attached workbooks could not be inspected from the workspace, so adjust the sheet and column settings to match their actual headers.

## Setup

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

Update the workbook paths, worksheet names, column headers, timezone, and send time in `.env`. Keep `DRY_RUN=true` while checking the workbook and output. A dry run logs the message that would be sent and does not need Graph credentials.

## Microsoft Graph setup

Create a Microsoft Entra app registration for a confidential client and configure client-credentials authentication. Grant the Microsoft Graph **application** permission `Mail.Send`, then have an administrator grant tenant-wide consent. Set `AZURE_TENANT_ID`, `AZURE_CLIENT_ID`, and `AZURE_CLIENT_SECRET` in `.env`; set `GRAPH_SENDER` to the mailbox user principal name or ID from which notices should be sent. Follow organizational policy for secret storage and limit the sender mailbox's access as appropriate.

After testing in dry-run mode, set `DRY_RUN=false`. Do not commit `.env`, workbook data, or the notification state file.

## Run

Run a one-time check for today (or provide an explicit date):

```sh
python -m birthday_anniversary_agent --run-once
python -m birthday_anniversary_agent --run-once --date 2026-09-28
```

Start the daily scheduler:

```sh
python -m birthday_anniversary_agent
```

The scheduler uses `TIMEZONE` and `NOTIFICATION_TIME` (24-hour `HH:MM`). Keep the process running under an operating-system service/container scheduler in production. The JSON state file records successful per-recipient sends by date, so restarting the process does not resend already completed deliveries for that day. Store that file on persistent storage if the process is containerized.

## Test

```sh
python -m pytest
```

February 29 birthdays match only on February 29; they are not shifted to another day in non-leap years.