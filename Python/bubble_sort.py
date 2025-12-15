unsorted_list = [9 , 5 , 6 , 7 , 3 , 4 , 1 , 2 , 8]

for j in range(len(unsorted_list)):
    for i in range(len(unsorted_list) - 1 - j):
        if unsorted_list[i] > unsorted_list[i+1]:
            unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1] , unsorted_list[i]

sorted_list = unsorted_list

print(sorted_list)