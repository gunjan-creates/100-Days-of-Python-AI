"""Runs coroutines concurrently using asyncio.gather."""
import asyncio


async def fetch_data(delay: float, name: str) -> str:
    await asyncio.sleep(delay)
    return f"{name} finished"


async def main() -> None:
    results = await asyncio.gather(
        fetch_data(0.5, "task-one"), fetch_data(0.2, "task-two"), fetch_data(0.3, "task-three")
    )
    for result in results:
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
