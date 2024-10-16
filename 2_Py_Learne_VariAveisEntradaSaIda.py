def main():
    # Uma variável é um nome que se refere a u valor
    """ DocString - Usar para escrever suas notas em diversas linhas """
    ''' DocString - Usar para escrever suas notas em diversas linhas'''
    # Uma Atribuição - Comando de atribuição cria uma nova variável e lhe dá um valor (set -> Setando -> Atribuindo um valor)
    # Tipos Primitivos
        # int/long
        # float
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
    
main()
