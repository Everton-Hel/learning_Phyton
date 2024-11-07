def main():
    """
    Faça um jogo para o usuário adivinhar qual a palavra secreta.
    - Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para
    o usuário digitar apenas uma letra.
    - Quando o usuário digitar uma letra, você vai conferir se a letra digitada está
    na palavra secreta.
        - Se a letra digitada estiver na palavra secreta; exiba a letra;
        - Se a letra digitada não estiver na palavra secreta; exiba *.
    Faça a contagem de tentativas do seu usuário.
    """
    PalavraSecreta = 'futebol'
    indice = 0
    while True:
        LetraSecreta = input("Entre apenas com uma letra: ").lower()
        Tentativa += 1
        if LetraSecreta in PalavraSecreta:
            QTDletra = PalavraSecreta.count(LetraSecreta)
            
            while indice <= len(PalavraSecreta):
                if LetraSecreta == PalavraSecreta[indice]:
                    Resultado += LetraSecreta
                else:
                    Resultado += '*'

        else:
            
            print('Letra não encontrada, tente novamente.')
            continue








main()