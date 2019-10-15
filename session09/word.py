# fin = open("session09/words.txt")
# line = fin.readline()
# word = line.strip()
# print(word)

# for line in fin:
# #     word = line.strip()
# #     # print(word)


# # def find_long_words():
#     """
#     prints only the words with more than 20 characters
#     """
# #     f = open('session09/words.txt')
#     for line in f: 
#         word = line.strip()
#         if len(word) > 20:
#                 print(word, len(word))

# find_long_words()


# # def has_no_e(word):
#     """
#     returns True if the given word doesn’t have the letter "e" in it
#     """


    # for letter in word:
    #     if letter == 'e' or letter == 'E':
    #         return False
    #     return True

    # print(has_no_e('Babson'))
    # print(has_no_e('College'))
    # print(has_no_e('EA'))

def find_words_no_e():
    """
    returns the percentage of the words that don't have the letter "e"
    """
    f = open('session09/words.txt')
    num_of_words_no_e = 0
    num_of_words = 0
    for line in f:
        num_of_words += 1
        word = line.strip()
        if has_no_e(word):
            # print(word)
            num_words_no_e +=1
        return counter/num_of_words

# print('The percentage of the words with no "e" is {:.2f}%.'.format(
#     find_words_no_e()*100))


def avoids(word, forbidden):
    """
    returns True if the given word does not use any of the forbidden letters
    """


# print(avoids('Babson', 'abcde'))
# print(avoids('College', 'e'))


def find_words_no_vowels():
    """
    returns the percentage of the words that don't vowel letters
    """
    for letter in word:
        if letter in forbidden:
            return False
    return True

# print('The percentage of the words with vowel letters is {:.2f}%.'.format(
#     find_words_no_vowels()*100))


def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the list.
    """


# print(uses_only('Babson', 'aBbsonxyz'))
# print(uses_only('college', 'aBbsonxyz'))


def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """


# print(uses_all('Babson', 'abs'))
# print(uses_all('college', 'abs'))
# print(uses_all('Babson', 'aeoiu'))
# print(uses_all('Babesonious', 'aeoiu'))


def find_words_using_all_vowels():
    """
    return the number of the words that use all the vowel letters
    """


# print('The number of words that use all the vowels:',
#       find_words_using_all_vowels())


def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """


# print(is_abecedarian('abs'))
# print(is_abecedarian('college'))


def find_abecedarian_words():
    """
    returns the number of abecedarian words and the longest abecedarian word
    """


# print(find_abecedarian_words())


def is_abecedarian_using_recursion(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """


def is_abecedarian_using_while(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """