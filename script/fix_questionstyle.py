from script.util import *
import re

# this substitution will be used when all solutions are finished

root = os.path.split(os.getcwd())[0]
toc = GetAnswerTOC(root)

tex = toc['tex']

testString = r'123ji\prmlstyle{1.12} '

for key, val in tex.items():
    text = None
    with open(val, 'r') as infile:
        text = infile.read()
    print('read')