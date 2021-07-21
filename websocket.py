import asyncio
import websockets

async def connect_to_Finage():
    uri = "YOUR_SERVER_ADDRESS"
    async with websockets.connect(uri) as websocket:
        symbol = input("Enter the currency symbol: ")

        query = '{"action": "subscribe", "symbols": "%s"}' % symbol

        await websocket.send(query)

        while True:
            response = await websocket.recv()
            print(f"< {response}")


asyncio.get_event_loop().run_until_complete(connect_to_Finage()) 
asyncio.get_event_loop().run_forever()