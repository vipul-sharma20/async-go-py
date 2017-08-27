import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        for i in range(1000):
            await session.get('http://example.com')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
