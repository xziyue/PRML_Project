from script.util import *

root = os.getcwd()
toc = GetAnswerTOC(root)

tocNames = [key for key,_ in toc.items()]

recv = input('please enter the index of the question: ').strip()

hit = []
for name in tocNames:
    if recv in toc[name]:
        hit.append(name)

target = None

if len(hit) == 0:
    print('unable to find index {}'.format(recv))
    exit(0)
elif len(hit) == 1:
    target = hit[0]
else:
    print('multiple targets found, please provide the type of answer you would like to inspect')
    for key in hit:
        print('name: {}\ttype: {}'.format(recv, key))
    typeRecv = input().strip()
    if typeRecv in hit:
        target = typeRecv
    else:
        print('invalid type {}'.format(typeRecv))
        exit(0)

if target == 'tex':
    with open(toc[target][recv], 'r') as infile:
        frac = infile.read()

    full = GenerateFullTex(root, frac)
    pdfOutput = CompileTeX(root, recv, full)
    if os.path.exists(pdfOutput):
        OpenFile(pdfOutput)
    else:
        raise RuntimeError('unable to open file {}, there might have been some error in compiling LaTeX'.format(pdfOutput))
elif target == 'python':
    raise RuntimeError('rules for target python is undefined')
else:
    raise RuntimeError('unknown target {}'.format(target))

