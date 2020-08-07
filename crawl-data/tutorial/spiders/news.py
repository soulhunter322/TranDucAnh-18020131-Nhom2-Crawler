import scrapy

class QuotesSpider(scrapy.Spider):
    name = "news"
    start_urls = [
        'https://zingnews.vn'
    ]
    def parse(self, response):
        f = open('hiho.txt')
        l = response.css('p.article-title a::attr(href)').extract()
        f.write(l,'\n')