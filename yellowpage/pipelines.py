# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb


class YellowPagePipline(object):
    def process_item(self, item, spider):
        print 'process_item is running...'
        db_settings = spider.settings.get('DB_SETTINGS')
        conn = MySQLdb.connect(**db_settings)
        cursor = conn.cursor()

        sql = ('insert into info(company, phone, email, website) '
            'values(%s, %s , %s, %s)')

        datas = (item['company'], item['phone'], item['email'], item['website'])
        try:
            cursor.execute(sql, datas)
        except Exception, e:
            print "Insert error:", e
            conn.rollback()
        else:
            conn.commit()
        cursor.close()
        conn.close()

        return item
