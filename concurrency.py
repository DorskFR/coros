import asyncio
from banana import Banana
from apple import Apple
from orange import Orange
import time

SLEEP_SYNC = 10
SLEEP_ASYNC = 1
DEBUG = False

'''
parents
'''

class Apple:
    def __init__(self):
        self.mandarine = Mandarine()
        self.loop = asyncio.get_running_loop()
        self.loop.run_in_executor(None, self.talk)

    def talk(self):
        while True:
            time.sleep(SLEEP_SYNC)
            print("Apple (Sync): ", self.loop.__dict__["_default_executor"])
            if DEBUG:
                print("Apple (Sync): ", self.loop.__dict__["_thread_id"])
                print("Apple (Sync): ", self.loop.__dict__["_selector"])
                print("Apple (Sync): ", self.loop.__dict__["_ssock"])
                print("Apple (Sync): ", self.loop.__dict__["_csock"])
                print("Apple (Sync): ", self.loop.__dict__["_transports"])

class Banana:
    def __init__(self):
        self.mandarine = Mandarine()
        self.loop = asyncio.get_running_loop()
        self.loop.create_task(self.talk())

    async def talk(self):
        while True:
            await asyncio.sleep(SLEEP_ASYNC)
            print("Banana (Async): ", self.loop.__dict__["_default_executor"])
            if DEBUG:
                print("Banana (Async): ", self.loop.__dict__["_thread_id"])
                print("Banana (Async): ", self.loop.__dict__["_selector"])
                print("Banana (Async): ", self.loop.__dict__["_ssock"])
                print("Banana (Async): ", self.loop.__dict__["_csock"])
                print("Banana (Async): ", self.loop.__dict__["_transports"])

class Kiwi:
    def __init__(self):
        self.strawberry = Strawberry()
        self.loop = asyncio.get_running_loop()
        self.loop.create_task(self.talk())

    async def talk(self):
        while True:
            await asyncio.sleep(SLEEP_ASYNC)
            print("Kiwi (Async): ", self.loop.__dict__["_default_executor"])
            if DEBUG:
                print("Kiwi (Async): ", self.loop.__dict__["_thread_id"])
                print("Kiwi (Async): ", self.loop.__dict__["_selector"])
                print("Kiwi (Async): ", self.loop.__dict__["_ssock"])
                print("Kiwi (Async): ", self.loop.__dict__["_csock"])
                print("Kiwi (Async): ", self.loop.__dict__["_transports"])

class Orange:
    def __init__(self):
        self.strawberry = Strawberry()
        self.loop = asyncio.get_running_loop()
        self.loop.run_in_executor(None, self.talk)

    def talk(self):
        while True:
            time.sleep(SLEEP_SYNC)
            print("Orange (Sync): ", self.loop.__dict__["_default_executor"])
            if DEBUG:
                print("Orange (Sync): ", self.loop.__dict__["_thread_id"])
                print("Orange (Sync): ", self.loop.__dict__["_selector"])
                print("Orange (Sync): ", self.loop.__dict__["_ssock"])
                print("Orange (Sync): ", self.loop.__dict__["_csock"])
                print("Orange (Sync): ", self.loop.__dict__["_transports"])

'''
children
'''

class Mandarine:
    def __init__(self):
        self.loop = asyncio.get_running_loop()
        self.loop.run_in_executor(None, self.talk)

    def talk(self):
        while True:
            time.sleep(SLEEP_SYNC)
            print("Mandarine (Sync): ", self.loop.__dict__["_default_executor"])
            if DEBUG:
                    print("Mandarine (Sync): ", self.loop.__dict__["_thread_id"])
                    print("Mandarine (Sync): ", self.loop.__dict__["_selector"])
                    print("Mandarine (Sync): ", self.loop.__dict__["_ssock"])
                    print("Mandarine (Sync): ", self.loop.__dict__["_csock"])
                    print("Mandarine (Sync): ", self.loop.__dict__["_transports"])


class Strawberry:
    def __init__(self):
        self.loop = asyncio.get_running_loop()
        self.loop.create_task(self.talk())

    async def talk(self):
        while True:
            await asyncio.sleep(SLEEP_ASYNC)
            print("Strawberry (Async): ", self.loop.__dict__["_default_executor"])
            if DEBUG:
                print("Strawberry (Async): ", self.loop.__dict__["_thread_id"])
                print("Strawberry (Async): ", self.loop.__dict__["_selector"])
                print("Strawberry (Async): ", self.loop.__dict__["_ssock"])
                print("Strawberry (Async): ", self.loop.__dict__["_csock"])
                print("Strawberry (Async): ", self.loop.__dict__["_transports"])




async def main():
    apple = Apple() # Apple executes SYNC code + creates a child Mandarine which runs SYNC code
    banana = Banana() # Banana executes ASYNC code + creates a child Mandarine which runs SYNC code
    kiwi = Kiwi() # Kiwi executes ASYNC code + creates a child Strawberry which runs ASYNC code
    orange = Orange() # Orange executes SYNC code + creates a child Strawberry which runs ASYNC code
 

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.create_task(main())
        loop.run_forever()
    finally:
        loop.close()
