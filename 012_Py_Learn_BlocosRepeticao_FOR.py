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

main()
