import argparse
import logging
from datetime import date, datetime
from zoneinfo import ZoneInfo

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

from .agent import Settings, run_for_date


def main() -> None:
    parser = argparse.ArgumentParser(description="Send birthday and work-anniversary reminders from Excel workbooks.")
    parser.add_argument("--run-once", action="store_true", help="Run immediately instead of starting the daily scheduler")
    parser.add_argument("--date", type=date.fromisoformat, help="Date to process with --run-once (YYYY-MM-DD); defaults to today")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")

    settings = Settings.from_environment()
    timezone = ZoneInfo(settings.timezone)
    if args.run_once:
        run_for_date(settings, args.date or datetime.now(timezone).date())
        return
    hour, minute = map(int, settings.notification_time.split(":"))
    scheduler = BlockingScheduler(timezone=timezone)

    def run_today() -> None:
        run_for_date(settings, datetime.now(timezone).date())

    scheduler.add_job(
        run_today,
        CronTrigger(hour=hour, minute=minute, timezone=timezone),
        id="daily-celebration-notices",
        coalesce=True,
        max_instances=1,
        misfire_grace_time=3600,
    )
    logging.getLogger(__name__).info(
        "Daily notifications scheduled for %02d:%02d (%s)", hour, minute, settings.timezone
    )
    scheduler.start()


if __name__ == "__main__":
    main()