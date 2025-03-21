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
from UW_Madison.items import UwMadisonItem

# CrawlSpider
class Madison_courses( scrapy.Spider ):

    name = 'uw_madison_final'

    allowed_domains = ['wisc.edu']

    start_urls = [

            "http://guide.wisc.edu/courses/acct_i_s/",
            #"http://guide.wisc.edu/courses/zoology/",
    
    ]
    
    def  start_requests( self ):

        for u in self.start_urls:
            
            yield scrapy.Request( u, callback = self.parse_httpbin,
                    errback = self.errback_httpbin,
                    dont_filter = True )


    def parse_httpbin( self, response ):

        self.logger.info("Got successful response {}".format(response.url) )
        courses = response.css('span.courseblockcode::text').extract() 
        #prerequisites  = response.css('p.courseblockextra.noindent.clearfix > span.cbextra-data > .bubblelink::text').extract()
        #prerequisites = response.xpath('//div[@class="cb-extras"]/p/span[@class="cbextra-data"]/a/@title').extract()

        prerequisites = response.xpath('//div[@class="cb-extras"]/p/span[@class="cbextra-data"]/a[1]/@title[1]').extract()

        title = response.css('div.sc_sccoursedescs > div.courseblock > p.courseblocktitle > strong::text').extract()
        unit = response.css('.courseblockcredits::text').extract()
        description =  response.css('.courseblockdesc::text').extract()
        
        final_courses = [] 
        final_prerequisites = []
        final_title = []
        final_unit = []
        final_description = []

        for course_set in courses:

            if course_set == '\n' or course_set == ' ':
                continue
            final_courses.append(course_set)

        for prerequisites_set in prerequisites:

            if prerequisites_set == '\n' or prerequisites_set == ' ' :
                continue
            final_prerequisites.append(prerequisites_set)

        for title_set in title:

            if title_set == '\n' or title_set == ' ':
                continue 
            final_title.append(title_set)

        for unit_set in unit: 

            if unit_set == '\n' or unit_set == ' ':
                continue
            final_unit.append(unit_set)

        for description_set in description: 

            if description_set == '\n' or description_set == ' ':
                continue 
            final_description.append(description_set)
          

        course_size = len(final_courses)
        items = []
        track_index = 0
        
        print("Course_Size:", course_size )
        print("prerequisites_size", len(final_prerequisites))
        print("title_size", len(final_title))
        print("Unit_size", len(final_unit))
        print("description", len(final_description))

        while track_index < course_size:
          
            print("Track_index", track_index )

            item = UwMadisonItem()

            #courses = response.css('span.courseblockcode::text').extract()[ track_index ].strip()
            #title = response.css('div.sc_sccoursedescs > div.courseblock > p.courseblocktitle > strong::text').extract()[ track_index ].strip()
            #unit = response.css('.courseblockcredits::text').extract()[ track_index ].strip()
            #description =  response.css('.courseblockdesc::text').extract()[ track_index ].strip()

            item['course'] = final_courses[ track_index ]
            item['title'] = final_title[ track_index ]
            item['unit'] = final_unit[ track_index ]
            item['description'] = final_description[ track_index ]
        
            try:

                item['prerequisites'] = final_prerequisites[ track_index ]

            except IndexError:

                item['prerequisites'] = 'None'


            items.append(item)
            track_index += 1
            
        return items

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



        
