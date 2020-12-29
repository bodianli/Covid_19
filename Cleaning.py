# Step 2: Remove Stop Words and Non-English Character
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import words
import string
import re
import emoji

data = pd.read_csv("Bodian-122820-CommentAll.csv", encoding="UTF8")

stop_words = set(stopwords.words("english"))
eng_words = set(words.words())


#
# a1 = data['comment'][0]
# print(remove_noneng(a1))


# Func_1: Remove Punctuation
def remove_punc(x):
    non_punct = []
    words_wo_punct = ""

    for w in x:
        if w not in string.punctuation:
            # Punctuation in String Library:  "!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~"
            non_punct.append(w)
    words_no_punct = words_wo_punct.join(non_punct)
    emp_lis_final = "".join(c for c in words_no_punct if c not in emoji.EMOJI_UNICODE)

    ## Second Method
    # non_punct = [w for w i n x if w not in string.punctuation]
    # words_wo_punct = "".join(non_punct)
    # return words_wo_punct

    return emp_lis_final


# Func_2: Remove Number/white space/ non-ASCII characters ex... see link "https://www.utf8-chartable.de/unicode-utf8-table.pl?start=127808&utf8=char"
def remove_number(x):
    text_nonum = re.sub(str("\d+"), " ", x)
    text_nodoublespace = re.sub(str("\s+"), " ", text_nonum).strip()

    encodestring = text_nodoublespace.encode("ascii", "ignore")
    decodestring = encodestring.decode()

    return decodestring


# Func_3: Remove Non-English
def remove_noneng(x):
    emp_lis = " "
    word_punct = nltk.wordpunct_tokenize(x)

    # for w in word_punct:
    #     if w.lower() in eng_words:
    #         emp_lis = emp_lis.join(w)

    emp_lis = emp_lis.join(w for w in word_punct if w.lower() in eng_words or not w.isalpha())
    emp_lis_final = emp_lis.join(c for c in emp_lis if c not in emoji.UNICODE_EMOJI)
    return emp_lis_final


# Func_4: tokenization
def work_token(x):
    filltered_sentence = []
    word_tokens = word_tokenize(x)

    for w in word_tokens:
        if w not in stop_words:
            filltered_sentence.append(w)

    return filltered_sentence


data['comment_nopunc'] = data['comment'].apply(lambda x: remove_punc(x))
data['comment_nopunc_nonum'] = data['comment_nopunc'].apply(lambda x: remove_number(x))
data['comment_final'] = data['comment_nopunc_nonum'].apply(lambda x: work_token(x))

data['y'] = data['label'].map(lambda x: int(x == 'Hate'))

# print(data.head(200))

data[['ID', 'comment_final', 'y']].to_csv("Bodian-122920-CleanComment.csv", encoding="UTF8", index=False)
