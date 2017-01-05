#!/bin/bash
# FILE trans_process.sh
# CREATED BY 邵传明 AT 2017-01-05 13:38

TRANS='./trans.txt'

# HDMan -A -D -T 1 -m -w wlist -i -l dlog dict VoxForgeDict
ex +':%s/<br>/\r/g' +':%s/^.*://g' +':%s/(.*)//g' +':%s/`/'\''/g' +':%s/\n//g' +':%s/ \+/ /g' +':w! trans_processed.txt' +':q!' $TRANS
