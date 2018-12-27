# compile all tex answers
from script.util import *

root = os.getcwd()
toc = GetAnswerTOC(root)

allAns = [val for _, val in toc['tex'].items()]
allAns.sort()

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
