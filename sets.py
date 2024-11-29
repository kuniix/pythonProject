#set

# planeta_anao = {'Plutão', "Ceres", "Eris", 'Haumea', 'Makemake'}
# print(len(planeta_anao))
# print('Lua' in planeta_anao)
# print('Lua' not in planeta_anao)
#
# for astro in planeta_anao:
#     print(astro.upper())


astros1 = {'Lua', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus'}
astros2 = {'Lua', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Cometa Halley'}
# print(astros1 | astros2)
# print(astros1.union(astros2))
#
# print(astros1 & astros2)
# print(astros1.intersection(astros2))
#
# print(astros1 ^ astros2)
# print(astros1.symmetric_difference(astros2))

astros1.add('Sol')
astros1.remove('Lua')
astros1.discard('Sol')
astros1.pop()
print(astros1)