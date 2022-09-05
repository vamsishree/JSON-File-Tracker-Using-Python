import asyncio
async def connect_client():
    reader,writer = await asyncio.open_connection("127.0.0.1",8088)
    while True:
        inp = await reader.read(100000)
        message = str(inp.decode())
        print(message)
        
asyncio.run(connect_client())
