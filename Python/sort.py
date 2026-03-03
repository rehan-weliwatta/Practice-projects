unsorted_list = [1, 5, 3, 7, 2, 8, 6, 9]

for j in range(len(unsorted_list)):
    for i in range(len(unsorted_list)- 1 -j):
        if unsorted_list[i] > unsorted_list[i+1]:
            unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1] , unsorted_list[i]

print(unsorted_list)