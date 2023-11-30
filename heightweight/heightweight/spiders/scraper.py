import scrapy

class scraper(scrapy.Spider):
    name = 'scraper'

    start_urls = ['https://www.atptour.com/en/rankings/singles']

    def parse(self, response):
        '''
        start on rankings page, then navigate
        '''