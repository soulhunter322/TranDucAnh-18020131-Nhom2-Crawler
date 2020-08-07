import scrapy
import json


class ThanhnienSpider(scrapy.Spider):
    name = 'abe'
    allowed_domains = ['laodong.vn']
    #path_page_bm = 'https://vietnamnet.vn/vn/giai-tri/the-gioi-sao/-'
    start_urls = ['https://laodong.vn/thoi-su/thu-tuong-tang-cuong-lien-ket-vung-di-dau-trong-phat-trien-kinh-te-so-825152.ldo']
    unique_page = set(['https://laodong.vn/thoi-su/thu-tuong-tang-cuong-lien-ket-vung-di-dau-trong-phat-trien-kinh-te-so-825152.ldo'])
    #start_page_id = 663355
    '''for i in range(1,10000):
        path_page_i = path_page_bm + str(start_page_id + i) + '.html'
        start_urls.append(path_page_i)'''

    def parse(self, response):
            f = open('T1.txt','a',encoding='utf-8')
        #if response.status == 200 and response.css('meta[property="og:site_name"]::attr("content")').get() == 'VietNamNet':
            data = {
                'link': response.url,
                'title':response.css('h1::text').get(),
                'description':response.css('p.abs::text').get(),
                'content': '\n'.join([
                    ''.join(c.css('*::text').getall())
                    for c in response.css('div.article-content > p')]),
                'tags':response.css('span.keywords a::text').getall(),
                'keywords': [
                        k.strip() for k in response.css('meta[name="keywords"]::attr("content")').get().split(',')
                ]
            }
            f.write(json.dumps(data, ensure_ascii=False))
            f.write('\n')
            next_links = response.css('article.article-small.N2 a::attr(href)').getall()
            for link in next_links:
                if link and (link not in self.unique_page) and len(self.unique_page) <= 10000:
                    self.unique_page.add(link)
                    yield scrapy.Request(
                        response.urljoin(link),
                        callback=self.parse)


