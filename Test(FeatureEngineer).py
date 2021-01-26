import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

# Build Frequencies Dictionary

data = pd.read_csv("Bodian-122920-CleanComment.csv", encoding="UTF8")
# print(data.head(50))


# Calculate frequency of each words
def count_word(string, n):
    # Change list to string format and split each vocabulary
    string_list = str(string).split(", ")

    # Create a dictionary to store top "n" frequency words
    top_n_dictionary = {}

    # Traverse each vocabulary in String_list
    for word in string_list:
        if word in top_n_dictionary:
            top_n_dictionary[word] += 1
        else:
            top_n_dictionary[word] = 1

    # Sorted vocabulary according to frequency
    word_frequency = []
    values = sorted(list(set(top_n_dictionary.values())), reverse=True)  # Calculate frequency of each vocabulary

    for w in values:
        # put vocabulary with same frequency in to a list
        word_list = []
        for k, v in top_n_dictionary.items():
            if v == w:
                word_list.append((k, v))

    # extend list with sorted vocabulary
    word_frequency.extend(sorted(word_list))

    # top n freqnency of vocabulary
    return word_frequency[:n]


def build_word_frequency(data):
    top_n_dictionary = {}

    # Process each row in data
    for i in range(0, len(data)):
        # The data in comment_final is list: [wtf, confirm..], first position is "["
        string_list = data.iloc[i]['comment_final'][1:-1]  # remove [ & ]
        string = "".join(string_list).encode("utf-8")  # change list to string and encode: from "unicode" to "utf-8"
        splited_string = string.split(", ")  # split string
        for word in splited_string:
            if word not in top_n_dictionary:
                top_n_dictionary[word] = 1
            else:
                top_n_dictionary[word] += 1
    return top_n_dictionary


'''
def sorted_frequency(dic, n):
    world_frequency = []
    # sorted values in "dic"
    values = sorted(list(set(dic.values())), reverse=True)

    for w in values:
        word_list = []
        for k, v in dic.items():
            if v == w:
                word_list.append((k, v))
        world_frequency.extend(sorted(word_list))
    return world_frequency[:n]
'''

# Bag of Word

dic1 = build_word_frequency(data)
corups = []
corups.append(dic1.keys())
total_list = corups[0][1:]
# print(total_list)


#
# X = vectorizer.fit_transform(corups)
# print(vectorizer.get_feature_names())
# print(X.toarray())


def word_of_bag(data):
    dic = build_word_frequency(data)
    corups = []
    corups.append(dic.keys())
    total_list = corups[0][1:]
    empty_array = np.empty((len(data), len(total_list)), dtype=float, order='C')

    for i in range(0, 5):
        # Create Bag Vector of Zero, shape(0,15566)
        bag_vector = np.zeros(len(total_list))
        # Split data in `comment_final`
        string_list = data.iloc[i]['comment_final'][1:-1]  # remove [ & ]
        string = "".join(string_list).encode("utf-8")  # change list to string and encode: from "unicode" to "utf-8"
        splited_string = string.split(", ")  # split string

        # iltera each vocabulary in string
        for w in string:
            # ilter each vocabulary in dictionary and related index
            for i, word in enumerate(total_list):
                if word == w:
                    bag_vector[i] += 1

        np.append(empty_array, np.array(bag_vector.T), axis=0)
    return empty_array


# print(word_of_bag(data))

#
#bag_vacter = np.zeros(len(total_list))
#print(bag_vacter.shape)
for i in range(0,5):
    string_list = data.iloc[i]['comment_final'][1:-1]  # remove [ & ]
    string = "".join(string_list).encode("utf-8")  # change list to string and encode: from "unicode" to "utf-8"
    splited_string = string.split(", ")  # split string
    bag_vector = np.zeros(len(total_list))
    for w in splited_string:
        for i, word in enumerate(total_list):
            if word ==w:
                bag_vector[i] +=1
        print(np.array(bag_vector).shape)

