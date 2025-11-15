"""Creates background tasks and awaits their completion."""
import asyncio


async def worker(identifier: int) -> None:
    await asyncio.sleep(0.1 * identifier)
    print(f"Worker {identifier} done")


async def main() -> None:
    tasks = [asyncio.create_task(worker(i)) for i in range(1, 4)]
    for task in tasks:
        await task


if __name__ == "__main__":
    asyncio.run(main())
