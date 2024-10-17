def main():
    # Uma variável é um nome que se refere a u valor
    """ DocString - Usar para escrever suas notas em diversas linhas """
    ''' DocString - Usar para escrever suas notas em diversas linhas'''
    # Uma Atribuição - Comando de atribuição cria uma nova variável e lhe dá um valor (set -> Setando -> Atribuindo um valor)
    """ 
    Variáveis são usadas para salvar algo na memória do computador.
    PEP8: inicie variáveis com letras minúsculas, pode usar
    números e underline _.
    O sinal de = é o operador de atribuição. Ele é usado para
    atribuir um valor a um nome (variável).
    Uso: nome_variavel = expressão 
    """
    
    # Tipos Primitivos
        # Ellipsis (... -> insirir o 3 pontinho tem a ação de que irá continuar e assim consegue debugar sem erros)
        # int/long ( int -> Número inteiro  - O tipo int representa qualquer número positivo ou negativo.
        # float ( Número com ponto flutuante - O tipo float representa qualquer número positivo ou negativo com ponto flutuante.
        # bool –> True/False
        # Str -> String
        # Tuple -> Registros
        # list –> Lista de objetos
        # dict –> Coleção chave/valor
        # set -> Setando -> Atribuindo um valor
        # get -> recuperando o valor de uma váriavel
        # iNPUT -> metodo input serve para receber dados do usuário
        # Cast -> se trta da conversão de tipo de váriavel
    # Input/Output
        # print('Ola mundo') -> imprimi na tela
        # input("Digite aqui: ") -> insere entrada de valores pelo usuário
    # pass

    # Exercicio 2.1 (Calcule a multiplicação enrte 2 valores setados)
    a = 5
    b = 6
    r = a * b
    print("A soma de", a, "com", b, "e: ", r)

    # Exercicio 2.2 (Calcule a SOMA enrte 2 valores de entrada, convertendo a entrada de estring para inteiro)
    Inp1 = int(input("Entre com o primeiro valor:"))
    Inp2 = int(input("Entre com o segundo valor:"))
    saida = Inp1 + Inp2

    print("A Soma de", Inp1, "com", Inp2, "é: ",saida)

    # Exercicio 2.3 (Calcule a SOMA enrte 2 valores de entrada, convertendo a entrada de estring para float)
    Inp1 = float(input("Entre com o primeiro valor:"))
    Inp2 = float(input("Entre com o segundo valor:"))
    saida = Inp1 + Inp2

    print("A Soma de", Inp1, "com", Inp2, "é: ",saida)

    # Exercicio 2.4 (passando argumento na função print e imprimindo na tela mudando o separador)
    # \r\n -> CRLF
    # \n -> LF
    # end='#' -> inclui e não quebra a linha
    print(12, 34, 1011, sep="", end='#')
    print(56, 78, sep='-', end='\n')
    print(9, 10, sep='-', end='\n')

    # Exercicio 2.5 (inserindo aspas duplas, assim tendo que iniciar com aspas simples)
    print('Luiz "Otávio"')
    
     # Exercicio 2.6 (Caractere de Escape, para inserir aspas duplas por exemplo, o caractere apos o "/" será ignorado)
    print("Luiz \"Otávio\"")

    # Exercicio 2.7 (r -> para espreções regulares)
    print(r"Luiz \"Otávio\"")

    # Exercicio 2.8 (A função type mostra o tipo que o Python
    print(type('Otávio'))
    print(type(0))
    print(type(1.1), type(-1.1), type(0.0))

    # Exercicio 2.9 (Incluindo formatações com String tendo a função format)
    T1 = 2
    T2 = 3
    Res = T1 + T2

    print("A soma de {0} com {1} é: {2}".format(T1, T2, Res))
    #F-string
    print(f"A soma de {T1} com {T2} é: {Res}")
    #F-string - formata tratando as casas decimais
    print("A soma de {:2f} com {:2f} é: {:2f}".format(T1, T2, Res))
    
main()
