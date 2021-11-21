from dfa import *

BLANK = " "
TAB = "\t"
MARK = "\n"

keyword = [ # array of keyword sesuai terminal pada cfg (kecuali string, integer, dan variable)
            '=', '==', '!=', '>', '<', '>=', '<=', '+', '-', '*', '/', '%', 'break', 'continue', 
            'pass', 'in', 'with', 'as', 'None', '(', ')', '[', ']', ':', ',', '.', 'True', 'False','int', 
            'str', 'float', 'input', 'print', 'and', 'or', 'not', 'is', '=', '+=', '-=', '*=', '/=', '%=', 'if', 
            'elif', 'else', 'while', 'for', 'def', 'return', 'import', 'from', 'raise', 'with'
          ]

def readPythonFile(filepath):
    ln = 1
    f = open(filepath,'r')
    lines  = f.readlines()
    array_of_codes = []
    for line in lines:
        varValid = True
        array_of_strings = []
        idx = 0
        useless_line = True

        for char in line: # pengecekan apakah suatu line hanya terdiri dari blank atau tab atau new line 
            if char != TAB and char != MARK and char != BLANK:
                useless_line = False 

        # jika useless_line True, line tidak perlu dibaca
        if not useless_line: # jika line perlu dibaca (useless_line False)
            while line[idx] == BLANK or line[idx] == TAB:
                idx += 1
            else:   
                while True:
                    string = ""
                    while idx <= len(line) - 1 and line[idx] != BLANK and line[idx] != TAB and line[idx] != MARK and string not in keyword: 
                        string += line[idx]
                        idx += 1
                        isString = (string[0] == '"' and string[-1] == '"' and len(string) > 1) or (string[0] == "'" and string[-1] == "'" and len(string) > 1) # jika string
                        if (string.isdigit() or (string[1:].isdigit() and (string[0] == '-' or string[0] == '+'))): # jika current character integer, harus dicek character selanjutnya
                            if idx <= len(line) - 1 and line[idx] not in keyword: # jika idx belum melebihi batas dan next cc tdk ada pada keyword (bisa jadi abjad atau integer)
                                continue
                        if isString or (idx <= len(line) - 1 and line[idx] in keyword): # jika string atau idx belum melebihi batas dan next cc ada pada keyword
                            break
                        # if idx <= len(line) - 1: # jika next cc ada di dalam keyword
                        #     if line[idx] in keyword:
                        #         break
                    if string not in keyword: # jika tdk ada di dalam keyword, maka string atau integer atau variabel
                        if (string[0] == '"' and string[-1] == '"' and len(string) > 1) or (string[0] == "'" and string[-1] == "'" and len(string) > 1):
                            string = 'string'
                        elif string.isdigit() or (string[1:].isdigit() and (string[0] == '-' or string[0] == '+')):
                            string = 'integer'
                        else:
                            varValid = isVarNameValid(string) # pengecekan nama variabel oleh DFA
                            if varValid:
                                string = 'variable'
                    array_of_strings.append(string)
                    if idx >= len(line) or line[idx] == MARK or not varValid:
                        break
                    while line[idx] == BLANK or line[idx] == TAB:
                        idx += 1
            if not varValid: # jika ada variabel tdk valid, line selanjutnya tdk perlu diperiksa lagi
                break
            array_of_codes.append(array_of_strings)
        ln += 1
    f.close()
    return array_of_codes, varValid, ln
