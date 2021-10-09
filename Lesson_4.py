# 1)
# my_str = "blablacar"
# my_symbol = "bla"
# result = my_str.count(my_symbol)
# print(result)

# 2)
# my_str = "blablacar"
# my_symbol = "bla"
# my_symbol_count = my_str.count(my_symbol)
# result = f"{my_symbol}\n" * my_symbol_count
# result = result.strip()
# print(result)

# 3)
# my_str = "bla BLA car"
# lower_str = my_str.lower()
# unique_symbols = []
#
# for symbol in lower_str:
#     if symbol not in unique_symbols
#
# print(unique_symbols_count) не закончено#########

# 4)
# my_str = "zdfdxchzgxjch"
# my_list = [111]
# print(id(my_list), my_list)
# new_str = my_str[::2]
# for symbol in new_str:
#     my_list.append(symbol)
# print(id(my_list), my_list)

# 5)
# from string import ascii_lowercase as alphabet
# my_str = alphabet
# str_index = [6, 5, 7, 7, 1, 4, 2, 3, 7, 3]
# my_list = []
# for index in str_index:
#     symbol = my_str[index]
#     my_list.append(symbol)
# print(my_list)

# 6)

# number = 12346574132165467481321
# digit_count = len(str(number))
# print(digit_count)

# 7)
# number = 12346574132165467481321
# max_symbol = max(str(number))
# print(max_symbol)

# 8)
# number = 12346574132165467481321
# numb_str = str(number)
# result_number = int(numb_str[::-1])
# # result_number = int(str(numb_str[::-1])) доделать
# print(result_number)

# 9)

# number = 1234657413216546748132100000
# numb_str = str(number)
# sort_numb_list = sorted(numb_str, reverse=True)
# new_number = "".join(sort_numb_list)
# result = int(new_number)
# print(result)

# my_list = [3, 6, 1, 8]
# # my_list
# my_list.sort()
# print(my_list)

# 10)

# my_list_1 = [1, 2, 3]
# my_list_2 = [10, 20, 30]
# my_result = []
#
# for index in range(len(my_list_1)):
#     my_result.append(my_list_1[index])
#     my_result.append(my_list_2[index])
# print(my_result)

# генератор списков ###################################
# множество ###########################################
# ord(), chr()

# функция ord
# print(ord("a"))
# print(chr(34))

# генератор списков (list comprehension)

# alphabet_list = []
# for index_ascii in range(ord('a'), ord('z') + 1):
#     alphabet_list.append(chr(index_ascii))
####################
# alphabet_list = [chr(index_ascii) for index_ascii in range(ord('a'), ord('z') + 1)]
#
# alphabet = "".join(alphabet_list)
# print(alphabet)
################################
# result = [x ** 2 for x in range(10)]
# print(result)

# my_list = [12, -45, 23, 5, 0, 21, 900]

# res = []
# for value in my_list:
#     if value < 10:
#         res.append(value)
# res = [value for value in my_list if value < 10]
#
#
# print(res)
 ################# множества (set) - изменяемый тип, толбко один представитель для каждого объекта, порядок не сохраняется

# my_list = [1, 2, 3, 4, 5, 5, 5, "1"]
#
# my_set = set(my_list)
# print(my_set, type(my_set))
####################################
# 3) через set
# my_str = "bla BLA car"
# lower_str = my_str.lower()
#
#
# unique_symbols = set(lower_str) ### порядок не сохраняется
# print(unique_symbols)
#
# unique_symbols_count = len(unique_symbols)
# print(unique_symbols_count)
# #
# print(unique_symbols_count) не закончено#########

# my_list = [1, 2, 3, 4, 5, 5, 5, "1"]
#
# my_set = list(set(my_list)) #убрать дубли в списке
# print(my_set, type(my_set))
####################################

my_str_1 = 'jhgghkgkglkdjdj'
my_str_2 = 'kflsb,xbmnvbjbkjdfbvnb  dfv'
my_str_1_set = set(my_str_1)
my_str_2_set = set(my_str_2)

same_symbol = my_str_1_set.intersection(my_str_2_set)
print(same_symbol)

all_symbols = my_str_1_set.union(my_str_2_set)
print(all_symbols)

first_str_unique = my_str_1_set.difference(my_str_2_set)
print(first_str_unique)