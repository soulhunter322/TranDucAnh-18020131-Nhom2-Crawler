import scrapy
class ExampleSpider(scrapy.Spider):
    name = "DA"
    allowed_domains = ['https://zingnews.vn']
    start_urls = ["https://zingnews.vn/mazda-bat-ngo-he-lo-dong-xe-cx-50-moi-post1112597.html"]


    def parse(self, response):
        f = open('hihihi.txt','w+',encoding="utf-8")
        title = response.css('h1.the-article-title::text').get()
        f.write(title + '\n')
        next_links = []
        for href in response.css('article.article-item.type-text p.article-thumbnail a::attr(href)'):
            alo = href.get()
            next_links.append(alo)
        for link in next_links:
            f.write(i)







