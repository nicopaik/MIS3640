#2.1
text= "This is a text sample!!"

def most_frequent(text):
    text.lower()
    letter_dictionary = {}
    for letter in text:
        if letter.isalpha():
            letter_dictionary[letter] = 1 + letter_dictionary.get(letter, 0)
    result = []
    for key in letter_dictionary:
        result.append((letter_dictionary[key], key))
    result.sort(reverse=True)
    for count, letter in result:
        print(letter, count)

most_frequent(text)

#2.2
list1 = ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled', 'retainers', 'ternaries', 'generating', 'greatening', 'resmelts', 'smelters', 'termless']

def is_anagram(words_list):
    d = {}

    for word in words_list:
        word_key = ''.join(sorted(word)) #adelst
        try:
            d[word_key].append(word)
        except KeyError:
            d[word_key] = [word]

    for key in d:
        print("These words are anagrams:")
        for value in d[key]:
            print(value)
is_anagram(list1)

#2.3
list1 = ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled', 'retainers', 'ternaries', 'generating', 'greatening', 'resmelts', 'smelters', 'termless']

def is_anagram_by_length(words_list):
    d = {}
    result = []
    for word in words_list:
        word_key = ''.join(sorted(word))
        try:
            d[word_key].append(word)
        except KeyError:
            d[word_key] = [word]

    for key in d:
        result.append((len(key), key, d[key]))

    result.sort(reverse=True)

    for length, key, words_list in result:
        print("These words are anagrams:")
        for word in words_list:
            print(word)
            
is_anagram_by_length(list1)