def main():
    # Uma variável é um nome que se refere a u valor
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
main()
