def main():
    # Documentação Phyton - https://docs.python.org/pt-br/3/library/stdtypes.html
    #
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
        # Ellipsis (pass ->  tem a ação de que irá continuar e assim consegue debugar sem erros)
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

    # Exemplo 1.0 -> (Verificando o identificado da memoria por variavel)
    v1 = 'a'
    v2 = 2
    print(id(v1))
    print(id(v2))
    
    # Exemplo 2.0 -> (Calcule a multiplicação enrte 2 valores setados)
    a = 5
    b = 6
    r = a * b
    print("A soma de", a, "com", b, "e: ", r)

    # Exemplo 3.0 -> (Calcule a SOMA enrte 2 valores de entrada, convertendo a entrada de estring para inteiro)
    Inp1 = int(input("Entre com o primeiro valor:"))
    Inp2 = int(input("Entre com o segundo valor:"))
    saida = Inp1 + Inp2
    print("A Soma de", Inp1, "com", Inp2, "é: ",saida)

    # Exemplo 4.0 -> (Calcule a SOMA enrte 2 valores de entrada, convertendo a entrada de estring para float)
    Inp1 = float(input("Entre com o primeiro valor:"))
    Inp2 = float(input("Entre com o segundo valor:"))
    saida = Inp1 + Inp2
    print("A Soma de", Inp1, "com", Inp2, "é: ",saida)

    # Exemplo 5.0 -> (passando argumento na função print e imprimindo na tela mudando o separador)
    # \r\n -> CRLF
    # \n -> realiza a quebra de linha (no Linux o LF realiza a quebra de linha)
    # end='#' -> inclui e não quebra a linha
    #sep = '-' -> em uma lista a vigula como padram inseri o "espaço" como separador, ou utilizando a função "sep" pode alterar o separador
    print(12, 34, 1011, sep="", end='#')
    print(56, 78, sep='-', end='\n')
    print(9, 10, sep='-', end='\n')

    # Exemplo 6.0 -> (inserindo aspas duplas, deve iniciar e finalizar com com aspas simples)
    print('Luiz "Otávio"')
    
     # Exemplo 7.0 -> (Caractere de Escape, para inserir aspas duplas por exemplo, o caractere apos o "/" será ignorado)
    print("Luiz \"Otávio\"")

    # Exercicio 8.0 -> (r -> para expreções regulares)
    print(r"Luiz \"Otávio\"")

    # Exemplo 9.0 -> (A função type mostra o tipo da variavel no Python)
    print(type('Otávio'))
    print(type(0))
    print(type(1.1), type(-1.1), type(0.0))
    # Exemplo 10.0 -> ("len" tem a ação de verificar a quantidade de caracteres da variavel)
    print(f'Seu nome tem {len(nome)} letras')
    # Exemplo 11.0 -> (Imprimindo apenas o primeiro caractere)
    print(f'A primeira letra do seu nome é {nome[0]}')
    # Exemplo 12.0 -> (Impriminto o ultimo caractere) 
    print(f'A última letra do seu nome é {nome[-1]}')
    # Exemplo 13.0 -> (Imprimindo invertido os caracteres)
    print(f'Seu nome invertido é {nome[::-1]}')

    # Exemplo 14.0 -> (Incluindo formatações com String tendo a função format)
    T1 = 2
    T2 = 3
    Res = T1 + T2
    # Format
    print("A soma de {0} com {1} é: {2}".format(T1, T2, Res))
    # format -> tratando as casas decimais
    print("A soma de {:2f} com {:2f} é: {:2f}".format(T1, T2, Res))
    # F-string
    print(f"A soma de {T1} com {T2} é: {Res:.2f}")

    # Exemplo 15.0 -> (É possível buscar por indice o caracter da String)
    Text0 = "Curso de Python"
    Print(Text0[2])    
     # Exemplo 15.0 -> (E possível buscar por indice o caracter da String buscando o final)
    Print(Text0[-2])    
    # Exemplo 16.0 -> (Verificando/pesquisando um caractere dentro de uma variavel)
    'z' in Text0
    'z' not in Text0    
    # Exemplo 17.0 -> (Verifica o tamanho/quantidade da variavel)
    print(len(Text0))    
    # Exemplo 18.0 -> (Alterando o tamanho da caixa da fonte - maiusculo/minusculo)
    Text0 = Text0.upper()
    Text0 = Text0.lower()    
    # Exemplo 19.0 -> (Removendo espaços a mais da String)
    print(Text0.strip())
    # Exemplo 20.0 -> (Juntando itens da string através de um delimitador)
    ",".join(Text0)
    # Exemplo 21.0 -> (Separando uma string através de um delimitador)
    print(Text0.split(","))
    # Exemplo 22.0 -> (Incluindo 10 zero a esquerda
    print(Text0.zfill(10))
    
    
main()
