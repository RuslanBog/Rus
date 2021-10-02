# value = "0"
# new_value = bool (value)
# print (new_value, type (new_value))



# some_value = 4
#
# bool_value_1 = (2 == some_value)
# bool_value_1 = (2 != some_value)
#
# # bool_value_2 = ("q" in "q.werty")
# bool_value = not bool_value_1
# print(bool_value, type(bool_value))






# value_1 = "25"
# value_2 = "2"

# value = value_1 / value_2 # обычное деление
# value = value_1 // value_2 # целочисленное деление (без округления)
# value = value_1 % value_2 # остаток от деления
# value = value_1 ** value_2 # возведение в степень. Корень для ** 0.5
# value = value_1 + value_2
# print(value) #, type(value))

# value = "100"
# value = 100
# print(value, type(value))

# first = "qwe"
# second = 1
# value = first
# first = second
# second = value

# first, second = second, first


# print("Hello, World!")
# # comment
# print("Hello, World!")
# print('Hello!')
#
#
# print(123 * 2, 456, 789, "qwe")
# print(12 - 3)
# print(23 + 5 * 10)


# lesson 2
# приведение типов
# value = 0.0
# value_bool = bool(value)
# print(value_bool)
#############################################################################

# if условие:
#     блок, если Да
# else:
#     блок, если Нет


# temp = 0.1
#
# if temp > 0:
#     print("Можно шапку не надевать")
# else:
#     print("Надень шапку!")


# case = input("Кинь кубик:") # результат всегда str!!
# case = int(case)
# print(case)
# if case == 6:
#     print("Pobedil Vasya")
# elif case == 1:
#     print("Pobedil Petya")
# else:
#     print("Proigrali vse))")


#тернарный оператор
# if case > 3:
#     result = case ** 2
# else:
#     result = - case

# from random import randint
# case  = randint(1, 6)
#
# result = case ** 2 if case > 3 else - case
#
# print("Выпало число:", case, "Результат:", result)
#################################
# Строки и методы строк
# case = 1
# result = "qwe"
# print(f"Выпало число: {case} с результатом: {result} ")
#
# dir_name = "home"
# file_name = "test.py"
# path = f"{dir_name}/{file_name}"
# print(path)

# # литералы
# my_str_1 = "I'm Qwerty"
# my_str_2 = "I'm Qwerty"
# my_str_3 = "I'm Qwerty"
# my_str_4 = "I'm Qwerty"
#
# index = -5
# symbol = my_str_1[index]
# print(symbol)

# my_str_1 = "I'm Qwerty"
# my_str_1_len = len(my_str_1)
# print(my_str_1_len, my_str_1[my_str_1_len - 1])

# срез строки
# my_str_1 = "IIIII'm Qwerty"
# index = 5
# new_str = my_str_1[: index] + "K" + my_str_1[index + 1 :]
# print(new_str)

# for symbol in my_str_1:
#     if (symbol.lower() not in "eyuioa") and symbol.isupper():
#         print(symbol)

# for symbol in my_str_1:
#     print(f"symbol '{symbol}' --> {ord(symbol)}")

# for index in range(ord(' '), ord('z') + 1, 2):
#     print(f"index '{index}' --> '{chr(index)}'")
#
# count = 0
# do_loop = True
#
# while count < 10:
#     print("This is while loop", count)

# Угадай число
# Обработка исключений
# Циклы while, for
# Кортежи и списки
############################игра угадай число
# from random import randint
#
# comp_value = randint(1, 10)
# cur_value = int(input("Угадай число от 1 до 10:"))
# go_game = True
# while go_game:
#     if cur_value > comp_value:
#         cur_value = int(input("Попробуй число меньше"))
#     elif cur_value < comp_value:
#         cur_value = int(input("Попробуй число больше"))
#     else:
#         go_game = False
#         print("Победа")
#
# from random import randint
#
# min_limit = 10
# max_limit = 20
# comp_value = randint(min_limit, max_limit)
# cur_value = int(input(f"Угадай число от {min_limit} до {max_limit}:"))
# go_game = True
# while cur_value != comp_value:
#     if cur_value > comp_value:
#         cur_value = int(input("Попробуй число меньше"))
#     elif cur_value < comp_value:
#         cur_value = int(input("Попробуй число больше"))
#     else:
#         go_game = False
# print("Победа")

################################## обработка исключений
# value = input("Введите целое число:")
#
# try:
#     value_int = int(value)
#     result = 1 / value_int
#     print(result)
# except ValueError:
#     print("Это не число!")
# except ZeroDivisionError:
#     print("На ноль делить нельзя!")
###########################################циклы

# for  врем_перем in итер_объект:
#     итерация

# my_str = "qwerty 123 %$# ASD"
#
# for symbol in my_str:
#     if symbol.isalnum()and symbol != " ":
#         print(symbol)
######################################### кортежи и списки
# итерируемые объекты

# my_tuple = (1, -10, "qwe", True, 3.14, (-2, 0), ["a", 'z'])
#
# my_list = [1, -10, "qwe", True, 3.14, (-2, 0), ["a", 'z']]

# print(my_tuple, type(my_tuple))
# print(my_list, type(my_list))
#
# index = 5
# print(my_tuple[index], my_list[index])
# print(len(my_tuple))
# срезы как у строк
# new_list = my_list[:: -1]
# print(new_list)

# for value in my_list:
#     if type(value) == int:
#         print(value)
################################################################ отличия!!
# my_tuple = (1, -10, "qwe", True, 3.14, (-2, 0), ["a", 'z']) #не изменяемый тип
# my_list = [1, -10, "qwe", True, 3.14, (-2, 0), ["a", 'z']] #изменяемый тип данных
#
# my_list[0] = 100
# print(my_list)
#
# my_tuple = (100, *my_tuple[1:])
# print(my_tuple)

############################распаковка кортежей и списков
# my_tuple = (1, 2, "qwe")
# val_int_1, val_int_2, my_str = my_tuple
# print( val_int_1, my_str * 2)

# my_tuple = (1, (-2, 0), ["a", 'z']) #не изменяемый тип
# my_list = [1, (-2, 0), ["a", 'z']]
# my_tuple[-1][0] = 100
# print(my_tuple)

# my_tuple = (1, 2, 3)
# print(id(my_tuple))
# my_tuple = (100, *my_tuple[1:])
# print(id(my_tuple))

# list_1 = [1, 2]
# list_2 = [3, 4]
#
# new_list = [list_1.copy(), list_2]
# print(new_list)
#
# list_1[0] = 100
# list_2[0] = 300
# print(new_list, list_1)

# value = [10, 20]
# new_list = [value.copy()] * 5
# value[0] = 100
# print(new_list)
# print(value)

####################################
# new_list = []
#
# for symbol in "qwerty":
#     new_list.append(symbol)
# new_list.append(1000)
# print(new_list)
#
# result = new_list.pop(0)
# print(new_list)
# print(result)

# new_list = list("new_tuple")
# print(new_list)
#
# new_str = "   ".join(new_list)
# print(new_str)

filename = 'lesson_3.py.txt'
# filename = filename.replace("txt", "")

# filename_parts = filename.split(".")
# filename = ".".join(filename_parts[:-1])
filename = filename.rsplit(".", 1)[0]
print(filename)