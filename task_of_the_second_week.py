import random
class Warrior:
    def __init__(self, health_amount):
        self.health_amount = health_amount
    def __str__(self):
        return "Количество здоровья юнита:({})".format(self.health_amount)
    def __sub__(self, other):
        return Warrior(self.health_amount - other)

first_unit = Warrior(100)
second_unit = Warrior(100)
while first_unit.health_amount and second_unit.health_amount > 0:
    attacking_unit =  random.choice(['first_unit', 'second_unit'])
    if attacking_unit == 'first_unit':
        second_unit = second_unit - 20
        print("Атаковал first_unit, у противника осталось здоровья: {}".format(second_unit.health_amount))
    elif attacking_unit == 'second_unit':
        first_unit = first_unit - 20
        print("Атаковал second_unit, у противника осталось здоровья: {}".format(first_unit.health_amount))
else:
    if first_unit.health_amount > 0:
        print("Unit first_unit win, {}".format(first_unit))
    elif second_unit.health_amount > 0:
        print("Unit second_unit win, {}".format(second_unit))

