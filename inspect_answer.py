from script.util import *
import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-s', '--source', dest='source', help = 'the index of the question')
parser.add_option('-t', '--type', dest = 'type', help = 'the type of the source')
parser.add_option('-n', '--no-open', action = 'store_false', dest = 'no_open', default = False, help = 'do not open the output')
options, args = parser.parse_args()

recv = options.source
if recv is None:
    print('no question index provided')
    parser.print_help()
    exit(0)

root = os.getcwd()
toc = GetAnswerTOC(root)
tocNames = [key for key,_ in toc.items()]


hit = []
for name in tocNames:
    if recv in toc[name]:
        hit.append(name)

target = options.type

if len(hit) == 0:
    print('unable to find index {}'.format(recv))
    exit(0)
elif len(hit) == 1:
    target = hit[0]
else:
    if target is None:
        print('multiple targets found, but no type specified')
        for key in hit:
            print('name: {}\ttype: {}'.format(recv, key))
        exit(0)
    else:
        if target not in hit:
            print('invalid type {}'.format(target))
            exit(0)

if target == 'tex':
    with open(toc[target][recv], 'r') as infile:
        frac = infile.read()

    #print(toc[target][recv])
    full = GenerateFullTex(root, frac)
    #print(full)
    pdfOutput = CompileTeX(root, recv, full)
    if options.no_open:
        if os.path.exists(pdfOutput):
            OpenFile(pdfOutput)
        else:
            raise RuntimeError('unable to open file {}, there might have been some error in compiling LaTeX'.format(pdfOutput))
elif target == 'python':
    raise RuntimeError('rules for target python is undefined')
else:
    raise RuntimeError('unknown target {}'.format(target))

