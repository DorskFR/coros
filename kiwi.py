import asyncio


class Kiwi:
    def __init__(self):
        self.loop = asyncio.get_running_loop()
        self.loop.create_task(self.talk())

    async def talk(self):
        while True:
            await asyncio.sleep(1)
            print("Kiwi: ", self.loop.__dict__["_default_executor"])
            print("Kiwi: ", self.loop.__dict__["_thread_id"])
            print("Kiwi: ", self.loop.__dict__["_selector"])
            print("Kiwi: ", self.loop.__dict__["_ssock"])
            print("Kiwi: ", self.loop.__dict__["_csock"])
            print("Kiwi: ", self.loop.__dict__["_transports"])