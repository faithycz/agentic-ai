import asyncio
from common.utils import setup
from async_runner import write_sales_emails, send_best_email

async def main():
    setup()

    message = "Write a cold sales email"

    emails = await write_sales_emails(message)

    response = await send_best_email(emails)

    print(f"Final response:\n{response}")

if __name__ == "__main__":
    asyncio.run(main())