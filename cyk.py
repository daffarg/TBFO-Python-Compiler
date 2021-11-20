from typing import DefaultDict
from CFG_to_CNF import *

def getRuleProduction(val,cnf):
    keys = []
    for key in cnf:
        productions = cnf[key]
        for production in productions:
            if val == production:
                keys.append(key)
    return keys

def concatRule(first, second):
    res = set()
    if first == set() or second == set():
        return set()
    for f in first:
        for s in second:
            res.add(f+s)
    return res
    

def cykAlgorithm(tokens,cnf):
    # Membuat table cyk
    length = len(tokens)
    cyk = [[set() for j in range(length-i)] for i in range(length)]

    # Mengisi baris pertama cyk
    for i in range(length):
        var = getRuleProduction([tokens[i]],cnf)
        for v in var:
            cyk[0][i].add(v)

    # Mengisi baris kedua sampai ke-n
    for i in range(1, length):
        for j in range(length - i):
            for k in range(i):
                row = concatRule(cyk[k][j], cyk[i-k-1][j+k+1])
                # print(row)
                for ro in row:
                    token = []
                    for r in ro:
                        token.append(r)
                    # print(token)
                    var = getRuleProduction(token,cnf)
                    if var:
                        for v in var:
                            cyk[i][j].add(v)

    return cyk

# filepath = input()
# cnf = CFGtoCNF((removeUnitProduction(readCFGFile(filepath))))
# tokens = ['b', 'a', 'a', 'b', 'a']
# cyk = cykAlgorithm(tokens,cnf)
# lastCYK = cyk[len(cyk)-1][0]
# if 'S' in lastCYK:
#     print("accept")
# else:
#     print('reject')