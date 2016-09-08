# -*- coding: utf-8 -*-
import scrapy
from pikabucrawl.simpledate import SimpleDate
from scrapy.exceptions import CloseSpider

# Структура URL:
# http://pikabu.ru/new/{date}?page={page}
# new - свежее, best - лучшее
# date - дата (день-месяц-год, день и месяц с дополнительными нулями, год полностью)
# page - номер страницы
#
# Структура URL поиска:
# http://pikabu.ru/search.php?n=32&r=0
# , где:
# n - тип материала (1-Любой, 2-Текст, 4-Картинки, 8-Видео, 16-"Моё", 32-Клубничка. Для нескольких - суммируется)
# r - рейтинг поста (0-Любой, 1-"-100", 2-"0", 3-"25", 4-"100", 5-"250", 6-"500", 7-"1000", 8-"2500", 9-"5000", 10-"10000")
# st - категория поста (1-"Свежее(по умолчанию)", 2-"Горячее")
# d - дата поста (0-1 января 2008)
# D - конечная дата (аналогино дате поста. Выбираются все посты из периода [d, D])
# t - теги. Перечесляются через запятую.
# page - номер страницы
#
#
#
class PikabuSpider(scrapy.Spider):
    name = "pikaspider"
    allowed_domains = ["pikabu.ru"]
    crawl_date = SimpleDate(10, 6, 2016)
    end_date = None
    crawl_date_count = 71
    pages = 10
    next_page = 1
    template_url = 'http://pikabu.ru/new/{date}?page={page}'
    __cookies= {'PHPSESS':'''4ccor9ri8ucf1jla9b6rpn0k5q495lef''','phpDug2': '''a%3A4%3A%7Bs%3A3%3A%22uid%22%3Bs%3A6%3A%22346299%22%3Bs%3A8%3A%22username%22%3Bs%3A5%3A%22unnmd%22%3Bs%3A3%3A%22rem%22%3Bs%3A32%3A%22624bfbed23b3a6959c3a83bb72b144a2%22%3Bs%3A5%3A%22tries%22%3Bi%3A0%3B%7D'''}




    def start_requests(self):
        self.end_date = self.crawl_date + self.crawl_date_count
        if self.end_date > self.crawl_date:
            url = self.template_url.format(date=str(self.crawl_date), page=1)
            yield scrapy.Request(url,cookies={'PHPSESS':'''4ccor9ri8ucf1jla9b6rpn0k5q495lef''','phpDug2': '''a%3A4%3A%7Bs%3A3%3A%22uid%22%3Bs%3A6%3A%22346299%22%3Bs%3A8%3A%22username%22%3Bs%3A5%3A%22unnmd%22%3Bs%3A3%3A%22rem%22%3Bs%3A32%3A%22624bfbed23b3a6959c3a83bb72b144a2%22%3Bs%3A5%3A%22tries%22%3Bi%3A0%3B%7D'''}, callback=self.parse)
            #yield scrapy.Request("http://pikabu.ru/story/dnevnik_kh_4059903", callback=self.parse_item)
            # Пост с положительным рейтингом
            #yield scrapy.Request("http://pikabu.ru/story/zloy_vegan_4056224", callback=self.parse_item)
            # Пост с отриательным рейтингом
            #yield scrapy.Request("http://pikabu.ru/story/bez_kefira_i_bez_kvasa_3985322", callback=self.parse_item)
            # Удаленный пост
            #yield scrapy.Request("http://pikabu.ru/story/myagkosti_post_4045696", callback=self.parse_item)
            # Моё да ещё и с клубникой
            #yield scrapy.Request("http://pikabu.ru/story/rabochiy_den_podkhodit_k_kontsu_4051774", callback=self.parse_item)
            # Проблемный пост с тегами
            #yield scrapy.Request("http://pikabu.ru/story/_4003627", callback=self.parse_item)

    def create_ajax_request(self, number):
        url = self.template_url.format(date=str(self.crawl_date), page=number)
        #print "Next url:", url
        return scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        if not response.xpath('//div[contains(@id,"no_stories_msg")]/@id').extract():
            for row in self.parse_item(response):
                yield row
            self.next_page += 1
        else:
            self.next_page = 1
            self.crawl_date += 1
            if self.end_date < self.crawl_date:
                raise CloseSpider("No more pages")
        yield self.create_ajax_request(self.next_page)

    def parse_item(self, response):
        print "Parse url:", response.url
        storys_on_page = response.xpath('//div[contains(@class,"story")]')
        for story in storys_on_page:
            sel = scrapy.Selector(text=story.extract())
            id = self.parse_id(sel)
            ratio = self.parse_ratio(sel)
            isdel = False
            if not ratio:  #проверка удалён ли пост
		#warn
                if sel.xpath('//i[contains(@class, "i-sprite--inline-block i-sprite--feed__rating-trash")]').extract():
                    isdel = True
            href = ''
            if id:
                href = self.parse_href(id, sel)
            date = self.parse_date(sel)
            user = self.parse_user(sel)
            pron = self.parse_pron(sel) #Клубничка не отображается для незалогиненого пользователя
            my = self.parse_my(sel)
            tags = self.parse_tags(sel)
            cat = self.parse_category(sel)
            #print cat, ratio, id
            #print id, ratio, isdel, href, date, user, my, pron, tags
            #raise CloseSpider("Test")
            yield {
                'id': id,
                'ratio' : ratio,
                'href' : href,
                'date' : date,
                'user' : user,
                'tags' : tags,
                'my': my,
                'pron' : pron,
                'isdel': isdel,
                'cat' : cat,
            }

    def parse_id(self, selector):
        id = selector.xpath('//div[@class="story"]/@data-story-id').extract()
        return id[0] if id else None

    def parse_ratio(self, selector):
        ratio = selector.xpath('//div[@class="story__rating-count"]/text()').extract()
        if ratio:
            try:
                return int(''.join(ratio))
            except:
                return None
        else:
            return None

    def parse_href(self, id, selector):
        href = selector.xpath('//div[@class="story__header-title"]/a/@href').extract()
        return href[0] if href else None

    def parse_user(self, selector):
        user = selector.xpath('//a[contains(@href, "profile")]/text()').extract()
        return user[0] if user else None

    def parse_date(self, selector):
        date = selector.xpath('//div[@class="story__date"]/@title').extract()
        return date[0] if date else None

    def parse_pron(self, selector):
        pron = selector.xpath('//a[@class="story__straw"]').extract()
        return True if pron else False

    def parse_my(self, selector):
        my = selector.xpath('//a[@class="story__authors"]').extract()
        return True if my else False

    def parse_tags(self, selector):
        tags = selector.xpath('//div[@class="story__tags"]/*')
        tags_list = list()
        for row in tags:
            sel = scrapy.Selector(text=row.extract())
            tag_href = sel.xpath('//a[@href]/@href').extract()
            tag_text = sel.xpath('//a[@class]/text()').extract()
            tag_href = tag_href[0] if tag_href else None
            if tag_href:
                tag_href = tag_href.replace('/hot', '')
            tag_text = tag_text[0] if tag_text else None
            tags_list.append({"txt": tag_text, "hrf": tag_href})
        return tags_list

    def parse_category(self, selector):
        category = selector.xpath('//noindex/img/@class').extract()
        if not category:
            return "Other" # категория контента не распознана
        cat_text = category[0]
        if "showtext" in category[0]:
            return "Text"
        elif "showpic" in category[0]:
            return "Picture"
        elif "showvideo" in category[0]:
            return "Video"
        elif "showtgp" in category[0]:
            # категория новых постов, которые включают
            # и текст, и видео, и всё что угодно
            return "All"
        else:
            return "Other" # Неизвестная категория
