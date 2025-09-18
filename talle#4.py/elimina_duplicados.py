elementos = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unicos = []
for elemento in elementos:
    if elemento not in unicos:
        unicos.append(elemento)
print("Lista sin duplicados:", unicos)
