def main():
    """ Calculadora com While (Usuario deve entrar com 2 valores numericos e então realizar as ações de (+)(-)(*)(/) """
    print("Calculadora (Adição/Subtração/Multiplicação/Divisão)")    
 
    while True:
        inser1 = float(input("Entre com o primeiro número: "))
        inser2 = float(input("Entre com o segundo número: "))
        operador = int(input("\n  1 - Soma[+]\n  2 - Subtração[-]\n  3 - Multiplicadoe[*]\n  4 - Divisao[/]\n  Entre número que representa um dos operador: "))
        # Ação não verifica se o digitado é realmente númerico
        if ((operador > 0) and (operador <= 4)):
            if operador == 1:
                total = inser1 + inser2
                print(f'{inser1} + {inser2} = {total}')
            elif operador == 2:
                total = inser1 - inser2
                print(f'{inser1} - {inser2} = {total}')
            elif operador == 3:
                total = inser1 * inser2
                print(f'{inser1} * {inser2} = {total}')
            elif operador == 4:
                total = inser1 / inser2
                print(f'{inser1} / {inser2} = {total}')
        else:
            print('Operador incorreto')
            continue

        Sair_Continua = input("Digite [S]air : ").lower().startswith('s')
        """ Formato direto, assim a Str se torna Boll, começa com determinada letra - retorna um bool"""
        if Sair_Continua is True:
            break
    
    print('Fim do sistema calculadora1') 

  #----------------------------------------------------------------------------------------------------------------------------------------------------------------
  #----------------------------------------------------------------------------------------------------------------------------------------------------------------
    """ Correção - outro modo -  Calculadora com while 
    while True:
        numero_1 = input('Digite um número: ')
        numero_2 = input('Digite outro número: ')
        operador = input('Digite o operador (+-/*): ')
        numeros_validos = None
    
        try:
            num_1_float = float(numero_1)
            num_2_float = float(numero_2)
            numeros_validos = True
        except:
            numeros_validos = None
    
        if numeros_validos is None:
            print('Um ou ambos os números digitados são inválidos.')
            continue
    
        operadores_permitidos = '+-/*'
    
        if operador not in operadores_permitidos:
            print('Operador inválido.')
            continue
    
        if len(operador) > 1:
            print('Digite apenas um operador.')
            continue
        ###
        sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
        if sair is True:
            break
      """
main()
