import asyncio
from aiohttp import ClientSession
from banana import Banana
from apple import Apple
from orange import Orange


class Caller:
    def __init__(self):
        super().__init__()

    async def get(self, url):
        async with ClientSession() as session:
            try:
                response = await session.get(url)
                data = await response.json()
                return data
            except Exception as e:
                print(e)


async def main():
    apple = Apple()
    banana = Banana()
    orange = Orange()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.create_task(main())
        loop.run_forever()
    finally:
        loop.close()
