# -*- coding: utf-8 -*-
from scrapy.spiders import SitemapSpider
from scrapy import Request
from pprint import pprint as pp
from re import compile as re_compile

from comics_scraper.items import *


class ComixologySpider(SitemapSpider):
    name = 'comixology'
    allowed_domains = ['comixology.com']
    download_delay = 2
    # start_urls = [
    #     'https://www.comixology.com/Guerillas-1/digital-comic/12',
    #     'https://www.comixology.com/Guerillas-1/digital-comic/500',
    #     'https://www.comixology.com/Guerillas-1/digital-comic/5000',
    #     'https://www.comixology.com/Archie-1/digital-comic/27509',
    #     'https://www.comixology.com/The-Best-of-Archie-Comics-Deluxe-Edition/digital-comic/417673',
    #     'https://www.comixology.com/Sakura-Pakk-vs-Rumble-Pak-Bleed-MidSummers-Dream/digital-comic/52',
    #     'https://www.comixology.com/Detective-Comics-1937-2011-28-29/digital-comic/10901',
    # ]
    sitemap_urls = ['https://www.comixology.com/sitemap.xml']
    sitemap_rules = [
        ('\/digital-comic\/', 'parse_issue'),
        ('\/comics-creator\/', 'parse_creator'),
        ('\/comics-publisher\/', 'parse_publisher'),
        ('\/comics-series\/', 'parse_series'),
        ('\/comics-story-arc\/', 'parse_story_arc'),
        ('\/comics-genre\/', 'parse_genre'),
    ]

    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': 5
    }

    # used to grab the issue number
    re_issue_number = re_compile('\#([\d-]{0,6})')


    def clean_url(url):
        '''Remove url parameters'''
        return url.split('?')[0] if url else None


    def parse_issue(self, response):

        issue = {}
        issue['issue_id'] = int(response.url.split('/')[-1].split('?')[0])
        issue['title'] = response.xpath('//*[@id="column2"]/h1/text()').get()

        # handle missing '#'
        # issue['issue_number'] = None
        # if len(issue['title'].split('#')) == 2:
        #     issue['issue_number'] = int(issue['title'].split('#')[1])

        issue['issue_number'] = None
        issue['issue_number_end'] = None

        # needs to handle missing '#' and double issues: '#28-29'
        issue_match = ComixologySpider.re_issue_number.search(issue['title'])

        if issue_match:
            # there is an issue number present (`#`)
            parts = issue_match.group(1)

            if len(parts) > 1:
                parts = parts.split('-')
                issue['issue_number']  = int(parts[0]) # the beginning issue number
                issue['issue_number_end']  = int(parts[1]) # the beginning issue number
            else:
                # not a double issue
                issue['issue_number'] = int(parts)


        issue['double_issue'] = None
        

        issue['series'] = issue['title'].split('#')[0].strip()
        issue['series_url'] = response.xpath('//*[@id="cmx_breadcrumb"]/a[3]/@href').get()

        try:
            issue['price'] = float(response.xpath('//h5[contains(@class, "item-price")]/text()').get().replace('$', ''))
        except ValueError:
            issue['price'] = None # the price = FREE

        issue['cover_url'] = response.xpath('//*[@id="cover"]/img/@src').get()

        issue['description'] = response.xpath('//*[@id="column2"]/section[@class="item-description"]/text()')
        # handle cases when there is no disclaimer field in the description
        if len(issue['description']) == 2:
            issue['description'] = issue['description'][1].get()
        else:
            issue['description'] = issue['description'].get()
        issue['description'] = issue['description'].strip()

        issue['publisher'] = response.xpath('normalize-space(//*[@id="column3"]/div[@class="credits"]/div[@class="publisher"]/a[2]/h3/text())').get()
        issue['publisher_url'] = response.xpath('//*[@id="column3"]/div[@class="credits"]/div[@class="publisher"]/a[2]/@href').get()

        issue['writers'] = map(str.strip,
                            response.xpath('//h2[@title="Written by"]/a/text()').getall()
                         )
        issue['writers_urls'] = response.xpath('//h2[@title="Written by"]/a/@href').getall()
        # how do we model author ordering? zip(range(1, len(writers)), (issue['writers'], issue['writer_urls']))

        issue['artists'] = list(map(str.strip,
                            response.xpath('//h2[@title="Art by"]/a/text()').getall()
                         ))
        issue['artists_urls'] = response.xpath('//h2[@title="Art by"]/a/@href').getall()
        # multiple artists + ordering

        # colors ("Colored by")
        issue['colors'] = list(map(str.strip,
                            response.xpath('//h2[@title="Colored by"]/a/text()').getall()
                         ))
        issue['colors_urls'] = response.xpath('//h2[@title="Colored by"]/a/@href').getall()

        # inks ("Inks")
        issue['inks'] = list(map(str.strip,
                            response.xpath('//h2[@title="Inks"]/a/text()').getall()
                         ))
        issue['inks_urls'] = response.xpath('//h2[@title="Inks"]/a/@href').getall()

        # pencils
        issue['pencils'] = list(map(str.strip,
                            response.xpath('//h2[@title="Pencils"]/a/text()').getall()
                         ))
        issue['pencils_urls'] = response.xpath('//h2[@title="Pencils"]/a/@href').getall()

        # handle all creators before issues
        for url in (
            issue['writers_urls'] +
            issue['artists_urls'] +
            issue['colors_urls'] +
            issue['inks_urls'] +
            issue['pencils_urls']):
            yield Request(url=url, callback=self.parse_creator)

        issue['story_arc_name'] = response.xpath('normalize-space(//*[@id="column3"]/div[@class="credits"]/div[contains(text(), \'Story Arc\')]/following-sibling::a/text())').get()
        issue['story_arc_url'] = response.xpath('//*[@id="column3"]/div[@class="credits"]/div[contains(text(), \'Story Arc\')]/following-sibling::a/@href').get()

        # handle story arcs first
        if issue['story_arc_url']:
            yield Request(url=issue['story_arc_url'], callback=self.parse_story_arc)
        
        issue['page_count'] = int(response.xpath('//h4[contains(text(), \'Page Count\')]/following-sibling::div[@class="aboutText"]/text()').get().split()[0])
        issue['print_release_date'] = response.xpath('//h4[contains(text(), \'Print Release Date\')]/following-sibling::div[@class="aboutText"]/text()').get()
        issue['digital_release_date'] = response.xpath('//h4[contains(text(), \'Digital Release Date\')]/following-sibling::div[@class="aboutText"]/text()').get()
        
        # could be a ref table AgeRating()
        issue['age_rating'] = response.xpath('normalize-space(//h4[contains(text(), \'Age Rating\')]/following-sibling::div[@class="aboutText"]/text())').get()

        # could be a ref table Seller()
        issue['sold_by'] = response.xpath('//h4[contains(text(), \'Sold by\')]/following-sibling::div[@class="aboutText"]/text()').get()
        

        issue['genre_names'] = response.xpath('//div[@class="credits"]/div[contains(text(), \'Genres\')]/following-sibling::a[contains(@href, \'comics-genre\')]/text()').getall()
        issue['genre_names'] = map(str.strip, issue['genre_names'])
        issue['genre_urls'] = response.xpath('//div[@class="credits"]/div[contains(text(), \'Genres\')]/following-sibling::a[contains(@href, \'comics-genre\')]/@href').getall()
        issue['genres'] = zip(issue['genre_names'], issue['genre_urls']) # turn the genres into name + url pairs

        # handle genres first
        for url in issue['genre_urls']:
            yield Request(url=url, callback=self.parse_genre)

        # If this has a value, then it is part of a collected edition. The collected edition is itself an issue.
        issue['collected_edition_url'] = response.xpath('//*[@class="collectedEdition"]/div[contains(text(), \'collected edition\')]/following-sibling::a/@href').get()
        issue['has_collected_edition'] = False

        # handle collected editions first
        if issue['collected_edition_url']:
            issue['has_collected_edition'] = True
            yield Request(url=issue['collected_edition_url'], callback=self.parse_issue)

        issue['ratings_count'] = response.xpath('//div[@itemprop="reviewCount"]/text()').get()
        issue['star_rating'] = int(response.xpath('//div[@class="rating-total hidden"]/text()').get())

        yield issue

    def parse_creator(self, response):
        creator = {}
        creator['name'] = response.xpath('normalize-space(//*[@id="cmx_breadcrumb"]/h2/text())').get()
        creator['url'] = self.clean_url(response.url)
        yield creator

    def parse_genre(self, response):
        genre = {}
        creator['name'] = response.xpath('normalize-space(//*[@id="cmx_breadcrumb"]/h2/text())').get()
        creator['url'] = self.clean_url(response.url)
        yield creator

    def parse_publisher(self, response):
        pass

    def parse_creator(self, response):
        pass

    def parse_story_arc(self, response):
        pass

    def parse_series(self, response):
        pass
