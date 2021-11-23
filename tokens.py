from os import read
from dfa import *

BLANK = " "
TAB = "\t"
MARK = "\n"

keyword = [ # array of keyword sesuai simbol terminal pada cfg (kecuali string, integer, comment, dan variable)
            'break', 'continue', 'pass', 'in', 'with', 'as', 'None', 'True', 'False','int', 
            'str', 'float', 'input', 'print', 'and', 'or', 'not', 'is', 'if', 'elif', 'else', 
            'while', 'for', 'def', 'return', 'import', 'from', 'raise', 'with', 'break', 'continue',
            'range', 'in', 
          ]
keywordOpAssign = [ # array simbol terminal untuk operator, assignment, dan yg tdk termasuk dalam array keyword
                    '=', '!', '>', '<', '+', '-', '*', '/', '%',
                    '(', ')', '[', ']', ':', ',', '.', '=',
                  ]

def readPythonFile(filepath):
    # mencatat jumlah baris
    f = open(filepath,'r')
    lines  = f.readlines()
    arrayOfCodes = []
    flagComment = False
    for ln, line in enumerate(lines):
        varValid = True
        idx = 0
        uselessLine = True

        for char in line: # pengecekan apakah suatu line hanya terdiri dari blank atau tab atau new line 
            if char != TAB and char != MARK and char != BLANK:
                uselessLine = False 

        # jika useless_line True, line tidak perlu dibaca
        if not uselessLine: # jika line perlu dibaca (useless_line False)
            while line[idx] == BLANK or line[idx] == TAB:
                idx += 1
            else:   
                while True:
                    string = ""
                    while idx <= len(line) - 1 and line[idx] != BLANK and line[idx] != TAB:
                        string += line[idx]
                        idx += 1
                        # if string[0] == "'": # masalahnya komennya multiple line
                        #     if len(string) >= 3 and string == "'''":
                        #         break 
                        #     else:
                        #         continue
                        if string[0] == '#':
                            while True:
                                if idx > len(line) - 1 or line[idx] == '\n':
                                    break
                                else:
                                    if idx <= len(line) - 1:
                                            string += line[idx]
                                            idx += 1
                                            continue
                        if idx <= len(line) - 1 and (line[idx] in keywordOpAssign or line[idx] == '\n' or (string in keywordOpAssign and line[idx] not in keywordOpAssign)):
                            break
                    if string not in keywordOpAssign and string not in keyword: # code yang dibaca adalah string, integer, atau variabel
                        if string == "'''":
                            flagComment = not flagComment
                            string = "comment" # agar tidak masuk ke variabel
                        elif string == '\n':
                            string = 'newline'
                        elif string[0] == '#':
                            string = 'comment'
                        elif (string[0] == '"' and string[-1] == '"' and len(string) > 1) or (string[0] == "'" and string[-1] == "'" and len(string) > 1):
                            #print(string)
                            string = 'string'
                        elif string.isdigit() or (string[1:].isdigit() and (string[0] == '-' or string[0] == '+')):
                            string = 'integer'
                        else:
                            varValid = isVarNameValid(string) # pengecekan nama variabel oleh DFA
                            if varValid:
                                string = 'variable'
                    if not flagComment:
                        arrayOfCodes.append(string)
                    if idx >= len(line) or not varValid:
                        break
                    if ln + 1 == len(lines):
                        break
                    else:
                        while line[idx] == BLANK or line[idx] == TAB:
                            idx += 1
            if not varValid: # jika ada variabel tdk valid, line selanjutnya tdk perlu diperiksa lagi
                break
    f.close()
    ln += 1
    return arrayOfCodes, varValid, ln, flagComment

a,b,c,d = readPythonFile("tes.py")
print(c)