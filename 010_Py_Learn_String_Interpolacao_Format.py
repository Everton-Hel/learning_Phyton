"""
Interpolação básica de strings
%s - string
%d e %i - int
%f - float (%.2f - insere 2 casa decimais)
%x e %X - Hexadecimal (ABCDEF0123456789) (caixa baixa e caixa alta, resulta no mesmo sentido)
%08X - Essa ação gera o resujltado com o tamanho de 8 caracteres, completando com zero a esquerda
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))


# -----------------------------------------------------------------------------------------------
"""
F-String - Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade) - ação para manter aimpressão mais a esquerda/direita/centro
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}.') # Exemplo:       ABC.
print(f'{variavel: <10}.') # Exemplo:ABC       .
print(f'{variavel: ^10}.') # Exemplo:   ABC    .
print(f'{1000.4873648123746:0=+10,.1f}') # o sinal de "=" irá formar o sinal de "+" fica na esquerda -. Exemplo:+0010.5
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')