word = input("Enter a word :").upper()
char_list = []

## first method

if word == word[::-1]:
    print("You entered a palindrome word")

else:
    print("You entered a non-palindrome word")

## second method
for i in word:
    char_list.append(i)

reversed_list = char_list[::-1]

if reversed_list == char_list:
    print("You entered a palindrome word")

else:
    print("You entered a non-palindrome word")
 