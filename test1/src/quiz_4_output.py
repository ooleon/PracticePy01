list_nums=[4, 3, 2, 1]
sorted_list=list_nums.sort()
no_values=None if all(list_nums) else list_nums
print(sorted_list==no_values)
print(no_values)