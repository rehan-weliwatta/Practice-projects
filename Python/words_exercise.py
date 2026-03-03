'''def get_words(words,long_words,f_letter):

    for i in range(5):
        word = input("Enter a Word: ")

        words.append(word)
        if word:
            f_letter.append(word[0])
            if len(word) > 3:
                long_words.append(word)

    print(words)
    print(long_words)
    print(f_letter)

words = []
long_words = []
f_letter = []

get_words(words,long_words,f_letter)'''


def get_words(no_of_times):
    words = []

    for count in range(no_of_times):
        word = input("Enter a word: ")
        words.append(word)

    return words

def filter_by_length(words, min_length):
    return [word for word in words if len(word) > min_length]

def first_letter_of_word(words):
    return [word[0] for word in words ]

def first_letter_multiplied(words):
    return [word[0] * 3 for word in words]

def main():
    words = get_words(5)
    print(filter_by_length(words,3))
    print(first_letter_of_word(words))
    print(first_letter_multiplied(words))

main()