import random
import string


def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding='UTF8')

    if skip_header == True:
        skip_gutenberg_header(fp)

    strippables = string.punctuation + string.whitespace

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break
        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()
            hist[word] = hist.get(word, 0) + 1

    return hist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):
            break


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    word_counter = 0
    for key in hist:
        word_counter += 1
    
    return word_counter


def most_common(hist):
    """Makes a list of word-freq pairs in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    most_common_list = []
    
    for word in hist:
        most_common_list.append((hist[word], word))
    
    most_common_list.sort(reverse=True)
    
    return most_common_list


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    most_common_list = most_common(hist)
    
    print("The most common words are:")
    for freq, word in most_common_list[:num]:
        print(word, '\t', freq)


def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.
    d1, d2: dictionaries
    """
    d3 = {}
    d1_words = d1.keys()
    d2_words = d2.keys()
    d3_words = []
    for word in d1_words:
        if word not in d2_words:
            d3_words.append(word)
    
    for word in d3_words:
        d3[word] = d1[word]
        
    return d3


def random_word(hist):
    """Chooses a random word from a histogram.
    The probability of each word is proportional to its frequency.
    """
    word_frequency_list = []
    
    for word in hist:
        word_frequency_list += ((word + ',') * hist[word]).split(',')
    
    random_choice = word_frequency_list[random.randint(0, len(word_frequency_list) - 1)]
    
    return random_choice


def main():
    hist = process_file('Session13/Pride and Prejudice.txt', skip_header=True)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[0:20]:
         print(word, '\t', freq)

    words = process_file('Session13/words.txt', skip_header=False)

    diff = subtract(hist, words)
    print("The words in the book that aren't in the word list are:")
    for word in diff.keys():
        print(word, end=' ')

    print("\n\nHere are some random words from the book")
    for i in range(100):
        print(random_word(hist), end=' ')


if __name__ == '__main__':
    main()