import asyncio
import time
from strawberry import Strawberry


class Orange:
    def __init__(self):
        self.strawberry = Strawberry()
        self.loop = asyncio.get_running_loop()
        self.loop.run_in_executor(None, self.talk)

    def talk(self):
        while True:
            time.sleep(1)
            print("Orange: ", self.loop.__dict__["_default_executor"])
            print("Orange: ", self.loop.__dict__["_thread_id"])
            print("Orange: ", self.loop.__dict__["_selector"])
            print("Orange: ", self.loop.__dict__["_ssock"])
            print("Orange: ", self.loop.__dict__["_csock"])
            print("Orange: ", self.loop.__dict__["_transports"])