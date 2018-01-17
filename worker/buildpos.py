import os
import pymorphy2


possw = {
    'NOUN' :  1,    # имя существительное
    'ADJF' :  2,    # имя прилагательное (полное)
    'ADJS' :  3,    # имя прилагательное (краткое)
    'COMP' :  4,    # компаратив
    'VERB' :  5,    # глагол (личная форма)
    'INFN' :  6,    # глагол (инфинитив)
    'PRTF' :  7,    # причастие (полное)
    'PRTS' :  8,    # причастие (краткое)
    'GRND' :  9,    # деепричастие
    'NUMR' :  10,   # числительное
    'ADVB' :  11,   # наречие
    'NPRO' :  12,   # местоимение-существительное
    'PRED' :  13,   # предикатив
    'PREP' :  14,   # предлог
    'CONJ' :  15,   # союз
    'PRCL' :  16,   # частица
    'INTJ' :  17,    # междометие
     None  :  18
}

symbol = {
    '!'  : '.',
    '.'  : '.',
    ','  : '',
    '?'  : '',
    ';'  : '.',
    ':'  : '',
    '('  : '',
    ')'  : '',
    '['  : '',
    ']'  : '',
    '{'  : '',
    '}'  : '',
    '"'  : '',
    '<'  : '',
    '>'  : '',
    '-'  : '',
    '@'  : '',
    '#'  : '',
    '$'  : '',
    '^'  : '',
    '&'  : '',
    '*'  : '',
    '+'  : '',
    '='  : '',
    '~'  : '',
    '/'  : '',
    '\\' : '',
    '|'  : '',
    '\n' : '',
    '«'  : '',
    '»'  : '',
    '—' : '',
    '–'  : '',
    None : '',
    '…'  : '',
    '“'  : '',
    '”'  : ''
}
morph = pymorphy2.MorphAnalyzer()


def createposfile(file_name):
    temp = ''
    cur_dir = os.path.abspath(os.curdir)
    infile = open(cur_dir + file_name, 'r')
    outfile = open(cur_dir + file_name.replace('.', '_out.'), 'w')
    log = open(cur_dir + file_name.replace('.', '_log.'), 'w')
    for char in infile.read():
        if char.isalpha():
            temp += char
        else:
            if temp != ' ' and temp != '':
                log.write(temp + " : " + str(possw.get(morph.parse(temp)[0].tag.POS)) +'\n')
                outfile.write(' ')
                outfile.write(str(possw.get(morph.parse(temp)[0].tag.POS)))
                temp = ''
            if ord(char) > 57 & ord(char) < 48:
                outfile.write(symbol.get(char, ''))
    infile.close()
    outfile.close()
    log.close()
    return cur_dir + file_name.replace('.', '_out.')

