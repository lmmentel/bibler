#from future import print_function
from pylatex import Document
import latexcodec
from termcolor import colored

def check_nonascii(fil):
    '''check if there are non ascci characters in a file'''

    with open(fil, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines, start=1):
        for char in line:
            if ord(char) > 128:
                j = line.index(char)
                cline = line[:j] + colored(char, color='red') + line[j+1:]
                #print(u'line {0:>3d} :'.format(i), cline, end = '')

def convert2bibtex(fil):
    '''convert a file to have all the characters acceptable by bibtex'''

    with open(fil, encoding='utf-8') as f:
        lines = f.readlines()

    with open('new.bib', 'w') as f:
        for i, line in enumerate(lines, start=1):
            print(i, line, end= '')
            for char in line:
                if ord(char) > 128:
                    f.write(char.encode('latex').decode('utf-8'))
                else:
                    f.write(char)

#check_nonascii('library.bib')
#convert2bibtex('library.bib')
#
#with open('input.txt', encoding='utf-8') as f:
#    data = f.read()
#
#
#print(type(data))
#print(data)
#
#doc = Document('test')
#
#doc.append(data.encode('latex').decode('utf-8'))
#doc.generate_tex()
##doc.generate_pdf()
