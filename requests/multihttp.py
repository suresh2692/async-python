import timeit
import asyncio
import aiohttp

URL = 'https://httpbin.org/uuid'

def timer(number, repeat):
    def wrapper(func):
        runs = timeit.repeat(func, number=number, repeat=repeat)
        print(sum(runs) / len(runs))

    return wrapper

async def fetch(session, url):
    async with session.get(url) as response:
        json_response = await response.json()
        print(json_response['uuid'])
        return json_response['uuid']


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, URL) for _ in range(10)]
        response = await asyncio.gather(*tasks)
        return response
        


@timer(1, 5)
def func():
    asyncio.run(main())
    