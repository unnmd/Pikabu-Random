# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pikabucrawl.items import PikabuCrawlItem
from time import gmtime, strftime, time
import sqlite3
# http://mysql-python.sourceforge.net/
import MySQLdb

class SimpleDuration():
    __beginTime = None
    __resultString = ''

    def start(self):
        self.__beginTime = time()

    def stop(self):
        duration = time() - self.__beginTime
        hour = int(duration / 3600)
        min = int((duration - hour * 3600) / 60)
        sec = duration % 60
        self.__resultString = "{:0=2}-{:0=2}-{:0=2}".format(hour, min, (int(sec)))

    def __str__(self):
        return self.__resultString

class PikabuSaveMySQL(object):
    __db = None
    __curs = None
    __insertrows = 0
    __updaterows = 0
    __insert_story_tmp = 'INSERT INTO storys ( \
                          story_id, date, ratio, user, \
                          pron, my, del, category, href) \
                          VALUES ( \
                          {id}, "{date}", {ratio}, {user}, \
                          {pron}, {my}, {isdel}, {cat}, \'{href}\' );'
    __insert_category_tmp = 'INSERT INTO categorys ( \
                             search_num, info) \
                             VALUES ( {snum}, {info} );'
    __insert_user_tmp = 'INSERT INTO users (nick) VALUES("{nick}");'

    def __init__(self):
        #passwd='9vWMZQK1aFs0wi77'
	self.__db = MySQLdb.connect(user='USER', passwd='PASSWORD', db='DBNAME', host='localhost', charset='utf8')
	self.__curs = self.__db.cursor()

    def __del__(self):
        self.__db.close()

    def process_item(self, item, spider):
        try:
            user_id = self.search_user_id(item['user'])
            categ = self.search_category_id(item['cat'])
            try:
                ratio = int(item['ratio'])
            except TypeError:
                ratio = 'NULL'
            story_insert = self.__insert_story_tmp.format(
                                    id=int(item['id']),
                                    date=strftime("%Y-%m-%d %H:%M:%S", gmtime(int(item['date']))),
                                    ratio=ratio,
                                    user=user_id,
                                    pron=int(item['pron']),
                                    my=int(item['my']),
                                    isdel=int(item['isdel']),
                                    cat=categ,
                                    href=item['href'])
            self.__curs.execute(story_insert)
            self.insert_tags(int(item['id']), item['tags'])
            self.__db.commit()
            return item
        except MySQLdb.Error as e:
            # Добавить обработку существующих записей
            print(e.args)
        except:
            print "Exception in process_item"
        finally:
            return item

    def search_user_id(self, user_name):
        try:
            self.__curs.execute('SELECT user_id FROM users WHERE nick="%s"' % user_name)
            if self.__curs.rowcount > 0:
                return self.__curs.fetchall()[0][0]
            else:
                user_insert = self.__insert_user_tmp.format(nick=user_name)
                self.__curs.execute(user_insert)
                return self.__curs.lastrowid #or __db.insert_id()
        except MySQLdb.Error as e:
            # Добавить обработку существующих записей
            print "Exception in search_user_id %s", e.args

    def search_category_id(self, category):
        try:
            self.__curs.execute('SELECT cat_id FROM categorys WHERE info="%s"' % category)
            if self.__curs.rowcount > 0:
                return self.__curs.fetchall()[0][0]
            else:
                self.__curs.execute('INSERT INTO categorys(search_num, info) VALUES (0, "%s")' % category)
                return self.__curs.lastrowid
        except MySQLdb.Error as e:
            print "Exception in search_category_id", e.args

    def search_tag_id(self, tag):
        try:
            tag_text = tag['txt'].encode('utf-8','ignore')
            tag_href = tag['hrf'].encode('utf-8','ignore')
            query = 'SELECT tag_id FROM tags WHERE text="%s"' % tag_text
            self.__curs.execute(query)
            if self.__curs.rowcount > 0:
                return self.__curs.fetchall()[0][0]
            else:
                query = 'INSERT INTO tags (text, href) VALUES("%s", "%s")' % (tag_text, tag_href)
                self.__curs.execute(query)
                return self.__curs.lastrowid
        except MySQLdb.Error as e:
            print "Exception in search_tag_id", e.args

    def insert_tags(self, story, tags):
        for tag in tags:
            tag_id = self.search_tag_id(tag)
            if not tag_id:
                return
            try:
                self.__curs.execute('INSERT INTO tags_in_storys(story, tag) VALUES(%d, %d)' % (story, tag_id))
            except MySQLdb.Error as e:
                # Добавить обработку существующих записей
                print "Exception in insert_tags", e.args
