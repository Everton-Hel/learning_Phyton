def main():
  # Na lista a posição inicial começa no indíce "0"
  lista1 = ["nome1", "nome2", "nome3"]
  print(lista1[0], lista1[1], lista1[2])

  #Lista com a função append, incluindo novo dado
  lista1.append("Novo Aluno1")

  # Funções build in são funções externas
  lista_build_in = list()
  variavel_para_lista = 12
  lista_build_in_cheia = list(['a', 2, variavel_para_lista])

  # Manipulando a listas (Lista B passa a referenciar a Lista A e inplementado o numero 4 em ambas)
  lista_a = [1, 2, 3]
  lista_b = lista_a
  lista_append(4)
  print(lista_a)
  print(lista_b)

  # Clonar uma lista para outra e acrecentar o valor 4 apenas na lista B (quando trabalha com os conchetes, trabalha com os elementos)
  lista_a = [1, 2, 3]
  lista_b = lista_a[:]
  lista_append(4)
  print(lista_a)
  print(lista_b)

  # Buscando os elemento da lista por indice
  lista_elemento = [1, 2, 3]
  elemento1 = lista_elemento = [0]
  elemento2 = lista_elemento = [1]
  elemento3 = lista_elemento = [2]
  print(elemento1, elemento2, elemento3)

  # Utilizando a lista da posição X até posição Y
  Lista_tudo = [1,2,3,4,5,6,7,8,9,0}
  teste1 = Lista_tudo[1:4]
  teste2 = Lista_tudo[:4]
  teste3 = Lista_tudo[2:]
  print(teste1, teste2, teste3)
  


main()
