#!/usr/bin/env python3
# FILE trans_to_sentences.py
# CREATED BY 邵传明 AT 2017-01-05 14:18

import nltk.data

def text2sentences(s):
    sent_detector = nltk.data.load('/home/shaw/Document/nltk_data/tokenizers/punkt/english.pickle')
    l = sent_detector.tokenize(s)
    return l

if __name__ == '__main__':
    s = open('trans_processed.txt', 'r').read().strip()
    l = text2sentences(s)
    print('\n-----\n'.join(l))
