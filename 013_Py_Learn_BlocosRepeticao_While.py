# Laço de repetição While, que significa 'enquanto'
## Funciona enquanto uma condição for verdadeira fazendo uma determinada ação, sendo necessario informar a saida do laço
## tomar cuidado para não entrar em looping infinito
## Continue -> Continua a operação de loop, então para a ação e volta ao inicio do laço
## Break -> Quebra a operação de loop (referentente ao laço mais proximo, tb pode ser inserido em IF)
## Loop infinito -> Quando um código não tem fim
"""
Operadores de atribuição - tb pode ser tratado com String, assim irá repetir a String conforme o operador
= += -= *= /= //= **= %=
"""

def main():
    contador = 1

    while contador < 6:
        print(contador)
        contador += 1    
# ------------------------------------------------------------------
    while condicao_de_parada != '9':
        condicao_de_parada = input('Digite im númro: ')
        for Cont_i in range(1, int(condicao_de_parada)):
            print(Cont_i)
# ------------------------------------------------------------------
# O comando Break tem a função de parar o looping e sair
    i = 1
    while i < 5:
        print(i)
        I += 1
        if i ==3:
            break
# ------------------------------------------------------------------
# O comando continue tem a função de pular aquela passada do looping e continuar a proxima passada
    c = 1
    while c < 5:
        c += 1
        if c ==3:
            continue
        print(c)
# ------------------------------------------------------------------
# Extra: ha possibilidade de por o "else" junto ao "While/FOR", na qual irá rodar após a interação
    while I in < 5:
        print(I)
        I += 1
    else:
        Print("Apos o laço a iteração")
# ------------------------------------------------------------------
# Demonstrando o while dentro de outro while
    qtd_linhas = 5
    qtd_colunas = 5
    linha = 1
    while linha <= qtd_linhas:
        coluna = 1
        while coluna <= qtd_colunas:
            print(f'{linha=} {coluna=}')
            coluna += 1
        linha += 1
    print('Acabou')

main()
