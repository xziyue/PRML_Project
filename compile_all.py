# compile all tex answers
from script.util import *

root = os.getcwd()
toc = GetAnswerTOC(root)

allAns = [val for _, val in toc['tex'].items()]
allAns.sort()

allFrac = ''
for path in allAns:
    with open(path, 'r') as in

print('compiling...')