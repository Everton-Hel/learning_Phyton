# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras. Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# São considerados falsy (0 0.0 '' False)
# Também existe o tipo None que é usado para representar um não valor

# Exemplo do Operador lógico AND
def main():
    entrada = input('[E]ntrar [S]air: ')
    senha_digitada = input('Senha: ')
    senha_permitida = '123456'
    
    if entrada == 'E' and senha_digitada == senha_permitida:
        print('Entrar')
    else:
        print('Sair')
main()

# Exemplo do Operador lógico OR
def main():
    cond1 = True
    cond2 = False
    
    if cond1 and cond2:
        print('Verdadeiro')
    elif cond1 or cond2:
      print('Uma delas é Verdadeiro')
    else:
        print('Ambas são falsas')
main()

# Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)
