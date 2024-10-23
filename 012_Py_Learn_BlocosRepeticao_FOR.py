# Para laços de repetição podemos utilizar o comando FOR
def main():
    # lista de alunos
    alunos = ['Aluno1', 'Aluno2', 'Aluno3']
    # incrementando um novo nome na lista
    alunos.append('NovoAluno')
    for ContadorAluno in alunos:
        print(ContadorAluno)

# Para utilizarmos um intervalo no FOR (de X até Y) podemos usar a função "RANGE"
notas = []
# Com a função range() podemos fazer o bloco FOR interar quantas vezes definirmos
for i in range(4,11):
    notas.append(i)

for nota in notas:
    print(nota)
main()
