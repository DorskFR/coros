import asyncio
from aiohttp import ClientSession


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


class Apple:
    def __init__(self):
        loop.create_task(self.talk())

    async def talk(self):
        while True:
            print("an apple a day keeps the doctor away...")
            await asyncio.sleep(1)


class Banana:
    def __init__(self):
        loop.create_task(self.talk())

    async def talk(self):
        while True:
            print("bananas exist in yellow, green, orange...")
            await asyncio.sleep(1)


class Kiwi:
    def __init__(self):
        loop.create_task(self.talk())

    async def talk(self):
        while True:
            print("why do they still put stickers on kiwis?...")
            await asyncio.sleep(1)


class Melon:
    def __init__(self):
        loop.create_task(self.talk())

    async def talk(self):
        while True:
            print("melons and watermelons... is there no water in the melon?...")
            await asyncio.sleep(1)


import time


class Orange:
    def __init__(self):
        loop.run_in_executor(None, self.talk)

    def talk(self):
        for i in range(0, 10):
            print("oranges for christmas, oranges in prison...")
            time.sleep(3)


async def main():
    apple = Apple()
    banana = Banana()
    kiwi = Kiwi()
    melon = Melon()
    orange = Orange()

    # this will block
    # await apple.talk()
    # await banana.talk()
    # await kiwi.talk()
    # await melon.talk()
    # await orange.talk()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.create_task(main())
        loop.run_forever()
    finally:
        loop.close()