
import time
import redis
import requests
from BeautifulSoup import BeautifulSoup

r = redis.Redis(host='localhost', port=6379, db=1)

while True:
    item = r.rpop('content')
    if item != None:
        # print(item)
        soup = BeautifulSoup(item)

        for a in soup.findAll('a', href=True):
            print a['href']

    else:
        time.sleep(1)
