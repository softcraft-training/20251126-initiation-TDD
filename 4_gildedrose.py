class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            self.decrement_sellin(item)

            if item.name == "Aged Brie":
                self.update_aged_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.update_backstage(item)
            elif item.name == "Conjured":
                self.update_conjured(item)
            else:
                self.update_general_item(item)

    def update_general_item(self, item):
        self.decrement_quality(item)
        if item.sell_in < 0:
            self.decrement_quality(item)

    def update_backstage(self, item):
        self.increment_quality(item)

        if item.sell_in < 10:
            self.increment_quality(item)

        if item.sell_in < 5:
            self.increment_quality(item)

        if item.sell_in < 0:
            self.reset_quality(item)

    def update_aged_brie(self, item):
        self.increment_quality(item)
        if item.sell_in < 0:
            self.increment_quality(item)

    def decrement_sellin(self, item):
        item.sell_in = item.sell_in - 1

    def reset_quality(self, item):
        item.quality = item.quality - item.quality

    def decrement_quality(self, item):
        if item.quality > 0:
            item.quality = item.quality - 1

    def increment_quality(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1

    def update_conjured(self, item):
        if item.quality > 0:
            item.quality = item.quality - 2

class LegacyGildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1

def test_gilded_rose():
    items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
    ]
    rose = GildedRose(items)

    legacy_items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
    ]

    legacy_rose = LegacyGildedRose(legacy_items)

    for i in range(10):
        rose.update_quality()
        legacy_rose.update_quality()

    assert [repr(x) for x in rose.items] == [repr(x) for x in legacy_rose.items]

@pytest.mark.parametrize("initialQuality, expectedQuality", [
    [ 20, 18 ],
    [ 0, 0 ],

])
def test_update_conjured(initialQuality, expectedQuality):
    items = [
        Item(name="Conjured", sell_in=10, quality=initialQuality),
    ]
    rose = GildedRose(items)
    rose.update_quality()
    assert rose.items[0].quality == expectedQuality
