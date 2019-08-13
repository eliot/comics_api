# -*- coding: utf-8 -*-
import scrapy
from pprint import pprint as pp
# import ..


class ComixologySpider(scrapy.Spider):
    name = 'comixology'
    allowed_domains = ['comixology.com']
    start_urls = ['https://www.comixology.com/Guerillas-1/digital-comic/12',
        'https://www.comixology.com/Guerillas-1/digital-comic/500',
    ]


    def parse(self, response):
        data = {}
        data['_title'] = response.xpath('//*[@id="column2"]/h1/text()').get()
        data['issue_number'] = int(data['_title'].split('#')[1])
        data['series'] = data['_title'].split('#')[0].strip()
        data['series_url'] = response.xpath('//*[@id="cmx_breadcrumb"]/a[3]/@href').get()
        data['price'] = float(response.xpath('//*[@id="column1"]/div[2]/div/div/h5[1]/text()').get().replace('$', ''))
        data['cover_url'] = response.xpath('//*[@id="cover"]/img/@src').get()
        data['description'] = response.xpath('//*[@id="column2"]/section[@class="item-description"]/text()')[1].get()
        data['publisher'] = response.xpath('normalize-space(//*[@id="column3"]/div[@class="credits"]/div[@class="publisher"]/a[2]/h3/text())').get()
        data['publisher_url'] = response.xpath('//*[@id="column3"]/div[@class="credits"]/div[@class="publisher"]/a[2]/@href').get()

        # redo this one
        data['writer'] = response.xpath('normalize-space(//h2[@title="Written by"]/a/text())').get()
        data['writer_url'] = response.xpath('//*[@id="column3"]/div/div[3]/dl/dd[1]/h2/a/@href').get()
        # multiple authors + author ordering

        data['artist'] = response.xpath('normalize-space(//*[@id="column3"]/div[@class="credits"]/div[@class="credits"]/dl/dt[contains(text(), \'Art by\')]/following-sibling::dd/h2[@title="Art by"]/a/text())').get()
        data['artist_url'] = response.xpath('//*[@id="column3"]/div[@class="credits"]/div[@class="credits"]/dl/dt[contains(text(), \'Art by\')]/following-sibling::dd/h2[@title="Art by"]/a/@href').get()

        data['story_arc_name'] = response.xpath('normalize-space(//*[@id="column3"]/div[@class="credits"]/div[contains(text(), \'Story Arc\')]/following-sibling::a/text())').get()
        data['story_arc_url'] = response.xpath('//*[@id="column3"]/div[@class="credits"]/div[contains(text(), \'Story Arc\')]/following-sibling::a/@href').get()
        
        # genres
        data['page_count'] = response.xpath('//h4[contains(text(), \'Page Count\')]/following-sibling::div[@class="aboutText"]/text()').get().split()[0]
        data['print_release_date'] = response.xpath('//h4[contains(text(), \'Print Release Date\')]/following-sibling::div[@class="aboutText"]/text()').get()
        data['digital_release_date'] = response.xpath('//h4[contains(text(), \'Digital Release Date\')]/following-sibling::div[@class="aboutText"]/text()').get()
        data['age_rating'] = response.xpath('normalize-space(//h4[contains(text(), \'Age Rating\')]/following-sibling::div[@class="aboutText"]/text())').get()
        data['sold_by'] = response.xpath('//h4[contains(text(), \'Sold by\')]/following-sibling::div[@class="aboutText"]/text()').get()
        
        data['genre_names'] = response.xpath('normalize-space(//div[@class="credits"]/div[contains(text(), \'Genres\')]/following-sibling::a[contains(@href, \'comics-genre\')]/text())').get()
        data['genre_urls'] = response.xpath('normalize-space(//div[@class="credits"]/div[contains(text(), \'Genres\')]/following-sibling::a[contains(@href, \'comics-genre\')]/@href').get()
        data['genres'] = zip(data['genre_names'], data['genre_urls'])

        # part of a collected edition e.g. issue=500
        # colored by
        # pencils (https://www.comixology.com/Madman-Atomic-Comics-6/digital-comic/900?r=1)
        # inks

        print('---------------')
        pp(data)
        print('---------------')
