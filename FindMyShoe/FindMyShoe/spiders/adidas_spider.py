import scrapy

class ShoeSpider(scrapy.Spider):
    name = "adidas"

    def start_requests(self):

    	urls = [
    		'http://www.adidas.ca/en/men-ultra_boost',
            'http://www.adidas.ca/en/men-originals-nmd-shoes'
            ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        productGrid = response.css("div.product-grid-area")[0]
        for shoeBox in productGrid.css("div#hc-container"):
            yield { 
                'shoeName': shoeBox.css("a.product-link a::attr(data-productname)").extract_first(),
                'stockStatus': shoeBox.css("span.badge-text::text").extract_first(),
                'price': shoeBox.css("span.salesprice::text").extract_first()
            }
            

