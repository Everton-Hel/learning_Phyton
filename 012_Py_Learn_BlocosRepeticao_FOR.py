# Explicação da lógica FOR
"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'Luiz'  # iterável

# iteratador = iter(texto)  # iterator
# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)
# -------------------------------------------------------------------------------
# Para laços de repetição podemos utilizar o comando FOR
def main():
    # lista de alunos
    alunos = ['Aluno1', 'Aluno2', 'Aluno3']
    # incrementando um novo nome na lista
    alunos.append('NovoAluno')
    for ContadorAluno in alunos:
        print(ContadorAluno)
    # -------------------------------------------------------------------------------
    # Para utilizarmos um intervalo no FOR (de X até Y) podemos usar a função "RANGE"
    notas = []
    # Com a função range() podemos fazer o bloco FOR interar quantas vezes definirmos
    for i in range(4,11):
        notas.append(i)
    for nota in notas:
        print(nota)
    # -------------------------------------------------------------------------------
    # Todos os possíveis alunos
    alunos = ['Aluno1', 'Aluno2', 'Aluno3', 'Aluno4']

    # A notas respectivas dos alunos
    notas = [[8,10],[10,7],[8,9],[5,5]]

    if (len(alunos) == len(notas)):
        for indice in range(len(alunos)):
            soma = 0
            for nota in notas[indice]:
                soma += nota

            media = soma / len(notas[indice])
            print(f'O aluno {alunos[indice]} tem a média {media}')
            if (media > 6):
                print(f' - Portanto ele foi aprovado')
            else:
                print(f' - Portanto ele foi reprovado')
    else:
        print("Tem algo errado/nPossivelmente algum aluno não fez a prova")


    # Utilizando a função "enumerate()" consegue além do valor o indice do char
    lista = ['E','v','e','r','t','o','n']
    for indiceKey, valor in enumerate(lista):
        print(indiceKey, valor)

    # ------------------------------------------------------------------
    # O comando Break tem a função de parar o looping e sair
    for x in range(10,20):
        print(x)
        if x ==15:
            break
    # ------------------------------------------------------------------
    # O comando continue tem a função de pular aquela passada do looping e continuar a proxima passada
    for c in range(10, 20):
        if c == 15:
            continue
        print(c)
    # ------------------------------------------------------------------
    # Extra: ha possibilidade de por o "ELSE" junto ao "FOR", na qual irá rodar após a interação
    """
    For + Range
    range -> range(start, stop, step) -> na função "range" pode inserir o inicio e fim do contador + o step que é forer a alteração/pula de x valor
    também pode ser inserido valor negativo, mas deve alterar o star e stop Exemplo: "for valor in range(0,-10,2):" dessa forma irá pular de 2 em 2
    iniciando do 0 até o -9. Exemplo de saida: 0 -> -2 -> -4 -> -6 -> -8.
    """
    for I in range(5):
        print(I)
    else:
        Print("Apos o laço a iteração")

main()
