import asyncio

async def square(value: int):
    return value * value

async def print_square(value: int):
    result = await square(4)
    print(f'O resultado igual a {result}')

print_square(3)

#Event loop
event_loop = asyncio.new_event_loop()
event_loop.run_until_complete(print_square(3))