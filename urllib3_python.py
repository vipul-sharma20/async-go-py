import asyncio
import urllib3


async def main(http):
    futures = [
        loop.run_in_executor(
            None,
            http.request('GET', 'http://example.com')
        )
        for i in range(1000)
    ]
    return await asyncio.gather(*futures)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    http = urllib3.PoolManager()
    _ = loop.run_until_complete(main(http))
