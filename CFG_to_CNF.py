from copy import deepcopy
import string

def readCFGFile(filepath):
# Mengembalikan CFG dari file
	cfg = {} 
	f = open(filepath, 'r')
	lines = [line.split('->') for line in f.readlines()]
	for line in lines:
		if line[0] not in "\n" and line[0][0] not in "#":
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
		if char not in (string.ascii_uppercase + '_' + string.digits):
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

def get_key(val,cnf):
    for key, value in cnf.items():
         if val == value:
             return key

def CFGtoCNF(cfg):
	cnf = {}
	# Mencari simbol terminal apa saja yang ada di cfg
	i = 1
	terminal = []
	for var in cfg:
		productions = cfg[var]
		for production in productions:
			for symbol in production:
				if not(isVar(symbol)):
					if symbol not in terminal:
						terminal.append(symbol)
						cnf.update({f'T{i}' :[[symbol]]})
						i += 1
	
	# Biarkan aturan produksi yang sudah dalam bentuk normal Chomsky
	for var in cfg:
		productions = cfg[var]
		for production in productions:
			if len(production) == 1 and not(isVar(production[0])):
				productions.remove(production)
				key = list(cnf.keys())
				if var in key:
					cnf[var].extend([production])
				else:
					cnf.update({var : [production]})
			if len(production) == 2 and isVar(production[0]) and isVar(production[1]):
				productions.remove(production)
				key = list(cnf.keys())
				if var in key:
					cnf[var].extend([production])
				else:
					cnf.update({var : [production]})

	# Lakukan penggantian aturan produksi yang ruas kanannya memuat simbol terminal dan panjang ruas kanan > 1
	for var in cfg:
		productions = cfg[var]
		for i, production in enumerate(productions):
			for j, symbol in enumerate(production):
				if not (isVar(symbol)):
					productions[i][j] = get_key([[symbol]],cnf)
					cfg.update({var : productions})
	
	for var in cfg:
		productions = cfg[var]
		for production in productions:
			if len(production) == 2 and isVar(production[0]) and isVar(production[1]):
				productions.remove(production)
				key = list(cnf.keys())
				if var in key:
					cnf[var].extend([production])
				else:
					cnf.update({var : [production]})	

	# Lakukan penggantian aturan produksi yang ruas kanannya memuat > 2 simbol variabel
	for var in cfg:
		productions = cfg[var]
		for production in productions:
			# print(production)
			idx = 1
			while len(production) > 2:
				cnf.update({f"{var}{idx}": [[production[0], production[1]]]})
				production = production[1:]
				production[0] = f"{var}{idx}"
				# print(production)
				idx += 1

			key = list(cnf.keys())
			if var in key:
				cnf[var].extend([production])
			else:
				cnf.update({var : [production]})

	# print(cfg)
	print(cnf)
	return

filepath = input()
# print(readCFGFile(filepath))
# print((removeUnitProduction(readCFGFile(filepath))))
# print()
CFGtoCNF((removeUnitProduction(readCFGFile(filepath))))