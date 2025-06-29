import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = [
        'https://example.com/1',
        'https://example.com/2',
        'https://example.com/3'
    ]
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

if __name__ == '__main__':
    asyncio.run(main())
