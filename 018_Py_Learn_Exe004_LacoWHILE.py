"""
Exercicio: Iterando strings '*' em cada letra do nome com while
"""
def main():
    nome = input('Digite seu nome: ')
    Count_letra = 0 # Indice
    novo_nome = ''# Declara uma variavel Str
    while  Count_letra < len(nome): # Irá do Indice inicial até o tamanho da variavel
        nova_string = nome[Count_letra] # Irá receber letra por letre
        novo_nome  += f'*{nova_string}' # Irá amarzenar letra por letra + a string '*'
        Count_letra += 1 # O contador irá somando até sair do laço

    print(novo_nome + '*') # imprimi fora do laço e adiciona a string '*' no final

main()
