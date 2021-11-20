BLANK = " "
TAB = "\t"
MARK = "\n"

keyword = [
            '==', '!=', '>', '<', '>=', '<=', '+', '-', '*', '/', '%', 'break',
            'continue', 'pass', 'in', 'with', 'as', 'None', '(', ')', '[', ']', ':', ',', '.', 'True', 'False','int', 
            'str', 'float', 'input', 'print', 'and', 'or', 'not', 'is', '=', '+=', '-=', '*=', '/=', '%=', 'if', 
            'elif', 'else', 'while', 'for', 'def', 'return', 'import', 'from', 'raise', 'with'
          ]

def readPythonFile(filepath):
    f = open(filepath,'r')
    lines  = f.readlines()
    array_of_codes = []
    for line in lines:
        array_of_strings = []
        idx = 0
        while line[idx] == BLANK or line[idx] == TAB:
            idx += 1
        if line[idx] == MARK:
            f.close()
        else:   
            while True:
                string = ""
                while line[idx] != BLANK and line[idx] != TAB and line[idx] != MARK and string not in keyword: 
                    string += line[idx]
                    idx += 1
                    isString = (string[0] == '"' and string[-1] == '"' and len(string) > 1) or (string[0] == "'" and string[-1] == "'" and len(string) > 1)
                    isInteger = string.isdigit() or (string[1:].isdigit() and (string[0] == '-' or string[0] == '+'))
                    if isString or isInteger:
                        break
                if string not in keyword:
                    if (string[0] == '"' and string[-1] == '"' and len(string) > 1) or (string[0] == "'" and string[-1] == "'" and len(string) > 1):
                        string = 'string'
                    elif string.isdigit() or (string[1:].isdigit() and (string[0] == '-' or string[0] == '+')):
                        string = 'integer'
                array_of_strings.append(string)
                if line[idx] == MARK or idx > len(line) - 1:
                    break
                while line[idx] == BLANK or line[idx] == TAB:
                    idx += 1
        array_of_codes.append(array_of_strings)
    return array_of_codes
print(readPythonFile("tes.txt"))
