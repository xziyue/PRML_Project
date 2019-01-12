import subprocess, os, sys

sep = os.sep

def __CreateFolderDict(folder):
    lst = os.listdir(folder)
    res = dict()
    for filename in lst:
        name, ext = os.path.splitext(filename)
        res[name] = os.path.join(folder, filename)

    if '.gitignore' in res:
        # remove .gitignore
        del res['.gitignore']
    return res

def OpenFile(filepath):
    if sys.platform.startswith('darwin'):
        subprocess.call(('open', filepath))
    elif os.name == 'nt': # For Windows
        os.startfile(filepath)
    elif os.name == 'posix': # For Linux, Mac, etc.
        subprocess.call(('xdg-open', filepath))

def GenerateFullTex(root, targetText):
    texTemplateName = os.path.join(root, 'script', 'tex_template.tex')

    templateStr = ''
    with open(texTemplateName, 'r') as infile:
        templateStr = infile.read()

    insertBeginPattern = '% !! insert begin\n'
    insertIndex = templateStr.find(insertBeginPattern)
    if insertIndex == -1:
        raise RuntimeError('invalid tex template: cannot find insert pattern')

    insertIndex += len(insertBeginPattern)

    return templateStr[:insertIndex] + targetText + templateStr[insertIndex:]


def GetAnswerTOC(root):
    solRoot = os.path.join(root, 'solutions')
    pythonRoot = os.path.join(solRoot, 'python')
    texRoot = os.path.join(solRoot, 'tex')

    pythonDict = __CreateFolderDict(pythonRoot)
    texDict = __CreateFolderDict(texRoot)

    res = {
        'tex' : texDict,
        'python' : pythonDict
    }

    return res


def CompileTeX(root, name, texText):
    fnameFormat = 'prml_ans_{}.{}'

    outputDir = os.path.join(root, 'temp')
    fname = fnameFormat.format(name, 'tex')
    filename = os.path.join(outputDir, fname)

    with open(filename, 'w') as outfile:
        outfile.write(texText)

    outputDirParam = '-output-directory={}'.format(outputDir)

    subprocess.call(['pdflatex', '-interaction=nonstopmode', '--shell-escape', outputDirParam, filename])

    pdfOutputName = fnameFormat.format(name, 'pdf')
    pdfOutputFilaname = os.path.join(outputDir, pdfOutputName)

    return pdfOutputFilaname



    

