import random
first_lst = random.sample(range(1, 20), 10)
print(first_lst)

max_num = 0
index = 0

while index < 10:
    if first_lst[index] > max_num:
        max_num = first_lst[index]
    index += 1
print(max_num)
