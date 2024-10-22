"""
Exercício 001
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
# resultado 100% de aproveitamento
def main():
    Nome_usuario = input(" Digite seu nome: ")
    Idade_usuario = input("Digite sua idade: ")
    Caractere_vazio = (' ' in Nome_usuario)

    if Nome_usuario != '' and Idade_usuario != '':
        print(f"Seu nome é {Nome_usuario}\nSeu nome invertido é {Nome_usuario[::-1]}")
        if Caractere_vazio == True:
            print("Seu nome Contém espaços")
        else:
            print("Seu nome Não Contém espaços")
        print(f"Seu nome tem {len(Nome_usuario)} letras")
        print(f"Aprimeira letra do seu nome é: {Nome_usuario[:1]}")
        print(f"A última letra do seu nome é {Nome_usuario[len(Nome_usuario)-1:len(Nome_usuario):]}")
    else:
        print("Desculpe, você deixou campos vazios.")
main()

# Exercicio corrigido - mesmo resultado
"""
nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')
if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios.")
"""
