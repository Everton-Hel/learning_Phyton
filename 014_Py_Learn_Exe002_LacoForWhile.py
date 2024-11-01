def main():
# Exercicio 2 - apresentar todos os números Pares e pular os Ímpares no intervalo de 0 ea 20, 
# executar a ação até chegar no número 15.

# Utilizando o laço FOR ---------------------------------------------------------
    print("Utilizando o laço FOR")
    for Count_ini in range(1,20):
        if Count_ini == 15:
            break
        if Count_ini % 2 == 1:
            continue 
        print(Count_ini)
        

# Utilizando o laço WHILE --------------------------------------------------------
    count_while = 0
    print("Utilizando o laço WHILE")
    while count_while <= 20:
        if count_while == 15:
            break    
        count_while +=1
        if count_while % 2 == 1:
            continue
        print(count_while)

# Utilizando o laço WHILE - realizando a contager de caracteres ------------------
"""
frase = 'aaaooo'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)
"""

main()
