import websocket
from datetime import datetime
import json

SUM_PRICE_VOLUME = 0
SUM_VOLUME = 0
new_list = []


def print_message(message):
    counter = 0
    for line in json.loads(message)['data']:
        counter += 1
        price = line['p']
        volume = line['v']
        vwap(price, volume)
        datetime_from_unix = datetime.utcfromtimestamp(line['t'] / 1000).strftime('%Y-%m-%d %H:%M:%S.%f')
        print(counter)
        print(datetime_from_unix, "price:", line['p'], "volume:", line['v'])


def vwap(p, v):
    global SUM_PRICE_VOLUME
    global SUM_VOLUME

    pv = (p * v)
    SUM_PRICE_VOLUME += pv
    SUM_VOLUME += v


def print_vwap():
    global SUM_PRICE_VOLUME
    global SUM_VOLUME

    print("Volume-weighted average price:", (SUM_PRICE_VOLUME / SUM_VOLUME))
    SUM_PRICE_VOLUME = 0
    SUM_VOLUME = 0


def on_message(ws, message):
    print_message(message)

    for data in json.loads(message)['data']:
        d = json.loads(message)['data']
        datetime_from_unix = datetime.utcfromtimestamp(data['t'] / 1000).strftime('%Y-%m-%d %H:%M:%S.%f')
        sec = str(datetime_from_unix[-9:-7])
        msec = int(datetime_from_unix[-6:])

        if sec == '59' and msec not in new_list:
            for dt in d:
                dt_from_unix = datetime.utcfromtimestamp(dt['t'] / 1000).strftime('%Y-%m-%d %H:%M:%S.%f')
                s = str(dt_from_unix[-9:-7])
                ms = int(dt_from_unix[-6:])
                if s == '59':
                    new_list.append(ms)

        if sec == '59' and s == '00' and msec == max(new_list):
            print_vwap()
            new_list.clear()

        if sec == '00' and s == '59' and msec == max(new_list):
            print_vwap()
            new_list.clear()
        if sec == '59':
            print_vwap()
            new_list.clear()


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')


if __name__ == "__main__":
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=ck25f7pr01qhd6ti4rc0ck25f7pr01qhd6ti4rcg",
                                on_message=on_message,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
