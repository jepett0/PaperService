import asyncio
import ijson
import aiofiles


async def iterate(json_file):
    f = await aiofiles.open(json_file, 'r')
    async for object in ijson.items(f, 'item'):
        print(object.keys())

asyncio.run(iterate('dblpv13.json'))        
