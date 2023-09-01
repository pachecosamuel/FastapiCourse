from time import sleep
import asyncio

class SpongeBob:
    async def cook_bread(self):
        await asyncio.sleep(2)
        
    async def cook_meat(self):
        await asyncio.sleep(2)
        
    async def mount_sandwich(self):
        await asyncio.sleep(2)
        
    async def make_milkshake(self):
        await asyncio.sleep(2)
        
    async def make_sandwich(self):
        await asyncio.gather(
            self.mount_sandwich(),
            self.make_milkshake()
        )
        event_loop = asyncio.get_running_loop()
        event_loop.create_task(self.mount_sandwich())
        
    async def cook_all(self):
        await asyncio.gather(self.make_sandwich(), self.mount_sandwich())
        

async_bob = SpongeBob()
asyncio.run(async_bob.cook_all())