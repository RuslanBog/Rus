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


case = input("Кинь кубик:") # результат всегда str!!
case = int(case)
print(case)
if case == 6:
    print("Pobedil Vasya")
elif case == 1:
    print("Pobedil Petya")
else:
    print("Proigrali vse))")