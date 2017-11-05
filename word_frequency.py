import sys
import re
import pdb
import time
import codecs


with codecs.open('dorian.txt',encoding='utf-8', errors='ignore') as f:
    original_text = f.read()


def clean_text(source_text):
    clean_text = source_text.replace("\n", "").replace("\r", "")
    split_text = re.split(' ', clean_text)

    return split_text

def histogram_dict(source_text):
    text_file = clean_text(source_text)
    histogram = {}

    for text in text_file:
        if text in histogram:
            histogram[text] += 1
        else:
            histogram[text] = 1
    return histogram


def histogram_tuple(source_text):
    text_file = clean_text(source_text)

    histogram_tuple = []

    for text in text_file:
        text_ = [x[0] for x in histogram_tuple]

        if text in text_:
            text_index = text_.index(text)
            tup = list(histogram_tuple[text_index])
            tup[1] += 1
            histogram_tuple[text_index] = tuple(tup)
        else:
            histogram_tuple.append((text, 1))

    return histogram_tuple


def histogram_lists(source_text):
    text_file = clean_text(source_text)
    histogram_lists = []

    for word_ in text_file:
        text_arr = [word[0] for word in histogram_lists]

        if word_ in text_arr:
            index = text_arr.index(word_)
            inner_list = histogram_lists[index]
            inner_list[1] += 1

        else:
            histogram_lists.append([word_, 1])

    return histogram_lists

def count_lists(source_text):
    list_of_dict = histogram_dict(source_text)

    unique_word = []
    count_list = []

    for word in list_of_dict:
        # num = [x[1] for x in list_of_dict]
            if list_of_dict[word] in count_list:
                # count_list += list_of_dict
            # list_of_dict[word]
                print(list_of_dict)
            else:
                count_list.append({1: [word]})
    # pdb.set_trace()


    pass


def sort_dict(source_text):
    list_of_dict = histogram_dict(source_text)
    # sort keys alphabetically
    sorted_dict = sorted(list_of_dict.items())


    return sorted_dict



def unique_words(histogram):
    count = 0

    for word in histogram:
        count += 1
    print(count)

def frequency(word, histogram):
    frequency = 0

    for word_ in histogram:
        if word_ == word:
            frequency = histogram[word_]

    return frequency


with open("histogram_entries", 'w') as h:
    histogram_ = histogram_dict("one fish two fish red fish blue fish")
    for key in histogram_:
        h.write("%s %s\n" % (key, histogram_[key]))
    h.close()


# start_time = time.time()
# his = histogram_dict(original_text)
# end_time = time.time() - start_time
# print his
# print end_time
# his = histogram("one fish two fish red fish blue fish")
# print(his)
# unique_words(his)
# frequency("sit", his)
