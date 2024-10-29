def main():
    exercicio = input("Entre com o número do Exercicio entre 1-3: ")
    try:
        exercicio_int = int(exercicio)
        if exercicio_int == 1:     
            """
            Faça um programa que peça ao usuário para digitar um número inteiro,
            informe se este número é par ou ímpar. Caso o usuário não digite um número
            inteiro, informe que não é um número inteiro.
            """
            # Ha 2 forma de fazer, utilizando o try/except ou if entrada.isdigit(): que irá verificar se é apenas números
            # Estarei comentando a opção do isdigit e assim podendo inverter
            V1 = input("Entre com um número inteiro: ")
            try:
            # V1.isdigit(): # ubstitui o 'try' verificando sé é apenas numerico
                V1_int = int(V1)
                if V1_int % 2 == 0:
                    print(f"O número {V1_int} é Par")
                else:
                    print(f"O número {V1_int} é Impar")
            except:
            # else: # substitui o 'except'
                print(f"O valor digitado: {V1} Não é um número inteiro")
        #------------------------------------------------------------------------------------
        elif exercicio_int == 2:
            """
            Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
            descrito, exiba a saudação apropriada. Ex. 
            Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
            """
            # Ha 2 forma de fazer, utilizando o try/except ou if entrada.isdigit(): que irá verificar se é apenas números
            # Estarei comentando a opção do isdigit e assim podendo inverter            
            hora = input("Informe apenas a HORA: ")
            try:
            # hora.isdigit(): # ubstitui o 'try' verificando sé é apenas numerico
                hora_int = int(hora)
                if (hora_int >= 0 and hora_int <= 11):
                    print("Bom dia")
                elif (hora_int >=12 and hora_int <=17):
                    print("Boa tarde")
                elif (hora_int >= 18 and hora_int <= 23):
                    print("Boa noite")
                else:
                    print(f"Valor digitado: {hora_int} é inregular.")
            except:
            # else: # substitui o 'except'
                print(f"O valor digitado: {hora_int} Não é um número inteiro")
        #------------------------------------------------------------------------------------
        elif exercicio_int == 3:
            """
            Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
            menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
            "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
            """
            nome_usuario = input("Entre com seu primeiro nome do usuário: ")
            try:
                nome_usuario_str = str(nome_usuario)
                if (len(nome_usuario_str) <= 4 and len(nome_usuario_str) > 0):
                    print("Seu nome é curto")
                elif (len(nome_usuario_str) == 5 or len(nome_usuario_str) == 6):
                    print("Seu nome é normal")
                elif len(nome_usuario_str) > 6:
                    print("Seu nome é muito grande")
                elif nome_usuario == '':
                    print(f"Não foi digitado nenhum nome")

            except:
                print(f"O nome de usuário digitado: {nome_usuario} não é valido")

        else:
            print(f"O valor digitado: {exercicio} está incorreto")

    except:
        print(f"O valor digitado: {exercicio} está incorreto")

main()
