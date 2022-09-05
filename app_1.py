import asyncio
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import json

async def changes(reader,writer):
    text = ""
    address = writer.get_extra_info('peername')
    print(f"\n{address} is connected.")
    with open('data.json','r') as r:
        data = json.load(r)
    data = data['access_points']
    print("Please make the changes now to JSON file and enter CHANGES MADE")
    a = input()
    if a == "CHANGES MADE":
        with open('data.json','r') as r:
            recorded_data = json.load(r)
        recorded_data = recorded_data['access_points']
        if data == recorded_data:
            text = text + "NO CHANGES WERE MADE\n"
        if data != recorded_data:
            print("CHANGES MADE- GETTING THE CHANGES")

            for i in range(len(recorded_data)):
                x = recorded_data[i]['ssid']
                if x in str(data):
                    pass
                else:
                    text = text + f"{x} added to the list with SNR {recorded_data[i]['snr']} and Channel {recorded_data[i]['channel']}\n"

            for i in range(len(data)):
                x = data[i]['ssid']
                if x not in str(recorded_data):
                    text = text + f"{x} removed from the list\n"
                else:
                    pass
            
            for i in recorded_data:
                for x in range(len(data)):
                            if data[x]['ssid'] == i['ssid']:
                                y = x
                if i in data:
                    pass
                elif i not in data:
                    if i['snr'] not in data and i['channel'] not in data:
                        if data[y]['snr'] != i['snr']:
                            if i['ssid'] in str(data):
                                text = text + f"{i['ssid']}'s SNR has changed from {data[y]['snr']} to {i['snr']}\n"
                    
                        if data[y]['channel'] != i['channel']:
                            if i['ssid'] in str(data):
                                text = text + f"{i['ssid']}'s channel has changed from {data[y]['channel']} to {i['channel']}\n"
                            
    writer.write(str(text).encode())                
                    



async def main():
    """ This function initiates a server and establishes connection between app_1 and app_2."""
    server = await asyncio.start_server(changes,'127.0.0.1',8088)
    addr = server.sockets[0].getsockname()
    print(f"started on {addr}")
    async with server:
        await server.serve_forever()

asyncio.run(main())