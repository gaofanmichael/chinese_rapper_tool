#!/usr/bin/env /usr/local/bin/python3


import json
from pypinyin import pinyin, lazy_pinyin, Style

target_suffix = [ 'ao', 'iu']
target_word_length = len(target_suffix)

def match_suffix(word, suffix):
    return word.endswith(suffix)


# Opening JSON file
f = open('chinese-xinhua/data/idiom.json')

# returns JSON object as 
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i, item in enumerate(data): 
    if len(item["word"]) != target_word_length:
        continue
    
    pinyin = lazy_pinyin(item["word"])
    found = True
    for i in range(target_word_length):
        if not match_suffix(pinyin[i], target_suffix[i]):
            found = False
            break
    if found:
        print(item["word"])


# Opening JSON file
f = open('chinese-xinhua/data/ci.json')

# returns JSON object as 
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i, item in enumerate(data): 
    if len(item["ci"]) != target_word_length:
        continue
    
    pinyin = lazy_pinyin(item["ci"])
    found = True
    for i in range(target_word_length):
        if not match_suffix(pinyin[i], target_suffix[i]):
            found = False
            break
    if found:
        print(item["ci"])