store = {
    'banana': {'price': 10, 'discount_price': 7, 'discount_count': 3},
    'mango': {'price': 15, 'discount_price': 12, 'discount_count': 3},
    'apple': {'price': 20, 'discount_price': 17, 'discount_count': 3}
}


class Item:
    def __init__(self, n, c):
        self.name = n
        self.count = c

    def __str__(self):
        return str(self.name)


class Bag:
    def __init__(self):
        self.shopping_list = {}

    def bulk_discount_price(self):
        for key, value in self.shopping_list.items():
            value['price'] = (value['count'] - (value['count'] % store[key]['discount_count'])) * \
                             store[key]['discount_price'] + (value['count'] % store[key]['discount_count']) * \
                             store[key]['price']

    def show_bag(self):
        self.bulk_discount_price()
        return self.shopping_list

    def add_bag(self, item):
        if item.name not in self.shopping_list:
            self.shopping_list[item.name] = {'count': item.count}
        else:
            self.shopping_list[item.name]['count'] += item.count

    def del_from_bag(self, item):
        if item.name in self.shopping_list:
            self.shopping_list.pop(item.name)
            return True
        else:
            return False

    def sum_price(self):
        return sum(value['price'] for key, value in self.shopping_list.items())

# p1 = Item('banana', 1)
# p2 = Item('banana', 3)
# p3 = Item('mango', 1)
# p4 = Item('mango', 2)
# c = Bag()
# c.add_bag(p1)
# c.add_bag(p2)
# c.add_bag(p3)
# c.add_bag(p4)
# print(c.show_bag())
# print(c.sum_price())
# #print(c.show_bag())