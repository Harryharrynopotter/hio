import scrapy
import json
from scrapy.http import Request
from urllib import parse
from fog_bot.items import FogBotItem


class FogItemSpider(scrapy.Spider):
    name = 'toutiao'

    def start_requests(self):
        query_string = {
            "offset": "0",
            "format": "json",
            "keyword": "甘肃",
            "autoload": "true",
            "count": "20",
            "cur_tab": "1",
            "from": "search_tab",
            "pd": "synthesis"
        }
        qs = parse.urlencode(query_string)
        url = 'https://www.toutiao.com/search_content/?' + qs
        url = "https://lf.snssdk.com/api/search/content/?" + qs
        yield Request(url=url, callback=self.parse_init_data)

    def parse_init_data(self, response):
        res = json.loads(response.text)['data']
        item = ToutiaoSpiderItem()
        for i in res:
            item['title'] = i['display']['lemmaTitle']
            item['description'] = i['display']['picAbs']
