import requests
import time


def send_request():
    response = requests.get('https://dummyjson.com/products/1')
    print(response.json())


if __name__ == '__main__':
    print('starting requests')
    while True:
        send_request()
        time.sleep(3)
