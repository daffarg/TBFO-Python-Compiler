BLANK = " "
TAB = "\t"
MARK = "\n"

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
                while line[idx] != BLANK and line[idx] != TAB and line[idx] != MARK:
                    string += line[idx]
                    idx += 1
                array_of_strings.append(string)
                if line[idx] == MARK or idx > len(line) - 1:
                    break
                while line[idx] == BLANK or line[idx] == TAB:
                    idx += 1
        array_of_codes.append(array_of_strings)
    return array_of_codes
print(readPythonFile("tes.txt"))
