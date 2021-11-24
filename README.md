# TBFO-Python-Compiler

## Tugas Besar IF2124 - Teori Bahasa Formal dan Automata

Implementasi CFG sebagai compiler untuk pengecekan kebenaran sintaks program Python dan DFA untuk pengecekan kebenaran nama variabel

** Note: tidak semua kata kunci dalam bahasa Python diimplementasikan dalam program ini **

Anggota:
1. 13520118 - Mohamad Daffa Argakoesoemah 
2. 13520125 - Ikmal Alfaozi

## How to Run
1. Unduh dan install Python3 melalui https://www.python.org/downloads/
2. Jalankan main.py pada terminal dengan perintah
```shell
python main.py
```
3. Masukkan nama file yang ingin dicek sintak programnya dengan ekstensi .py atau .txt
4. Jika sintaksnya benar, program akan mengeluarkan `Accepted`
5. Jika sintaks salah, program akan mengeluarkan pesan kesalahan `Syntax Error` atau pesan kesalahan lain khusus kesalahan nama variabel atau multiline comment