from multiprocessing import Process
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from .models import *
import time
import datetime


def make_bypass(m=1):
    names = locals()
    processes = []
    for n in range(0, m):
        names['t' + str(n)] = Process(target=bypass_ys, args=(n,))
        processes.append(names['t' + str(n)])
    for t in processes:
        t.start()
    for t in processes:
        t.join()


def bypass_ys(n=0):
    home_link = 'http://yeezysupply.com'
    print('start%s' % n)
    item_link = Item.objects.first().item_url
    # sku = Item.objects.first().item_sku[0]
    bp_object = Bypass.objects.filter(browser_name="YS%s" % n, bot_type="YS")
    bp_object.update(browser_name="YS%s" % n)
    bp_object.update(created=datetime.datetime.now())

    test_option = webdriver.ChromeOptions()
    test_option.add_argument('--user-data-dir=C:\\Program Files (x86)\\Google\\Chrome\\Application\\%s' % n)
    test_option.add_argument('blink-settings=imagesEnabled=false')
    test_option.add_argument('--disable-gpu')
    # test_option.add_argument('--headless')
    test_option.add_argument('--proxy-server=static-us-private-pw-39.resdleafproxies.com:33128:InsykilC9La7:InsykilC9L')
    test_browser = webdriver.Chrome(options=test_option)
    test_browser.get(item_link)

    print('浏览器已启动-%s' % n)

    # test_browser.get_cookies()
    # test_browser.delete_all_cookies()
    #
    # print('缓存已清除-%s' % n)

    WebDriverWait(test_browser, 20, 0.2).until(lambda x: x.find_element_by_xpath("//select[@id='SIZE']"))
    test_browser.find_element_by_xpath("//select[@id='SIZE']").click()
    s = test_browser.find_element_by_id("SIZE")
    Select(s).select_by_visible_text('M')

    test_browser.find_element_by_xpath("//input[@name='add']").click()

    print('商品已加车-%s' % n)

    WebDriverWait(test_browser, 20, 0.2).until(lambda x: x.find_element_by_xpath("//input[@name='checkout']"))
    test_browser.get('https://yeezysupply.com/cart/checkout.js')
    print('前往结账，正在获取KEY...%s' % n)

    WebDriverWait(test_browser, 20, 0.2).until(lambda x: x.find_element_by_xpath("//span[@class='btn__content']"))
    url = test_browser.current_url
    url1 = url.split('checkouts/')
    url2 = url1[1].split('?')

    key = url2[0]
    bp_object.update(bypass_key=key)
    print('BYPASS已存储!%s' % n)

    test_browser.get('https://yeezysupply.com/cart/clear.js')

    # test_browser.get('https://yeezysupply.com/cart')
    # WebDriverWait(test_browser, 20, 0.2).until(lambda x: x.find_element_by_xpath("//a[@class='C__remove']"
    #                                                                              "//span[contains(text(),'×')]"))
    # test_browser.find_element_by_xpath("//a[@class='C__remove']//span[contains(text(),'×')]").click()
    print('购物车已清空-%s' % n)

    time.sleep(1)
    test_browser.quit()


