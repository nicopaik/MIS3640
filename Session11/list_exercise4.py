#4.1 
random = dict()
def create_dict():
    f = open('Session11/words.txt')

    for line in f:
        words = line.strip()
        random[words] = words
    return random



test_dict = create_dict()
def check_dict(text, dict):
    if text in dict:
        return True
    else:
        return False

print(check_dict('text', test_dict))



#4.2
def dupli(text, dict):
    if len(text) > len(set(dict)):
        return True
    return False


print(dupli('test1', test_dict))
