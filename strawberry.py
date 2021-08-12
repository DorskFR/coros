import asyncio


class Strawberry:
    def __init__(self):
        self.loop = asyncio.get_running_loop()
        self.loop.create_task(self.talk())

    async def talk(self):
        while True:
            await asyncio.sleep(1)
            print("Strawberry: ", self.loop.__dict__["_default_executor"])
            print("Strawberry: ", self.loop.__dict__["_thread_id"])
            print("Strawberry: ", self.loop.__dict__["_selector"])
            print("Strawberry: ", self.loop.__dict__["_ssock"])
            print("Strawberry: ", self.loop.__dict__["_csock"])
            print("Strawberry: ", self.loop.__dict__["_transports"])