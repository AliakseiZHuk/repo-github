from time import perf_counter

my_list = [randint(-10, 10) for _ in range(20)]

uniq_list = [el for el in my_list if my_list.count(el) == 1]
print(uniq_list)