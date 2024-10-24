# Laço de repetição While, que significa 'enquanto'
## Funciona enquanto uma condição for verdadeira fazendo uma determinada ação, sendo necessario informar a saida do laço
## tomar cuidado para nçao entrar em looping infinito
## Continue -> Continua a operação de loop
## Break -> Quebra a operação de loop

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
            

main()
