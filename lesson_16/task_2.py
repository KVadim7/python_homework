class Mathematician:
    @staticmethod
    def square_nums(list_numbers: list):
       return [i ** 2 for i in list_numbers]

    @staticmethod
    def remove_positives(list_numbers: list):
        return [num for num in list_numbers if num < 0]

    @staticmethod
    def filter_leaps(list_years: list):
        return [year for year in list_years if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]


m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
