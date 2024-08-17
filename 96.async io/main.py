# import time
# import asyncio
# async def func1():
#     await asyncio.sleep(2)
#     print("hi")
#     return "hi"
# async def func2():
#     await asyncio.sleep(1)
#     print("hi")
#     return "hi"
# async def func3():
#     await asyncio.sleep(3)
#     print("hi")
#     return "hi"

# async def main():
#     L=await asyncio.gather(
#         func1(),
#         func2(),
#         func3(),
#     )
#     print(L)

# # asyncio.run(main())

import time
import asyncio

async def func1():
    await asyncio.sleep(2)
    print("hi1")
    return "hi"

async def func2():
    await asyncio.sleep(1)
    print("hi2")
    return "hi"

async def func3():
    await asyncio.sleep(3)
    print("hi3")
    return "hi"

async def main():
    L = await asyncio.gather(
        func1(),
        func2(),
        func3(),
    )
    print(L)
asyncio.run(main())
