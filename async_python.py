import asyncio

import requests


async def main():
    futures = [
        loop.run_in_executor(
            None,
            requests.get,
            'http://example.com'
        )
        for i in range(1000)
    ]
    for response in await asyncio.gather(*futures):
        pass


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
