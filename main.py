from tokens import *
from dfa import *

# PROGRAM MAIN

file = input("Your file (.py): ")
codes, varValid, numOfLines = readPythonFile()
if not varValid:
    print("Variable name not valid in line " + str(numOfLines))
else: # cek dengan CYK
    print("Cek dengan CYK")
