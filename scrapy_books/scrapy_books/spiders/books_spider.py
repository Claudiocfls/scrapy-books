import scrapy
from scrapy.selector import Selector

class BooksSpider(scrapy.Spider):
    name = 'books_spider'
    start_urls = [
        'http://books.toscrape.com'
    ]

    def parse(self, response):
        categories_links = response.xpath('//div[@class="side_categories"]/ul/li/ul/li/a/@href').extract()
        for category_link in categories_links:
            yield response.follow(category_link, callback=self.parse_category)

    def parse_category(self, response):
        product_pods = response.xpath('//article[@class="product_pod"]').extract()
        for product in product_pods:
            title = Selector(text=product).xpath('//h3/a/@title').get()
            href = Selector(text=product).xpath('//h3/a/@href').get()
            price = Selector(text=product).xpath('//div[@class="product_price"]/p[@class="price_color"]/text()').get()
            image_src = Selector(text=product).xpath('//div[@class="image_container"]/a/img/@src').get()
            yield {
                'book_title': title,
                'book_url': response.urljoin(href),
                'book_price': price,
                'book_cover_src': response.urljoin(image_src)
            }

        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse_category)
