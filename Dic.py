import pandas as pd
def build_word_frequency(data):
    top_n_dictionary = {}

    # Process each row in data
    for i in range(0, len(data)):
        # The data in comment_final is list: [wtf, confirm..], first position is "["
        string_list = data.iloc[i]['comment_final'][1:-1]  # remove [ & ]
        string = string_list.encode("utf-8")  # change list to string and encode: from "unicode" to "utf-8"
        splited_string = string.split(", ")  # split string
        for word in splited_string:
            if word in top_n_dictionary:

                top_n_dictionary[word] += 1
            else:
                top_n_dictionary[word] = 1
    return top_n_dictionary



data = pd.read_csv("../Cleanings_1/Bodian-122920-CleanComment.csv", encoding="UTF8")
dic1 = build_word_frequency(data)
corups = [dic1.keys()]
total_list = corups[0][1:]