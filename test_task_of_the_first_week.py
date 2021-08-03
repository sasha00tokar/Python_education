from exercise.task_of_the_first_week import multiple_elements, multiple_elements_2, factorial, factorial_2, \
    generate_dict, generate_dict_2, str_to_tuple, str_in_list, up_first_letter, unique_word, binary_digit, \
    calculate_sequence, generate_password, sorted_by_priority, distance_between_points, words_in_text


def test_multiple_elements():
    assert multiple_elements(1, 100) == '7,14,21,28,42,49,56,63,77,84,91,98'


def test_test_multiple_elements_2():
    assert multiple_elements_2(1, 100) == '7,14,21,28,42,49,56,63,77,84,91,98'


def test_factorial():
    assert factorial(6) == 720


def test_factorial_2():
    assert factorial_2(6) == 720


def test_generate_dict():
    assert generate_dict(4) == {1: 1, 2: 4, 3: 9, 4: 16}


def test_generate_dict_2():
    assert generate_dict_2(4) == '112439416'


def test_str_to_tuple():
    assert str_to_tuple('1,2,3,     4,5,6,7,8,9') == ('1', '2', '3', '4', '5', '6', '7', '8', '9')


def test_str_in_list():
    assert str_in_list("Hello,world,how,are,you") == ['are', 'hello', 'how', 'world', 'you']


def test_up_first_letter():
    assert up_first_letter(["hello world how are you", "i\'m fine and you"]) == \
           "Hello World How Are You\nI'm Fine And You\n"


def test_unique_word():
    assert unique_word('hello world world how are you') == ['hello', 'world', 'how', 'are', 'you']


def test_binary_digit():
    assert binary_digit("1100,1101,1111,10100") == '1111,10100'  # 12,13,15,20


def test_calculate_sequence():
    assert calculate_sequence(3) == 3702


def test_generate_password():
    assert generate_password('11kTFD5@#1#') is True
    assert generate_password('1111111') is False


def test_sorted_by_priority():
    assert sorted_by_priority([('Max', 18, 100), ('Anton', 23, 101), ('Max', 19, 100), ('Max', 18, 90)]) == \
           [('Anton', 23, 101), ('Max', 18, 90), ('Max', 18, 100), ('Max', 19, 100)]


def test_distance_between_points():
    assert distance_between_points(['1 UP', '2 LEFT', '3 DOWN, 4 RIGHT']) == 2.24
    assert distance_between_points(['1 UP', '1 RIGHT']) == 1.41
    assert distance_between_points(['7 UP', '1 LEFT', '3 DOWN, 3 RIGHT']) == 7.07


def test_words_in_text():
    assert words_in_text('bb bb. cc cc, aa cc') == [('aa', 1), ('bb', 2), ('cc', 3)]
