import asyncio
import time


class Mandarine:
    def __init__(self):
        self.loop = asyncio.get_running_loop()
        self.loop.run_in_executor(None, self.talk)

    def talk(self):
        while True:
            time.sleep(1)
            print("Mandarine: ", self.loop.__dict__["_default_executor"])
            print("Mandarine: ", self.loop.__dict__["_thread_id"])
            print("Mandarine: ", self.loop.__dict__["_selector"])
            print("Mandarine: ", self.loop.__dict__["_ssock"])
            print("Mandarine: ", self.loop.__dict__["_csock"])
            print("Mandarine: ", self.loop.__dict__["_transports"])