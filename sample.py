import random
import time
from word_frequency import histogram_dict
import codecs


with codecs.open('dorian.txt',encoding='utf-8', errors='ignore') as f:
    original_text = f.read()


def get_probability(histogram):
    total = sum(histogram.values())
    probabilities = {}

    for word in histogram:
        probabilities[word] = float(histogram[word]) / float(total)
    return probabilities


def sample(probabilities, histogram):
    random_num = random.random()
    print("ran num: %s" % random_num)

    prob = 0
    for i in probabilities:
        prob += probabilities[i]
        if random_num < prob:
            print("prob: %s" % probabilities[i])
            return i


start_time = time.time()
his = histogram_dict(original_text)
his = histogram_dict(original_text)
print(his)
p = get_probability(his)
s = sample(p, his)
end_time = time.time() - start_time
print his
print("W: %s" % s)
print(end_time)


# 1. Key Features: Generate histogram of dict, get the token for type
# 2. Names of modules, variables and files are named after their functionality
# 3. No global variables.
# 4. Each function has a few lines of code instead of a big chunk
# 5. By placing all the funcs(methods) in a class, the code could be more organized
# 6. Files can be used as both modules and scripts. Adding <if __name__ = __"main"__> at
#    of file can achieve that
# 7. Modules can be used dependently. E.g. from word_frequency import histogram_dict
