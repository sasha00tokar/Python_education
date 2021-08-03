from collections import Counter
from operator import itemgetter
import re


print('****************** task 1 ******************\n')
# 1. написати програму, яка буде знаходити всі числа кратні 7 але не кратні 5,
# не менше 1000 і не більше 3100. Результат вивести через кому в один рядом.


def multiple_elements(n, m):
    multiple_elements = []
    for element in range(n, m):
        if element % 7 == 0 and element % 5 != 0:
            multiple_elements.append(element)
    return ','.join(map(str, multiple_elements))

########################################################################################################################


print('\n****************** task 2 ******************\n')
# 2. написати те ж що в №1, але в 1 рядок( без використання eval


def multiple_elements_2(n, m):
    return ','.join(map(str, [x for x in range(n, m) if x % 7 == 0 and x % 5 != 0]))

########################################################################################################################


print('\n****************** task 3 ******************\n')
# 3. написати функцію, яка буде знаходити факторіал числа.


def factorial(n):
    fac = 1
    for i in range(1, n+1):
        fac *= i
    return fac


########################################################################################################################


print('\n****************** task 4 ******************\n')
# 4. те ж саме, але без рекурсії ( з рекурсією, якщо зробили без рекурсії ).
# рекурсивною функцією знайти факторіал числа 105.


def factorial_2(n):
    if n == 1:
        return n
    else:
        return n * factorial_2(n-1)


print(factorial_2(105))

########################################################################################################################


print('\n****************** task 5 ******************\n')
# 5. написати функцію, яка при заданому n буде
# генерувати dict вигляду {i: i^2, ...}, де і від 1 до n.


def generate_dict(n):
    return {i: i**2 for i in range(1, n+1)}

########################################################################################################################


print('\n****************** task 6 ******************\n')
# 6. написати те ж що в №5, але генерація в 1 рядок


def generate_dict_2(n):
    return ''.join([str(i) + str(i**2) for i in range(1, n+1)])

########################################################################################################################


print('\n****************** task 7 ******************\n')
# 7. написати функцію, яка отримує аргумент типу string з числами
# через кому (можливі пробіли(space)), а на виході видає tuple цих чисел


def str_to_tuple(num_str):
    num_list = []
    for i in ''.join(num_str.split()).split(','):
        num_list.append(i)
    return tuple(num_list)

########################################################################################################################


print('\n****************** task 8 ******************\n')
# 8. написати функцію, яка приймає string зі словами через кому,
# а повертає список із словами відсортованими в алфавітному порядку


def str_in_list(words_str):
    return sorted([x.lower() for x in ''.join(words_str.split()).split(',')])

########################################################################################################################


print('\n****************** task 9 ******************\n')
# 9. написати функцію, яка приймає список текстових рядків
# (list[str]) і виводить кожен рядок, роблячи кожну першу букву слова великою


def up_first_letter(txt_list):
    return str(''.join([' '.join([x[0].upper() + x[1:] for x in line.split()]) + '\n' for line in txt_list]))

########################################################################################################################


print('\n****************** task 10 ******************\n')
# 10. написати функцію, яка приймає string зі словами, розділеними
# пробілами (одним чи більше) і повертає список із унікальними словами


def unique_word(str_word):
    unique_list = []
    for el in str_word.split():
        if el not in unique_list:
            unique_list.append(el)
    return unique_list

########################################################################################################################


print('\n****************** task 11 ******************\n')
# 11. написати програму, яка приймає string із бінарними числами,
# розділеними комою, і повертає тільки ті, які діляться на 5


def binary_digit(str_number):
    return ','.join([x for x in str_number.split(',') if int(x, 2) % 5 == 0])

########################################################################################################################


print('\n****************** task 12 ******************\n')
# 12. написати функцію, яка обчислює a+aa+aaa+ aaaa при заданому а.
# приклад, а=1 -- 1+11+111+1111


def calculate_sequence(num):
    added_sequence = 0
    for element in range(1, 5):
        intermediate_str = ''
        for i in range(element):
            intermediate_str += str(num)
        added_sequence += int(intermediate_str)
    return added_sequence

########################################################################################################################


print('\n****************** task 13 ******************\n')
# 13. написати функцію, яка перевіряє пароль на відповідність правилам:
#    1. At least 1 letter between [a-z]
#    2. At least 1 number between [0-9]
#    1. At least 1 letter between [A-Z]
#    3. At least 1 character from [$#@]
#    4. Minimum length of transaction password: 6
#    5. Maximum length of transaction password: 12


def generate_password(symb_str):
    if all([re.findall('[A-Z]', symb_str), re.findall('[a-z]', symb_str),
            re.findall('[0-9]', symb_str), re.findall('[$#@]', symb_str),
            6 <= len(symb_str) <= 12]):
        return True
    else:
        return False

########################################################################################################################


print('\n****************** task 14 ******************\n')
# 14. написати функцію, яка буде сортувати tuple із 3х значень.
# tuple вигляду (імя, вік, та рейтийнг). Пріорітет сортування - по імені, потім по віку, потім по рейтингу.


def sorted_by_priority(list_for_sort):
    return sorted(sorted(sorted(list_for_sort, key=itemgetter(2)), key=itemgetter(1)), key=itemgetter(0))

########################################################################################################################


print('\n****************** task 15 ******************\n')
# 15. На вході функція отримує список strings із переміщеннями робота
# вигляду "1 UP", "2 LEFT", "3 DOWN", і т.д. робот може рухатись
# тільки в 4 сторони(UP,DOWN,LEFT,RIGHT). функція повинна повертати
# відстань між початковою і кінцевою точками робота.


def distance_between_points(moving_robot_list):
    x_axis = 0
    y_axis = 0
    for direction in range(len(moving_robot_list)):
        sides_direction_list = list(moving_robot_list[direction].split())
        if sides_direction_list[1] == 'UP':
            y_axis += int(sides_direction_list[0])
        elif sides_direction_list[1] == 'DOWN':
            y_axis -= int(sides_direction_list[0])
        elif sides_direction_list[1] == 'RIGHT':
            x_axis += int(sides_direction_list[0])
        elif sides_direction_list[1] == 'LEFT':
            x_axis -= int(sides_direction_list[0])
    return round((x_axis * x_axis + y_axis * y_axis)**0.5, 2)

########################################################################################################################


print('\n****************** task 16 ******************\n')
# 16. Написати функцію, яка буде рахувати частоту використання слів у тексті.
# Функція повинна роздрукувати слова і частоту в алфавітному порядку.


def words_in_text(text_str):
    word_in_order = []
    for key, value in sorted(list(Counter(text_str.replace('.', ' ').replace(',', ' ').split()).items())):
        word_in_order.append((key, value))
    return word_in_order


print('\n****************** END ******************\n')
