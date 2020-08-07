import scrapy
class ExampleSpider(scrapy.Spider):
    name = "DA12"
    start_urls = ["https://zingnews.vn/10-ngoi-sao-giai-nghe-sau-mua-201920-post1114840.html"]
    unique_page = set(['https://zingnews.vn/10-ngoi-sao-giai-nghe-sau-mua-201920-post1114840.html'])

    def parse(self, response):

        f = open('newsReports.txt','a+',encoding="utf-8")
        title = response.css('h1.the-article-title::text').get()
        f.write('===' + title + '\n')

        '''img_srcs = response.css('td.pic img::attr(src)').extract()
        for img_src in img_srcs:
            f.write(img_src + '\n')
        author_name = response.css('li.the-article-publish::text').get()
        f.write(author_name + '\n')
        category = response.css('p.the-article-category a::attr(title)').getall()
        for i in category:
            f.write(i + ' ')'''
        p_body = response.css('td.pCaption.caption p::text').getall()
        for i in p_body:
            f.write(i + '\n')

        '''next_links = response.css('article.article-item.type-text p.article-thumbnail a::attr(href)').getall()
        for link in next_links:
            if link and (link not in self.unique_page) and len(self.unique_page) <= 5:
                self.unique_page.add(link)
                yield scrapy.Request(
                    response.urljoin(link),
                    callback=self.parse)'''






