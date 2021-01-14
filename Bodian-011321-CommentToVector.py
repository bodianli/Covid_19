import pandas as pd
import numpy as np
from collections import defaultdict

data = pd.read_csv("Bodian-122920-CleanComment.csv", encoding="UTF8")
print(data.head())


# Change comment_final to the string
def to_string_list(nonstring):
    string_list = nonstring[1:-1]
    string = "".join(string_list).encode("utf-8")
    splited_string = string.split(", ")
    return splited_string


def build_word_frequency(data):
    top_n_dictionary = defaultdict(int)

    # Process each row in data
    for i in range(0, len(data)):
        # The data in comment_final is list: [wtf, confirm..], first position is "["
        string_list = data.iloc[i]['comment_final'][1:-1]  # remove [ & ]
        string = string_list.encode("utf-8")  # change list to string and encode: from "unicode" to "utf-8"
        splited_string = string.split(", ")  # split string
        for word in splited_string:
            top_n_dictionary[word] += 1
    return top_n_dictionary


dic1 = build_word_frequency(data)
corups = [dic1.keys()]
total_list = corups[0][1:]


def generate(sentence):
    bag_vector = np.zeros(len(total_list))
    for w in sentence:
        for i, word in enumerate(total_list):
            if word == w:
                bag_vector[i] += 1
    myarray = np.array(bag_vector)  # Change vector to Array, shape of each array is (10586L,0)
    return myarray


data['comment_final'] = data['comment_final'].apply(lambda x: to_string_list(x))
data['comment_final_vector'] = data['comment_final'].apply(lambda x: generate(x))

df = pd.DataFrame(data=data['comment_final_vector'], columns=total_list)

# Create a empty array
empty_array = []

# Append empty array with each row of data
for i in range(0, len(data)):
    empty_array.append(data.iloc[i]['comment_final_vector'])

# Change empty_array to dataframe for saving
df = pd.DataFrame(data=empty_array, columns=total_list)
df['y'] = data['y']

df.to_csv("Bodian-111321-Premodel.csv", encoding="UTF8", index=False)

#
# for i in range(5):
#     arr = data.iloc[i]['comment_final_vector']
#
#     df = df.append(arr)
#
#
# print df.head()
#
# #
# #
# # finalist = array_to_df(data['comment_final_vector'])
# # finalist.to_csv("Boel.csv", encoding="UTF8", index=False)
# #
#
# #
# # print data['comment_final_vector'][1]
#
# # print len(data['comment_final_vector'][1])
#
# #
# data[['comment_final_vector', 'y']].to_csv("Bodian-111121-Premodel.csv", encoding="UTF8", index=False)
#
#
#
#
#
#
# df2 = pd.DataFrame(myarray, columns=total_list)
#
#
#

'''
def word_of_bag(data):
    dic = build_word_frequency(data)
    corups = []
    corups.append(dic.keys())
    total_list = corups[0][1:]
    empty_array = np.empty((len(data), len(total_list)), dtype=float, order='C')
    print empty_array.shape

    for i in range(0, 5):
        # Create Bag Vector of Zero, shape(0,15566)
        bag_vector = np.zeros(len(total_list))
        # Split data in `comment_final`
        string_list = data.iloc[i]['comment_final'][1:-1]  # remove [ & ]
        string = "".join(string_list).encode("utf-8")  # change list to string and encode: from "unicode" to "utf-8"
        splited_string = string.split(", ")  # split string
        print splited_string

        # iltera each vocabulary in string
        for w in splited_string:
            # ilter each vocabulary in dictionary and related index
            print w
            for i, word in enumerate(total_list):
                if word == w:
                    bag_vector[i] += 1

        np.append(empty_array, np.array(bag_vector), axis=0)

    return empty_array

# print (word_of_bag(data))
'''
