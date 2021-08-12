import asyncio
from mandarine import Mandarine


class Banana:
    def __init__(self):
        self.mandarine = Mandarine()
        self.loop = asyncio.get_running_loop()
        self.loop.create_task(self.talk())

    async def talk(self):
        while True:
            await asyncio.sleep(1)
            print("Banana: ", self.loop.__dict__["_default_executor"])
            print("Banana: ", self.loop.__dict__["_thread_id"])
            print("Banana: ", self.loop.__dict__["_selector"])
            print("Banana: ", self.loop.__dict__["_ssock"])
            print("Banana: ", self.loop.__dict__["_csock"])
            print("Banana: ", self.loop.__dict__["_transports"])