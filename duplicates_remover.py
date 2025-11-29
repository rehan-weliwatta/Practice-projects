list_with_dups = [2 , 2, 2, 5 , 6 , 7 , 8, 8, 8, 9]
new_list = []

for number in list_with_dups:
    if number not in new_list:
        new_list.append(number)

print(f"New list without Duplicates :{new_list}")