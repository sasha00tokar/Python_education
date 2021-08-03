print('\n****************** task 2 ******************\n')

import random
class Warrior:
    def health(self, health_amount):
        self.health_amount = health_amount
    def __str__(self):
        return "Количество здоровья юнита:({})".format(self.health_amount)
    def kick(enemy):
        enemy.health_amount -= 20

first_unit = Warrior()
second_unit = Warrior()
first_unit.health(100)
second_unit.health(100)
while first_unit.health_amount and second_unit.health_amount > 0:
    attacking_unit =  random.choice(['first_unit', 'second_unit'])
    if attacking_unit == 'first_unit':
        Warrior.kick(second_unit)
        print("Атаковал first_unit, у противника осталось здоровья: {}".format(second_unit.health_amount))
    elif attacking_unit == 'second_unit':
        Warrior.kick(first_unit)
        print("Атаковал second_unit, у противника осталось здоровья: {}".format(first_unit.health_amount))
else:
    if first_unit.health_amount > 0:
        print("Unit first_unit win, {}".format(first_unit))
    elif second_unit.health_amount > 0:
        print("Unit second_unit win, {}".format(second_unit))

########################################################################################################################

print('\n****************** task 3 ******************\n')

class Person:
    def __init__(self, n, s, q = 1):
        self.name = n
        self.surname = s
        self.level = q
    def __str__(self):
        return "Имя сотрудника: {}\nФамилия сотрудника: {}\nКвалификация сотрудника: {}".format(self.name, self.surname, self.level)
    def __del__(self):
        print("До свидания мистер {} {}".format(self.name, self.surname))
p1 = Person('Sanya', 'Tokar', 12)
p2 = Person('Sasha', 'Rozko', 10)
p3 = Person('Maks', 'Hudko', 13)
min = p1.level
loose = p1
for employee in [p1, p2, p3]:
    if employee.level < min:
        min = employee.level
        loose = employee
print("Самое слабое звено мистер {} {} с квалификацией ({})".format(loose.name, loose.surname, loose.level))
loose.__del__()
input()


