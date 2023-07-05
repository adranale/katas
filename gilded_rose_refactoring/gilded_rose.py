# -*- coding: utf-8 -*-
MIN_QUALITY = 0
SELL_DATE_THRESHOLD_1 = 11
SELL_DATE_THRESHOLD_2 = 6
SELL_DATE_THRESHOLD_LAST = 0
MAX_QUALITY = 50
AGED_BRIE = "Aged Brie"
TAFKAL_ETC_CONCERT = "Backstage passes to a TAFKAL80ETC concert"
SLUFURAS_HAND_OF_RAGNAROS = "Sulfuras, Hand of Ragnaros"


def increase_quality(item):
    item.quality = item.quality + 1


def decrease_quality(item):
    item.quality = item.quality - 1


def decrease_quality_by_half(item):
    item.quality = item.quality - item.quality


def decrease_sell_in(item):
    item.sell_in = item.sell_in - 1


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == AGED_BRIE or item.name == TAFKAL_ETC_CONCERT:
                if item.quality < MAX_QUALITY:
                    increase_quality(item)
                    if item.name == TAFKAL_ETC_CONCERT and item.quality < MAX_QUALITY:
                        if item.sell_in < SELL_DATE_THRESHOLD_2:
                            increase_quality(item)
                            increase_quality(item)
                        elif item.sell_in < SELL_DATE_THRESHOLD_1:
                            increase_quality(item)
            else:
                if item.name != SLUFURAS_HAND_OF_RAGNAROS and item.quality > MIN_QUALITY:
                    decrease_quality(item)

            if item.name != SLUFURAS_HAND_OF_RAGNAROS:
                decrease_sell_in(item)
            if item.sell_in < SELL_DATE_THRESHOLD_LAST:
                if item.name == AGED_BRIE:
                    if item.quality < MAX_QUALITY:
                        increase_quality(item)
                elif item.name == TAFKAL_ETC_CONCERT:
                    decrease_quality_by_half(item)
                elif item.name != SLUFURAS_HAND_OF_RAGNAROS:
                    if item.quality > MIN_QUALITY:
                        decrease_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
