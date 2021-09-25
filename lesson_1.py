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
case = 1
result = "qwe"
print(f"Выпало число: {case} с результатом: {result} ")

dir_name = "home"
file_name = "test.py"
path = f"{dir_name}/{file_name}"
print(path)

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
my_str_1 = "IIIII'm Qwerty"
# index = 5
# new_str = my_str_1[: index] + "K" + my_str_1[index + 1 :]
# print(new_str)

# for symbol in my_str_1:
#     if (symbol.lower() not in "eyuioa") and symbol.isupper():
#         print(symbol)

# for symbol in my_str_1:
#     print(f"symbol '{symbol}' --> {ord(symbol)}")

for index in range(ord(' '), ord('z') + 1, 2):
    print(f"index '{index}' --> '{chr(index)}'")