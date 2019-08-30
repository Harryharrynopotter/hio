from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import urlparse
import requests
import sys
import time
import lxml
from multiprocessing import Process
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from .models import *
import datetime
import time
import random


def atc_driver(url):
    names = locals()

    processes = []
    m = FogBot.objects.count()
    for n in range(0, m):
        names['t' + str(n)] = Process(target=atc_web_driver, args=(url, n,))
        processes.append(names['t' + str(n)])
    for t in processes:
        t.start()
    for t in processes:
        t.join()


def atc_web_driver(url, n=0):
    print('start%s' % n)
    item_link = get_atc(url)
    # sku = ['XS', 'S', 'M', 'L']
    bp_object = Bypass.objects.filter(bot_type="Fog")
    bp_object.update(created=datetime.datetime.now())

    fog_option = webdriver.ChromeOptions()
    fog_option.add_argument('--user-data-dir=C:\\Program Files (x86)\\Google\\Chrome\\Application\\%s' % n)
    # proxy_source = Proxies.objects.filter(proxy_id=n+1).get()
    # proxy = str(proxy_source.proxy_ip) + ':' + str(proxy_source.proxy_port)
    # print(proxy)
    fog_option.add_argument('--proxy-server=http://us-static-chicago.resdleafproxies.com:20366')
    # fog_option.add_argument('blink-settings=imagesEnabled=false')
    # fog_option.add_argument('--disable-gpu')

    fog_browser = webdriver.Chrome(options=fog_option)
    fog_browser.get(item_link)

    time.sleep(1800)


def get_atc(url):
    getURL(url)
    getSoup()
    getItem()
    getSize()
    getStock()
    getPrice()
    getVariants()
    getTotal()
    formatData()
    print(ATC())
    return ATC()


# def getTime():
#     return time.strftime('|%D | %H:%M:%S|')


def getURL(url):
    global r
    global soup
    global URL

    URL = url


def getSoup():
    global soup
    s = requests.Session()
    r = s.get(URL + '.xml')
    soup = BeautifulSoup(r.text, 'lxml')
    return soup

# def getImg():
#     global get
#     img = soup.find_all()

def getItem():
    global item
    item = soup.find('title').text


def getSize():
    global sz
    sz = list()
    for size in soup.find_all('title')[1:]:
        sz.append(size.get_text())
    return sz


def getStock():
    global stk
    stk = list()
    for stock in soup.find_all('inventory-quantity'):
        stk.append(stock.get_text())
    return stk


def getPrice():
    global prc
    prc = list()
    for price in soup.find_all('price'):
        prc.append(price.get_text())
    return prc


def getVariants():
    global vrnt
    vrnt = list()
    for variants in soup.find_all('product-id'):
        vrnt.append(variants.find_previous('id').get_text())
    return vrnt


def getTotal():
    global ttl
    ttl = list()
    for stocktotal in soup.findAll("inventory-quantity"):
        ttl.append(int(stocktotal.text))
    return ttl


def formatData():
    print('')
    print(item)
    if len(stk) > 0:
        print('{:<5} | {:<20} | {:<10} | {:10} | {:20} '.format('', 'size', 'stock', 'price', 'variants'))
        for i, (size, stock, price, variant) in enumerate(zip(sz, stk, prc, vrnt)):
            print('{:<5} | {:<20} | {:<10} | {:10} | {:20} '.format(i, size, stock, '$' + price, variant))
        if sum(ttl) == 0:
            print('Sold out!')
        elif sum(ttl) != 0:
            print('Total stock: {:<5}'.format(sum(ttl)))
    else:
        print('Stock could not be found :(')
        print('{:<5} | {:<20} | {:10} | {:20} '.format('', 'size', 'price', 'variants'))
        for i, (size, price, variant) in enumerate(zip(sz, prc, vrnt)):
            print('{:<5} | {:<20} | {:10} | {:20} '.format(i, size, '$' + price, variant))


def ATC():
    # print('')
    # choice = input('Would you like to buy this item? (y/n) ')
    # while (choice != 'y1') and (choice != 'n1'):
    #     if choice == 'y':
    print(sz)
    size = random.sample(sz, 1)
    print("atc sizes = %s" % size)
    quantity = '1'

    variant = soup.find(text=size).findPrevious('id').text

    url = urlparse(URL)
    baseurl = 'https://' + url.netloc + '/cart/'
    BD = baseurl + variant + ':' + quantity
    return BD
    # driver = webdriver.Chrome()
#     driver.get(BD)
#     [getURL(), getSoup(), getItem(), getSize(), getStock(), getPrice(), getVariants(), getTotal(),
#      formatData(), ATC()]
# # elif choice == 'n':
#     choice1 = input('Would you like to search for another product? (y/n) ')
#     while (choice1 != 'yo') and (choice1 != 'no'):
#         if choice1 == 'y':
#             [getURL(), getSoup(), getItem(), getSize(), getStock(), getPrice(), getVariants(), getTotal(),
#              formatData(), ATC()]
#         else:
#             print('Ok, closing shopify stock checker')
#             sys.exit()

