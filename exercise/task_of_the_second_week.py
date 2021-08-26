import random

from class_for_task_7 import WinDoor, Room

print('\n****************** task 2 ******************\n')


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
    attacking_unit = random.choice(['first_unit', 'second_unit'])
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
        return str([self.name, self.surname, self.level])

    def __del__(self):
        return str(self.name), str(self.surname)


p1 = Person('Sanya', 'Tokar', 12)
p2 = Person('Sasha', 'Rozko', 10)
p3 = Person('Maks', 'Hudko', 13)
min = p1.level
loose = p1
for employee in [p1, p2, p3]:
    if employee.level < min:
        min = employee.level
        loose = employee
print(p1)
print(p2)
print(p3)
print("Самое слабое звено мистер {} {} с квалификацией ({})".format(loose.name, loose.surname, loose.level))
print('До свидания мистер {}'.format(loose.__del__()))
input()

########################################################################################################################
print('\n****************** task 4 ******************\n')


class Variors:
    id = 1

    def __init__(self):
        self.id = Variors.id
        Variors.id += 1


class Soldiers(Variors):

    def __init__(self):
        Variors.__init__(self)

    def __str__(self):
        return f'{self.id}'


class Heroes(Variors):

    def __init__(self, team):
        Variors.__init__(self)
        self.team = team
        self.level = 1

    def level_up(self):
        self.level += 1
        return self.level

    def following_with_hero(self):
        random_follower_id = random.choice(list_team1)
        print(f'Солдат з ID {random_follower_id} прямує за героєм з ID {self.id}')


hero_1 = Heroes('team1')
hero_2 = Heroes('team2')
list_team1 = []
list_team2 = []
for _ in range(50):
    if random.choice(['team1', 'team2']) == 'team1':
        list_team1.append(Soldiers())
    else:
        list_team2.append(Soldiers())

print(f'Солдатів у першого героя - {len(list_team1)}')
print(f'Солдатів у дрогого героя - {len(list_team2)}')
if len(list_team1) > len(list_team2):
    hero_1.level_up()
else:
    hero_2.level_up()

hero_1.following_with_hero()

########################################################################################################################

print('\n****************** task 5 ******************\n')

class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return A(self.x + other.x, self.y + other.y)
    def __str__(self):
        return '{}, {}'.format(self.x, self.y)


########################################################################################################################

print('\n****************** task 6 ******************\n')


class Table:
    def __init__(self, type, width, length, height, weight):
        self.type = type
        self.__width = width
        self.__length = length
        self.__height = height
        self.__weight = weight

    def __get__(self, n):
        getattr(self, f'{Table}{n}')

    def __set__(self, atr, val):
        setattr(self, f'{Table}__{atr}', val)

# ########################################################################################################################

print('\n****************** task 7 ******************\n')


class WinDoor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square_win_door(self):
        return self.x * self.y


class Room:
    def __init__(self, width, lenght, height):
        self.width = width
        self.lenght = lenght
        self.height = height
        self.wd = []

    def oll_surface(self):
        return 2 * self.height * (self.width + self.lenght)

    def add_wd(self, w, h):
        self.wd.append(WinDoor(w, h))

    def work_surface(self):
        new_square = self.oll_surface()
        for i in self.wd:
            new_square -= i.square_win_door()
        return new_square

    def count_roll(self, w=1, h=10):
        self.roll_square = w * h
        return self.work_surface() / self.roll_square
########################################################################################################################

print('\n****************** task 8 ******************\n')

class Snow:
    def __init__(self, amount):
        self.snow_amount = amount

    def add(self, n):
        self.snow_amount += n
        return self.snow_amount

    def sub(self, n):
        self.snow_amount -= n
        return self.snow_amount

    def mul(self, n):
        self.snow_amount *= n
        return self.snow_amount

    def truediv(self, n):
        self.snow_amount /= n
        return round(self.snow_amount)

    def call(self, new_quantity):
        self.quantity_of_snowflakes = new_quantity
        return self.quantity_of_snowflakes
    def make_snow(self, snow_amount_in_a_row):
        string_of_snowfall = ""
        amount_of_rows = int(self.snow_amount) // snow_amount_in_a_row
        for i in range(amount_of_rows):
            string_of_snowfall += ("*" * snow_amount_in_a_row)
            string_of_snowfall += "\n"
        remain_snowflakes = (int(self.snow_amount) - amount_of_rows * snow_amount_in_a_row)
        string_of_snowfall += "*" * remain_snowflakes
        return string_of_snowfall

########################################################################################################################
print('\n****************** task 9 ******************\n')

print("Enter the width of the room:")
w_room = int(input())
print("Enter the length of the room:")
l_room = int(input())
print("Enter the height of the room:")
h_room = int(input())
r1 = Room(w_room, l_room, h_room)
print("Enter the number of windows and doors together:")
n = int(input())
for i in range(1, n+1):
    print("Enter the width and length of the {} window /0 door through the space:".format(i))
    w_win_door, l_win_door = map(int, input().split())
    r1.addWD(w_win_door, l_win_door)
print("The area of the work surface: {}".format(r1.workSurface()))
print("Number of rolls required: {}".format(r1.countRoll()))

########################################################################################################################

print('\n****************** task 10 ******************\n')


print('\n****************** task 11 ******************\n')

import random

class Data:
    def __init__(self, *info):
        self.info = list(info)
    def __getitem__(self, i):
        return self.info[i]

class Teacher:
    def __init__(self):
        self.work = 0
    def teach(self, info, *pupil):
        for i in pupil:
            i.take(info)
            self.work += 1

class Pupil:
    def __init__(self):
        self.knowledge = []
    def take(self, info):
        return self.knowledge.append(info)
    def forgot(self):
        index = random.randint(0, len(self.knowledge)-1)
        del self.knowledge[index]

lesson = Data('class', 'object', 'inheritance', 'polymorphism','encapsulation')
marIvanna = Teacher()
vasy = Pupil()
pety = Pupil()
marIvanna.teach(lesson[2], vasy, pety)
marIvanna.teach(lesson[0], pety)
print(vasy.knowledge)
print(pety.knowledge)
pety.forgot()
pety.take(lesson[4])
print(pety.knowledge)


print('\n****************** task 14 ******************\n')
import random

class Simple_iterator:
    def __init__(self, amount, left_border, right_border):
        self.amount = amount
        self.left_borded = left_border
        self.right_border = right_border

    def next(self):
        lst_of_random_meaning = []
        for i in range(self.amount):
            i = random.randint(self.left_borded, self.right_border)
            lst_of_random_meaning.append(i)
        return  lst_of_random_meaning


iterator1 = Simple_iterator(4, 10, 20)
print(iterator1.next())

print('\n****************** task 15 ******************\n')

import random

def simple_generator(amount, left_border, right_border):
    lst_of_random_meaning = [random.randint(left_border, right_border) for i in range(amount)]
    return  lst_of_random_meaning

print(simple_generator(9,1,20))