import sys
import re



with open('dorian.txt') as f:
    original_text = f.read()
    f.close

def histogram(source_text):
    clean_text = source_text.replace("\n", "").replace("\r", "")
    split_text = re.split(' ', clean_text)

    histogram = {}

    for text in split_text:
        if text in histogram:
            histogram[text] += 1
        else:
            histogram[text] = 1
    return histogram
    print histogram

def unique_words(histogram):
    count = 0

    for word in histogram:
        count += 1
    print count

def frequency(word, histogram):
    frequency = 0

    for word_ in histogram:
        if word_ == word:
            frequency = histogram[word_]

    return frequency

his = histogram(original_text)
# print(his)
# unique_words(his)
frequency("sit", his)
