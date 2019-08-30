from multiprocessing import Process
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from .models import *
import datetime
import time
import random


def make_bypass_fog(m=1):
    names = locals()
    processes = []
    for n in range(0, m):
        names['t' + str(n)] = Process(target=bypass_fog, args=(n,))
        processes.append(names['t' + str(n)])
    for t in processes:
        t.start()
    for t in processes:
        t.join()


def bypass_fog(n=0):
    home_link = 'http://fearofgod.com'
    print('start%s' % n)
    item_link = Item.objects.filter(item_site="Fog").first().item_url
    sku = ['XS', 'S', 'M', 'L']
    bp_object = Bypass.objects.filter(bot_type="Fog")
    bp_object.update(created=datetime.datetime.now())

    fog_option = webdriver.ChromeOptions()
    fog_option.add_argument('--user-data-dir=C:\\Program Files (x86)\\Google\\Chrome\\Application\\%s' % n)
    fog_option.add_argument('blink-settings=imagesEnabled=false')
    fog_option.add_argument('--disable-gpu')
    # fog_option.add_argument('--headless')

    fog_browser = webdriver.Chrome(options=fog_option)
    fog_browser.get(item_link)

    print('浏览器已启动-%s' % n)

    WebDriverWait(fog_browser, 20, 0.2).until(lambda x: x.find_element_by_xpath("//a[contains(text(),'Social')]"))
    if fog_browser.find_element_by_xpath("//a[contains(text(),'Account')]"):
        print("已登录")
        WebDriverWait(fog_browser, 20, 0.2).until(lambda x: x.
                                                  find_element_by_xpath("//select[@id='ProductSelect']"))
        print("商品已加载")
        s = fog_browser.find_element_by_xpath("//select[@id='ProductSelect']")
        print("点击1")
        Select(s).select_by_value('29220836999229')
        print(fog_browser.current_url)

        time.sleep(10)
        # print('商品已加车-%s' % n)
        #
        # WebDriverWait(fog_browser, 20, 0.2).until(lambda x: x.find_element_by_xpath("//input[@name='checkout']"))
        # fog_browser.get('https://yeezysupply.com/cart/checkout.js')
        #
        # print('前往结账，正在获取KEY...%s' % n)
        #
        # fog_browser.get('https://yeezysupply.com/cart/clear.js')
        #
        # print('购物车已清空-%s' % n)
        #
        # fog_browser.get('https://yeezysupply.com/')
        #
        # print('已回到首页-%s' % n)
        #
        # fog_browser.quit()