
def duplicates(t):

    x = {}
    for a in t:
        if a in x:
            return True
        x[a] = True
    return False


def duplicate(h):
    return len(set(h)) < len(t)