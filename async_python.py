import asyncio

import requests


async def main():
    futures = [
        loop.run_in_executor(
            None,
            requests.get,
            'http://thecatapi.com/api/images/get?type=jpg'
        )
        for i in range(20)
    ]
    for response in await asyncio.gather(*futures):
        print(response)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

