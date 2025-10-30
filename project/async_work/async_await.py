import asyncio
import time
#
# def generator():
#     n = 1
#     while True:
#         yield n
#         n += 1
#
# def generator2():
#     n = 1000
#     while True:
#         yield n
#         n += 1
#
# gen = generator()
# gen2 = generator2()
# print(gen)
#
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen2))
# print(next(gen))
# print(5555555555555555555555555555)
# print(next(gen))
from time import sleep

# 1111111111111111
# async def hello():
#     print("Hello world")
#     await asyncio.sleep(2)
#     print('Hello again')
#
#
# asyncio.run(hello())


# 22222222222222222222222

async def hello():
    print("Hello world")
    await asyncio.sleep(2)
    print('Hello again')


async def foo(n):
    print(f"Foooooo {n}")
    # sleep(n)
    await asyncio.sleep(n)
    print(f'Foooooooooo again {n}')


async def main():
    await asyncio.gather(
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
        foo(5), hello(), hello(), hello(), foo(2),
    )

start = time.monotonic()
print(start)

asyncio.run(main())

end = time.monotonic()
print(end)
print(__file__, end-start)