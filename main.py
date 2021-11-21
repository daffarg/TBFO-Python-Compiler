from tokens import *
from dfa import *
from CFG_to_CNF import *
from cyk import *

# PROGRAM MAIN

file = input("Your file (.py): ")
codes, varValid, numOfLines = readPythonFile(file)
if not varValid:
    print("Variable name not valid in line " + str(numOfLines))
else: # cek dengan CYK
    cfg = readCFGFile('cfg.txt')
    cnf = CFGtoCNF((removeUnitProduction(cfg)))
    for ln, code in enumerate(codes):
        cyk = cykAlgorithm(code,cnf)
        lastCYK = cyk[len(cyk)-1][0]
        if 'S' not in (lastCYK):
            print('Syntax Error')
            print(f'ln : {ln+1}')
            break
    if 'S' in lastCYK:
        print("Accepted")

    # print(cnf)
    # print()
    # print(cyk)

    # print(codes)    
    # print("Cek dengan CYK")