import scrapy

class ShoeSpider(scrapy.Spider):
    name = "nike"

    def start_requests(self):

        urls = [
            'http://store.nike.com/ca/en_gb/pw/mens-running-shoes/7puZ8yzZoi3',
            ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        productWall = response.css("div.exp-product-wall")[0]
        for gridItem in productWall.css("div.grid-item"):
            yield { 
                'shoeName': gridItem.css("p.product-display-name::text").extract(),
                'price': gridItem.css("div.prices span.local::text").extract()[0]
            }
            
