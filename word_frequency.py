import sys
import re



with open('dorian.txt') as f:
    original_text = f.read()
    f.close

def histogram(source_text):
    split_text = re.split(' ', source_text)

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
    print frequency

his = histogram("one fish two fish red fish blue fish")
# unique_words(his)
frequency("fish", his)
