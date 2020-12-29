
# -*- coding: utf-8 -*-

import pandas as pd
import nltk

# Step 1: Merge Data / Change Upper_Case

data1 = pd.read_csv("Bodian-122320-hand-label-795-comment.csv",
                    index_col=None,
                    usecols=['Comment', 'Label3'],
                    encoding="UTF8"
                    )

data2 = pd.read_csv("Bodian-122220-label-data.csv",
                    index_col=None,
                    usecols=['Comment', 'label2'],
                    encoding="UTF8"
                    )

col_names = ['comment', 'label']

data1.columns = col_names
data2.columns = col_names

# Concat two dataset
data = pd.concat([data1, data2], axis=0, join='outer', ignore_index=True)

# Change comment from Upper Case to Lower Case
data['comment'] = data['comment'].str.lower()

# Insert New Column as Index
data.insert(0, "ID", range(0, len(data)))


# No Index Created
data.to_csv("Bodian-122820-CommentAll.csv", index=False, encoding="UTF8")

print(data.shape)

