import requests
import time

while True:
    response = requests.get('https://dummyjson.com/products/1')
    print(response.json())
    time.sleep(5)
