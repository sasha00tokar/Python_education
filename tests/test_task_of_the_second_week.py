from exercise.task_of_the_second_week import Warrior, Heroes, A, WinDoor, Room, Snow, Data, Pupil, Teacher


def test_kick():
    unit = Warrior()
    unit.health(100)
    Warrior.kick(unit)
    assert unit.health_amount == 80


def test_level_up():
    hero_1 = Heroes('team1')
    hero_1.level_up()
    assert hero_1.level == 2


def test___add__():
    p1 = A(1, 2)
    p2 = A(3, 4)
    assert isinstance(p1+p2, A) is True


def test_square_win_door():
    height_weight = WinDoor(4, 3)
    assert height_weight.square_win_door() == 12


def test_oll_surface():
    room_1 = Room(1, 2, 3)
    assert room_1.oll_surface() == 18


def test_work_surface():
    room_1 = Room(1, 2, 3)
    room_1.add_wd(1, 2)
    assert room_1.work_surface() == 16


def test_count_rool():
    room_1 = Room(1, 2, 3)
    room_1.add_wd(1, 2)
    assert room_1.count_roll() == 1.6


def test_add():
    snow = Snow(5)
    assert snow.add(2) == 7


def test_sub():
    snow = Snow(5)
    assert snow.sub(2) == 3


def test_mul():
    snow = Snow(5)
    assert snow.mul(2) == 10


def test_truediv():
    snow_1 = Snow(5)
    snow_2 = Snow(7)
    snow_3 = Snow(19)
    assert snow_1.truediv(2) == 2
    assert snow_2.truediv(2) == 4
    assert snow_3.truediv(2) == 10


def test_call():
    snow_1 = Snow(5)
    assert snow_1.call(6) == 6

def test_make_snow():
    snow_1 = Snow(4)
    assert snow_1.make_snow(2) == "**\n**\n"

def test___getitem__():
    data = Data('class', 'object', 'inheritance', 'polymorphism','encapsulation')
    assert data.__getitem__(1) == 'object'


# def test_take():
#     data = Data('class', 'object', 'inheritance', 'polymorphism', 'encapsulation')
#     teacher = Teacher()
#     vasy = Pupil()
#     teacher.teach(data[0], vasy)
#
#     assert vasy.take('object') == ['class', 'object']
