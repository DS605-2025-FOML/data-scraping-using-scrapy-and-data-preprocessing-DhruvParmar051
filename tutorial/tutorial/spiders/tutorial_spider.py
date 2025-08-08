import scrapy

from ..items import TutorialItem

class TutorialSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]
    
    
    def parse(self, response):
        
        all_quote_div = response.css('div.quote')
        
        items = TutorialItem()
        
        for quote_item in all_quote_div:
            
            text = quote_item.css('span.text::text').extract_first()
            author = quote_item.css('.author::text').extract_first()
            tags = quote_item.css('.tag::text').extract_first()
            
            items['text'] = text
            items['author'] = author
            items['tags'] = tags
            
            yield items
            
        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)