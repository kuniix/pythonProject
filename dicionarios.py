elemento = {
    'Z' : 3,
    'nome' : 'Lítio',
    'grupo' : 'Metais Alcalinos',
    'densidade': 0.534
}

print(f"Elemento: {elemento['nome']}")
print(f"Desendidade: {elemento["densidade"]}")
print(f'O dicionario possui {len(elemento)} elementos')

"""#Atualizar uma entrada
elemento['grupo'] = 'Acalinos'
print(elemento)

#Adicionar uma entrada
elemento['periodo'] = 1
print(elemento)

#exclusao de itens em dicionarios
del elemento['periodo']
print(elemento)

elemento.clear()
print(elemento)

del elemento"""

print(elemento.items())
for i in elemento.values():
    print(i)

for i, j in elemento.items():
    print(f"{i} : {j}")
