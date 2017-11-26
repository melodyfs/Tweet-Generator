import random
import sys
import time


def random_words(num):
    with open("/usr/share/dict/words") as f:
        original = f.read()
        split_words = original.split()
        f.close()

        words = []

        for w in range(0, num):
            random_num = random.randint(0, len(words))
            words.append(split_words[random_num])
        return(" ".join(words))


if __name__ == "__main__":
    start_time = time.time()
    params = sys.argv
    num = int(params[1])
    print random_words(num)
    end_time = time.time() - start_time
    print(float(end_time))


# random_words()
