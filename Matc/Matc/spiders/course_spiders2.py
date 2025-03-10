from scrapy import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
import scrapy
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError
from Matc.items import MatcItem


class MatcSpider( scrapy.Spider ):

    name = 'matc2'

    allowed_domains = ['madisoncollege.edu']

    start_urls = [ 

            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001211/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001213/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001215/DEGR/2018-05-29',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001220/DEGR/2018-05-29',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001221/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001222/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001223/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001225/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001229/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001230/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001231/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001232/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/012071/DEGR/2018-05-29',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/013468/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/015455/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/011996/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/012329/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/012330/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/015341/DEGR/2018-05-29',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/014934/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/006834/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/014766/DEGR/2018-05-29',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001593/DEGR/2018-05-29',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/014767/DEGR/2018-05-29',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/016508/DEGR/2019-06-03',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001610/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001611/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001616/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001635/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001640/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/014525/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001646/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001650/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001653/DEGR/2018-05-29',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/016480/DEGR/2019-06-03',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001655/DEGR/2018-05-29',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/014787/DEGR/2018-05-29',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/014788/DEGR/2018-05-29',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/015392/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/015517/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/015517/DEGR/2017-05-30', 
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001039/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001040/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001042/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001044/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001045/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001046/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001047/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001049/DEGR/2017-05-30',
            



            ]

    def  start_requests( self ):

        for u in self.start_urls:

            yield scrapy.Request( u, callback = self.parse_httpbin, 
                    errback = self.errback_httpbin,
                    dont_filter = True )

    def parse_httpbin( self, response ):

        self.logger.info("Go successful response {}".format(response.url) )

        preqs_check = False

        items = MatcItem() 
        #course_elements = response.xpath('div[@class="main"]')
    
        title = response.xpath('//div[@class="strong section-body"]/text()').extract_first()
        description = response.xpath('//div[@class="section-body"]/text()').extract_first()
        unit =  response.xpath('////div[@class="pull-right"]/div/text()').extract()[1]
        course = response.xpath('////div[@class="pull-right"]/div/text()').extract()[2]
        department =  response.xpath('////div[@class="pull-right"]/div/text()').extract()[4]
        #prerequisites = response.xpath('////div[@class="pull-right"]/div/text()').extract()[5]
        #prerequisites = response.css('div.pull-right > div::text').extract()[5]

        items['title'] = title
        items['description'] = description
        items['unit'] = unit
        items['course'] = course
        #items['prerequisites'] = prerequisites
        items['department'] = department

        yield items
    
    def errback_httpbin( self, failure):

        # log all failures
        self.logger.error(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the failure's type:

        if failure.check(HttpError):

            # These exception come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error("HttpError on %s", response.url )

        elif failure.check(DNSLookupError):

            # This is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url )

        elif failure.check(TimeoutError, TCPTimeOutError ):

            request = failure.request 
            self.logger.error('TimeoutError on %s', request.url)



























