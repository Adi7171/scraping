# First execute this file and then you will get a json file then after you get the json file go tto p.py to convert it so that you can get an excel sheet


import scrapy
import json


class NberSpider(scrapy.Spider):
    name = 'nber'
    start_urls = ['https://www.nber.org/nber-news/nber-research-news?page=1&perPage=50']
    
    def start_requests(self):
        url='https://www.nber.org/api/v1/in_the_news/contentType/news_reference/_/_/search?page=1&perPage=50'
        headers= {
        "content-type": "application/json",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-IN,en;q=0.9",
        "referer": "https://www.nber.org/nber-news/nber-research-news?page=1&perPage=50",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36"
        }
        yield scrapy.http.Request(url, headers=headers)


    def parse(self, response):
      parsedJson = json.loads(response.body)
      yield {
            'title': parsedJson['source']['title'],
            'url':parsedJson['source']['url'],
            'summary':parsedJson['title']
      }
