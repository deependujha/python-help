import asyncio

async def main():
    print("main func")
    await asyncio.sleep(1)
    print('hello')

asyncio.run(main())