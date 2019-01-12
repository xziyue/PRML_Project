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
allAns = _allAns

allFrac = ''

titlepage = os.path.join(root, 'script', 'title_page.tex')
with open(titlepage, 'r') as infile:
    allFrac += infile.read()

allFrac += '\\frontmatter\n\\tableofcontents\n\\label{doctocpos}\n\\clearpage\n\\mainmatter\n\\rfoot{\\hyperlink{doctocpos}{$\\scriptscriptstyle\\uparrow$}}\n'

pastSec = 0
for index, path in allAns:
    nowSec = index[0]
    if nowSec != pastSec:
        pastSec = nowSec
        allFrac += '\\chapter*{{Chapter {}}}\n\\addcontentsline{{toc}}{{chapter}}{{Chapter {}}}\n\\stepcounter{{chapter}}\n'.format(nowSec, nowSec)

    nowInd = index[1]
    if nowInd == 1 or nowInd % 5 == 0:
    	allFrac += '\\phantomsection\\addcontentsline{{toc}}{{section}}{{Question {}.{}}}\n'.format(*index)
    
    with open(path, 'r') as infile:
        allFrac += infile.read()

full = GenerateFullTex(root, allFrac)
CompileTeX(root, 'all', full)
pdfOutput = CompileTeX(root, 'all', full)
if os.path.exists(pdfOutput):
    OpenFile(pdfOutput)
else:
    raise RuntimeError('unable to open file {}, there might have been some error in compiling LaTeX'.format(pdfOutput))
