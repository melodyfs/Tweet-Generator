from random import shuffle
import sys

def rearrange_word(a, b, c, d):
    list_ = [a, b, c, d]
    shuffle(list_)
    return ' '.join(list_)
    # return list_


if __name__ == "__main__":
    params = sys.argv
    a = str(params[1])
    b = str(params[2])
    c = str(params[3])
    d = str(params[4])
    word = rearrange_word(a, b, c, d)
    print word
