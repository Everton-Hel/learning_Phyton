""" Operador lógico "not" Usado para inverter expressões
Também pode se aplicado em conjunto nas funções IF / ELIF / ELSE / OR / AND
not True = False
not False = True
"""
print(not True)  # False
print(not False)  # True

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')
if encontrar not nome:
    print(f'{encontrar} Não encontrado em {nome}')
else:
    print(f'{encontrar} está em {nome}')
# ----------------------------------------------------------------------------------
""" Operador "IN" usado para verificar se um valor está dentro de outra variavel """
nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')
if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
