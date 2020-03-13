import requests
from bs4 import BeautifulSoup
import time

def findmove(link):
    url = link
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    source = str(soup.findAll())
    index = source.find("lastMove")
    ruch = ""
    for a in range(index + 11, index + 15):
        ruch = ruch + str(source[a])
    return ruch

print("Podaj adres partii: ")
link = "https://lichess.org/" + input()

last = "abc"
while 1:
    new = findmove(link)
    if new != last:
        last = new
        print(last)
    time.sleep(0.1)