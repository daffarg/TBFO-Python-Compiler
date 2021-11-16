from copy import deepcopy
import re
import string

def readCFGFile(filepath):
# Mengembalikan CFG dari file
	cfg = {} 
	f = open(filepath, 'r')
	lines = [line.split('->') for line in f.readlines()]
	for line in lines:
		if line[0] != "\n":
			var = line[0].replace(" ","")
			production = [raw.split() for raw in line[1].split('|')]
			key = list(cfg.keys())
			if var in key:
				productions = cfg[var]
				productions.extend(production)
			else:
				cfg.update({var : production})
	f.close()
	return cfg

def isVar(x):
# Mengembalikan true jika x adalah Variabel
	for char in x:
		if char not in (string.ascii_uppercase):
			return False
	return True

def removeUnitProduction(cfg):
	keyVar = list(cfg.keys())
	for var in cfg:
		productions = cfg[var]
		flag = True
		while flag:
			flag = False
			for production in productions:
				if len(production) == 1 and isVar(production[0]):
					productions.remove(production)
					if production[0] in keyVar:
						newProduction = deepcopy([production for production in cfg[production[0]] if production not in productions])
						productions.extend(newProduction)
					flag = True
	return(cfg)

filepath = input()
# print(readCFGFile(filepath))
print((removeUnitProduction(readCFGFile(filepath))))

# print(removerUselessProduction(removeUnitProduction(readCFGFile(filepath))))