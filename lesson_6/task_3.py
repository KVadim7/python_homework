numbers_list = [x for x in range(1, 101)]
print(numbers_list)

extracted_list = list()
i = 0

while i < 100:
    if numbers_list[i] % 7 == 0 and numbers_list[i] % 5 != 0:
        extracted_list.append(numbers_list[i])
    i += 1
print(extracted_list)





