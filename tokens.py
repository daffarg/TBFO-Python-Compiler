BLANK = " \t"

def readPythonFile(filepath):
    f = open(filepath,'r')
    lines = f.readlines()
    return lines

# def readline(line):

def ignoreBlank(cc,idx,line):
    if cc in BLANK:
        idx = idx+1
        cc = line[idx]

def adv(cc,idx,line):
    ignoreBlank(cc,idx,line)
    string = ""
    while cc not in (BLANK+'\n'):
        string += cc
        idx += 1
        cc = line[idx]
    return string

filepath = input()
# print(readPythonFile(filepath))
lines = readPythonFile(filepath)
for line in lines:
    idx = 0
    cc = line[idx]
    while cc != "\n":
        string = adv(cc,idx,line)
        print(string) 