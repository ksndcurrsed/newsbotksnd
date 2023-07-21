from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime

cnt = 0
dt = datetime.datetime.today()
def newss(cnt):

    url = 'https://habr.com/ru/news/'
    page = urlopen(url)
    Soup = BeautifulSoup(page, 'lxml')
    news = Soup.find_all('a', class_='tm-title__link')
    filtrednews = []
    answtg = ''

    for data in news:
        if data.find('a', class_='tm-tetle__link') is None:
            filtrednews.append(data.text)

    for data in filtrednews:
        answtg += data + '\n ' + '\n'
        cnt += 1
        if cnt == 5:
            break

    return answtg

def bestnews(cnt):

    url2 = 'https://habr.com/ru/news/top/daily/'
    page2 = urlopen(url2)
    Soup2 = BeautifulSoup(page2, 'lxml')
    news2 = Soup2.find_all('a', class_='tm-title__link')
    filtrednews2 = []
    answtg2 = ''

    for data in news2:
        if data.find('a', class_='tm-tetle__link') is None:
            filtrednews2.append(data.text)

    for data in filtrednews2:
        answtg2 += data + '\n ' + '\n'
        cnt += 1
        if cnt == 5:
            break
    return answtg2