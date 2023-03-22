import random

list_1 = list()
list_2 = list()

lists_len = 10
index = 0

while index < lists_len:
    list_1.append(random.randint(1, lists_len))
    list_2.append(random.randint(1, lists_len))
    index += 1
print(list_1)
print(list_2)


common_list = list()
index = 0
while index < 10:
    if list_1[index] in list_2 and not list_1[index] in common_list:
        common_list.append(list_1[index])
    index += 1
print(common_list)

