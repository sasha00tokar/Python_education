class Item:
    def __init__(self, n, c, p):
        self.name = n
        self.count = c
        self.price = p
    def __str__(self):
        return str(self.name)
class Bag:
    shopping_list = {}
    # def __str__(self):
    #     return self.name
    def show_bag(self):
        for key in self.shopping_list:
            # print(self.shopping_list[key]['count'])
            print('{} : count {}, price {}'.format(key,
                  self.shopping_list[key]['count'], self.shopping_list[key]['price']))
    def add_bag(self, item):
        if item.name not in self.shopping_list:
            self.shopping_list[item.name] = {'count':item.count, 'price':item.price}
        else:
            self.shopping_list[item.name]['count'] += 1
            self.shopping_list[item.name]['price'] += item.price
    def del_from_bag(self, item):
        if item.name in self.shopping_list:
            self.shopping_list.pop(item.name)
        else:
            print('Товара нету в корзине!')
    def change_count(self, item):
        n = int(input('Введіть к-сть одиниць товару:'))
        self.shopping_list[item.name]['count'] = n
        self.shopping_list[item.name]['price'] = item.price * n
    def sum_price(self):
        sum = 0
        for el in self.shopping_list:
            sum += self.shopping_list[el]['price']
        return print('Сумма всіх товарів в корзині: {}'.format(sum))

p1 = Item('banana', 1, 10)
p2 = Item('banana', 1, 10)
p3 = Item('mango', 1, 20)
c = Bag()
c.add_bag(p1)
c.add_bag(p2)
c.add_bag(p3)
c.show_bag()
c.sum_price()








    # def addToBag(self, n, c, p):
    #     self.shopping_list.append(Item(n, c, p))

