"""
Introdução à Programação com Python
Nilo Ney Coutinho Menezes

Cap 03 Variáveis e entrada de dados
Tipo de variáveis, propriedades de cada tipo, operações e operadores. Apresenta o conceito de programa no 
tempo e uma técnica simples de rastreamento. Entrada de dados pelo teclado, conversão de tipos de dados e 
erros comuns


Maurício Humberto Vancine
20/03/2017
"""

### 3.2 Variáveis numéricas

## Exercício 3.1 ##
5 # inteiro
5.0 # ponto flutuante
4.3 # ponto flutuante5
-2 # inteiro
100 # inteiro
1.333 # ponto flutuante

###-----------------------------------------------------------###

### 3.3 Variáveis numéricas

# Listagem 3.1 - Exemplo de variáveis do tipo lógico
resultado = True
aprovado = False

# 3.3.1 Operadores relacionais
# Listagem 3.2 - Exemplo de uso de operadores relacionais
a = 1 # a recebe 1
b = 5 # b recebe 5
c = 2 # c recebe 2
d = 1 # d recebe 1
a == b
b > a
a < b
a == d
b >= a
c <= b
d != a
d != b

# Listagem 3.3 - Exemplo de uso de operadores relacionais com variáveis do tipo lógico
nota = 8
media = 7
aprovado = nota > media
print(aprovado)

## Exercício 3.2 ##
a = 4
b = 10
c = 5.0
d = 1
f = 5

a == c # False
a < b # True
d > b # False
c!= f # False
a == b # False
c < d # False
b > a # True
c >= f # True
f >= c # True
c <= c # True
c <= f # True

# 3.3.2 Operadores lógicos
# 3.3.2.1 Operador not
# Listagem 3.4 - Operador not
not True
not False

# 3.3.2.2 Operador and
# Listagem 3.6 - Operador and
True and True
True and False
False and True
False and False

# 3.3.2.3 Operador or
# Listagem 3.6 - Operador or
True or True
True or False
False or True
False or False

## Exercício 3.3 ##
a = True
b = False
c = True

a and a #True
b and b # False
not c # False
not b # True
not a # False
a and b # False



# 3.3.3 Expressões lógicas

## Exercício 3.4 ##
salario = 1500
salario > 1500







###-----------------------------------------------------------###