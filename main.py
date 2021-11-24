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
    cyk = cykAlgorithm(codes,cnf)
    lastCYK = cyk[len(cyk)-1][0]
    if 'S' not in (lastCYK):
        print('Syntax Error')
    else:
        print("Accepted")