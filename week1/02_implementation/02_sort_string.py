# https://stackoverflow.com/questions/14776980/splitting-list-that-contains-strings-and-integers
# https://needneo.tistory.com/92
# k1ka5cb7


import time

string = input()

start_time = time.time()
sorted_list = sorted(string)

int_list = list(map(int, [x for x in sorted_list if x.isdigit()]))
str_list = [x for x in sorted_list if x.isalpha()]

print(int_list)
print(str_list)

print("".join(str_list)+str(sum(int_list)))

print(time.time() -start_time)