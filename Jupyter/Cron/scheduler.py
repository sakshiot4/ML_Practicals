import schedule
import time
from cron_eg import generate_sales_report  # import your function


def job():
    print("⏳ Running scheduled job...")
    generate_sales_report()


# Run every day at 12:58
schedule.every().day.at("13:07").do(job)


if __name__ == "__main__":
    print("🟢 Scheduler started...")

    while True:
        schedule.run_pending()
        time.sleep(1)