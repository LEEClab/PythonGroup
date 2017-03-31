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
b and c # False
a or c # True
b or c # True
a or c # True
b or c # True
c or a # True
c or b # True
c or c # True
b or b # False



# 3.3.3 Expressões lógicas

## Exercício 3.4 ##
salario = 1500
imposto = 1200

salario >= imposto 

salario = 1199
imposto = 1200

salario >= imposto 



## Exercício 3.5 ##
A = 1
B = 2
C = True
D = False
A > B and C or D # False

A = 10
B = 3
C = False
D = False
A > B and C or D # False

A = 5
B = 1
C = True
D = True
A > B and C or D # True


## Exercício 3.6 ##
materia1 = 1
materia2 = 2
materia3 = 10

media = 7

(materia1 + materia2 + materia3) / 3 >= media

materia1 = 10
materia2 = 8
materia3 = 10

media = 7

(materia1 + materia2 + materia3) / 3 >= media

###-----------------------------------------------------------###

## 3.4 Variáveis string
# Listagem 3.7 - A função len
print(len("A"))
print(len("AB"))
print(len(""))
print(len("O rato roeu a roupa"))

# Listagem 3.8 - Manipulação de strings no interpretador
a = "ABCDEF"
print(a[0])
print(a[1])
print(a[5])
print(a[6])
print(len(a))

## 3.4.1 Operações com strings
## 3.4.1.1 Concatenação
# Listagem 3.9 - Exemplo de concatenação
s = "ABC"
print(s + "C")
print(s + "D" * 4)
print("X" + "-" * 10 + "X")
print(s + "4x = " + s * 4 )

## 3.4.1.2 Composição
# Listagem 3.10 - Exemplo de composição com marcadores
idade = 22
print("[%d]" % idade)
print("[%03d]" % idade)
print("[%3d]" % idade)
print("[%-3d]" % idade)

# Listagem 3.11 - Exemplo de composição com números decimais
print("%5f" % 5)
print("%5.2f" % 5)
print("%10.2f" % 5)

# Listagem 3.12 - Exemplo de composição de string
nome = "João"
idade = 22
grana = 51.34
print("%s tem %d anos e R$%f no bolso." % (nome, idade, grana))
print("%12s tem %3d anos e R$%5.2f no bolso." % (nome, idade, grana))
print("%12s tem %03d anos e R$%5.2f no bolso." % (nome, idade, grana))
print("%-12s tem %-3d anos e R$%-5.2f no bolso." % (nome, idade, grana))

## 3.4.1.3 Fatiamento
# Listagem 3.13 - Exemplo de fatiamento
s = "ABCDEFGHI"
print(s[0:2])
print(s[1:2])
print(s[2:4])
print(s[0:5])
print(s[1:8])


# Listagem 3.14 - Exemplo de fatiamento com omissão de valores e com índices negativos
s = "ABCDEFGHI"
print(s[:2])
print(s[1:])
print(s[0:-2])
print(s[:])
print(s[-1:])
print(s[-5:7])
print(s[-2:-1])

###-----------------------------------------------------------###

## 3.5 Sequências e tempo
# Listagem 3.15 - Exemplo de sequência e tempo
divida = 0
compra = 100
divida = divida + compra
compra = 200
divida = divida + compra
compra = 300
divida = divida + compra
compra = 0
print(divida)

###-----------------------------------------------------------###

## 3.6 Rastreamento

###-----------------------------------------------------------###

## 3.7 Entrada de dados

# Listagem 3.15 - Exemplo de sequência e tempo
divida = 0

# Listagem 3.15 - Exemplo de sequência e tempo
divida = 0

# Listagem 3.15 - Exemplo de sequência e tempo
divida = 0

# Listagem 3.15 - Exemplo de sequência e tempo
divida = 0

# Listagem 3.15 - Exemplo de sequência e tempo
divida = 0


###-----------------------------------------------------------###









