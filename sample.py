import random
import time
from word_frequency import histogram_dict

with open('dorian.txt') as f:
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
# his = histogram_dict(original_text)
# print(his)
p = get_probability(his)
s = sample(p, his)
end_time = time.time() - start_time
# print his
print("W: %s" % s)
print end_time
