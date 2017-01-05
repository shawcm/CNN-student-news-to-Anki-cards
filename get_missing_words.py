#!/usr/bin/env python3
# FILE get_missing_words.py
# CREATED BY 邵传明 AT 2017-01-05 17:43

def has_missing_words():
    dlog = 'dlog'
    s = open(dlog, 'r')
    for l in s:
        l = s.readline()
        if l.startswith('Missing Words'):
            s.close()
            return True
    return False


def get_missing_words():
    '''get missing words list from dlog file'''
    if not has_missing_words():
        return []

    words = []
    dlog = 'dlog'
    s = open(dlog, 'r')
    while True:
        l = s.readline()
        if l.startswith('Missing Words'):
            s.readline()
            break
        elif l.startswith('Dictionary Usage Statistic'):
            s.close()
            return words
    while True:
        l = s.readline().strip()
        if l == '':
            break
        words.append(l)
    s.close()
    return words


if __name__ == '__main__':
    words = get_missing_words()
    print(words)
