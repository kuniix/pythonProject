numeros = [1, 4, 7, 9, 12, 21]

quadrados = list(map(lambda num: num ** 2, numeros))

print('Usando map: ', quadrados)

quadrados = [num ** 2 for num in numeros]
print('Usando List compreehension: ', quadrados)

# criar um lista de numeros pares de 0 a 10
pares = [num for num in range(11) if num % 2 == 0]
print('Usando list compreehension numeros pares: ', pares)

frase = 'Curso em Video Python'
vogais = ['a', 'e', 'i', 'o', 'u', 'é', 'á', 'í', 'ó', 'ú']

lista_vogais = [v for v in frase if v in vogais]
print(f"A frase possui {len(lista_vogais)} vogais.")

# distributiva entre valores de duas listas
distributiva = [k * m for k in [2, 3, 5] for m in [10, 20, 30]]

print(distributiva)