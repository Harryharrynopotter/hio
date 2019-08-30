from .models import *
import os


def mass_url(url: str, n):
    for i in range(0, n):
        browser = "Google%s" % i
        os.putenv("browser", browser)
        os.putenv("url", url)
        os.system('C:\\Users\\Harry\\PycharmProjects\\yeezysupply\\bat\\openURL.bat')


