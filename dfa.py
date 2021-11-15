# IMPLEMENTASI DFA UNTUK PENGECEKAN NAMA VARIABEL

def isVarNameValid(varName):
    alphabet = []
    numerical = []
    firstLowerASCII = 97
    lastLowerASCII = 122
    firstUpperASCII = 65
    lastUpperASCII = 90

    # Inisialisasi array dengan elemen semua alfabet (upper dan lower case)
    for i in range(firstLowerASCII, lastLowerASCII + 1):
        alphabet.append(chr(i))

    for j in range(firstUpperASCII, lastUpperASCII + 1):
        alphabet.append(chr(j))

    # Inisialisasi array dengan elemen semua numerik dalam bentuk string [0..9]
    for i in range(0, 10):
        numerical.append(str(i))

    # DFA terdiri dari state p0, empty, dan p1, dengan empty adalah dead state

    dfa = { # DFA dalam bentuk dictionary dengan value dictionary
        'p0': {'_': 'p1'}, # start state
        'empty': {'_': 'empty'}, # dead state
        'p1': {'_': 'p1'}, # final state
    }

    # penambahan fungsi transisi ke dalam DFA untuk input alfabet dan numerik
    for key, trans in dfa.items():
        for i in range(firstLowerASCII, lastLowerASCII + 1):
            if key == 'p0':
                trans[chr(i)] = 'p1'
            elif key == 'empty':
                trans[chr(i)] = 'empty'
            else: # key == p1
                trans[chr(i)] = 'p1'
        for j in range(firstUpperASCII, lastUpperASCII + 1):
            if key == 'p0':
                trans[chr(j)] = 'p1'
            elif key == 'empty':
                trans[chr(j)] = 'empty'
            else: # key == p1
                trans[chr(j)] = 'p1'
        for k in range(0, 10):
            if (key == 'p0' or key == 'empty'):
                trans[str(k)] = 'empty'
            elif (key == 'p1'):
                trans[str(k)] = 'p1'

    state = 'p0' # start state
    validSymbol = True
    
    # pengecekan apakah nama variabel valid dengan DFA
    for symbol in varName:
        if (symbol in alphabet or symbol in numerical or symbol == '_'): # jika simbol valid
            state = dfa[state][symbol]
        else : # simbol tidak valid
            validSymbol = False
            break
        
    return state in {'p1'} and validSymbol # p1 adalah final state