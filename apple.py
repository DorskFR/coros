import asyncio
from kiwi import Kiwi


class Apple:
    def __init__(self):
        self.kiwi = Kiwi()
        self.loop = asyncio.get_running_loop()
        self.loop.create_task(self.talk())

    async def talk(self):
        while True:
            await asyncio.sleep(1)
            print("Apple: ", self.loop.__dict__["_default_executor"])
            print("Apple: ", self.loop.__dict__["_thread_id"])
            print("Apple: ", self.loop.__dict__["_selector"])
            print("Apple: ", self.loop.__dict__["_ssock"])
            print("Apple: ", self.loop.__dict__["_csock"])
            print("Apple: ", self.loop.__dict__["_transports"])