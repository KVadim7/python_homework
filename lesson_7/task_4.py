list_days = "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"

list_week = [day for day in list_days]
print(list_week)
dict_week1 = {i: j for i, j in enumerate(list_days, start=1)}
print(dict_week1)

k = range(1, len(list_days))
dict_week2 = {i: j for i, j in zip(list_days, k)}
print(dict_week2)
