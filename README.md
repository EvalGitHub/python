基础知识普及：
========================
let us see an example :

 方式一：start_urls + parse 
 ------------------------------  
 ## [如果我们没有写start_urls,以及回调parse，他会默认爬去start_urls的url,执行parse,]
    import scrapy
    class mySpider(scrapy.Spider):
    name = "sp"
    allowed_domains=['example.com']
    start_urls=[
        'http://www.example.com/1.html',
        'http://www.example.com/2.html',
        'http://www.example.com/3.html',
    ]
    def parse(self,response):
       for href in response.css('.author + a::attr(href)'):
          yield response.follow(href,self.parse_author)
          ......
          
          
  方式二：直接使用start_requests
    ------------------------------  
    import scrapy
    class mySpider(scrapy.Spider):
    name = "sp"
    allowed_domains=['example.com']
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
     def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open("url.txt", 'a') as f:
            f.write(page)
