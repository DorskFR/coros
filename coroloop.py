import asyncio
import json
import time

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
        await asyncio.sleep(1)
        print("Apple: ", loop.__dict__["_default_executor"])
        print("Apple: ", loop.__dict__["_thread_id"])
        print("Apple: ", loop.__dict__["_selector"])
        print("Apple: ", loop.__dict__["_ssock"])
        print("Apple: ", loop.__dict__["_csock"])
        print("Apple: ", loop.__dict__["_transports"])


class Banana:
    def __init__(self):
        loop2 = asyncio.get_running_loop()
        loop2.create_task(self.talk())

    async def talk(self):
        await asyncio.sleep(1)
        print("Banana: ", loop.__dict__["_default_executor"])
        print("Banana: ", loop.__dict__["_thread_id"])
        print("Banana: ", loop.__dict__["_selector"])
        print("Banana: ", loop.__dict__["_ssock"])
        print("Banana: ", loop.__dict__["_csock"])
        print("Banana: ", loop.__dict__["_transports"])


class Orange:
    def __init__(self):
        loop.run_in_executor(None, self.talk)

    def talk(self):
        time.sleep(1)
        print("Orange: ", loop.__dict__["_default_executor"])
        print("Orange: ", loop.__dict__["_thread_id"])
        print("Orange: ", loop.__dict__["_selector"])
        print("Orange: ", loop.__dict__["_ssock"])
        print("Orange: ", loop.__dict__["_csock"])
        print("Orange: ", loop.__dict__["_transports"])


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
