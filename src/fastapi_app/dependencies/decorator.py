# Retry decorator
from asyncio import sleep
from functools import wraps


def retry(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        for i in range(3):  # Retry up to 3 times
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                print("*args:", *args, "**kwargs:", **kwargs)
                print(f"\nAn error occurred: {e}. Retrying...")
                await sleep(0.01)  # Wait for 0.01 seconds before retrying
        print("Failed after 3 retries.")

    return wrapper
