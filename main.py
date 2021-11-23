from tokens import *
from dfa import *
from CFG_to_CNF import *
from cyk import *

# PROGRAM MAIN

file = input("Your file (.py): ")
codes, varValid, numOfLines, flag = readPythonFile(file)
if not varValid:
    print("SyntaxError: variable name not valid in line " + str(numOfLines))
elif flag:
    print("SyntaxError: EOF while scanning triple-quoted string literal")
else: # cek dengan CYK
    cfg = readCFGFile('cfg.txt')
    cnf = CFGtoCNF((removeUnitProduction(cfg)))
    #ln = 1
   # for code in codes:
    cyk = cykAlgorithm(codes,cnf)
    lastCYK = cyk[len(cyk)-1][0]
    if 'S' not in (lastCYK):
        print('Syntax Error')
            #print(f'ln : {ln+1}')
           # break
    else:
        print("Accepted")
    #print(cnf)

    # print(cnf)
    # print()
    #print(cyk)

    # print(codes)    
    # print("Cek dengan CYK")
