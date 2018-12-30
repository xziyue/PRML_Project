# compile all tex answers
from script.util import *
import operator

root = os.getcwd()
toc = GetAnswerTOC(root)

def GetTuple(name):
    fname = os.path.basename(name)
    name, _ = os.path.splitext(fname)
    nums = name.split('.')
    return tuple(map(int, nums))


_allAns = [(GetTuple(val), val) for _, val in toc['tex'].items()]
_allAns.sort(key=operator.itemgetter(0))
allAns = [val[1] for val in _allAns]

allFrac = ''
for path in allAns:
    with open(path, 'r') as infile:
        allFrac += infile.read()

full = GenerateFullTex(root, allFrac)
pdfOutput = CompileTeX(root, 'all', full)
if os.path.exists(pdfOutput):
    OpenFile(pdfOutput)
else:
    raise RuntimeError('unable to open file {}, there might have been some error in compiling LaTeX'.format(pdfOutput))
