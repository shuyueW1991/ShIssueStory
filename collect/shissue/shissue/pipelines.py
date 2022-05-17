# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from multiprocessing import connection
from itemadapter import ItemAdapter
from pytest import Item
from scrapy.exceptions import DropItem
import json

import pymongo



class ShissuePipeline:
    def __init__(self):
        self.ids_seen = set()

    def open_spider(self, spider):
        self.file = open('itemss.jl', 'w', encoding="utf8")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict(), indent=4, ensure_ascii=False) + "\n"

        adapter = ItemAdapter(item)
        if adapter['title'] in self.ids_seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.ids_seen.add(adapter['title'])
            self.file.write(line)
            return item
