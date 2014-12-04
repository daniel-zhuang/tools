# Rename.py
# encoding utf-8
# batch rename files
# run with python3 cli
# input: 2 parameter, line [18, 22] value
# output: console log, all of match files have been renamed

import os
import os.path
import codecs
import re

if __name__=="__main__":

    print('read...')

    # probability.html.txt update
    file = codecs.open('probability.html.txt', 'r', 'utf-8')
    p = re.compile(r'\w+\.*\w*$')

    # dir value update
    dir = ''
    os.chdir(dir)

    for line in file.readlines():
        # line format see also: HTMLParser.py line 81
        line = line.strip()
        if not len(line) or line.startswith('#'):
            continue
        row = line.split('        ') #8 space
        result = re.search(p, row[0]).group(0)
        fileName = row[1].replace('.', '').replace(':', '').replace('!', '').replace('?', '').replace('\\', '')
        if result and row[1] and os.path.isfile(result) and os.access(result, os.W_OK):
            os.rename(result, fileName + '.mp4')

    print('done!')
