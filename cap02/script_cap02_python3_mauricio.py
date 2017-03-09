"""
Introdução à Programação com Python
Nilo Ney Coutinho Menezes

Cap 02 Preparação do ambiente
Intalação do interpretador Python, introdução ao editor de textos, apresentação do IDLE, ambiente de execução,
como degitar programas e fazer os primeiros testes com operações aritméticas no interpretador

Maurício Humberto Vancine
26/02/2017

Modificado Por Bernardo Niebuhr - 09/03/2017
"""

### 2.5 Os primeiros progrmas

# Listagem 2.1 - Usando o interpretador como calculadora
2 + 3

# Listagem 2.2 - Subtração
5 - 3

# Listagem 2.3 - Adição e subtração
10 - 4 + 2

# Listagem 2.4 - Multiplicação e divisão
2 * 10

20 / 4

# Listagem 2.5 - Exponenciação
2 ** 3

# Listagem 2.6 - Resto da divisão inteira
10 % 3

16 % 7

63 % 8

## Exercício 2.1 ##
10 + 20 * 30

4 ** 2 / 30

(9 ** 4 + 2) * 6 - 1

## Exercício 2.2 ##
10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2

###-----------------------------------------------------------###

### 2.6 Conceitos de variáveis e atribuição

# Listagem 2.7 - O primeiro programa com variáveis
a = 2
b = 3
print(a + b)

# Listagem 2.8 - Exemplo mostrado no interpretador
a = 2
b = 3
print(a + b)

# Listagem 2.9 - Outra forma de resolver o problema
print(2 + 3)

# Listagem 2.10 - Outra forma de resolver o problema
print(5)

# Listagem 2.11 - Cálculo de aumento de salário
salário = 1500
aumento = 5
print(salário + (salário * aumento / 100))

# Listagem 2.12 - Cálculo de aumento de salário no interpretador
salário = 1500
aumento = 5
print(salário + (salário * aumento / 100))

# Listagem 2.13 - Alternativa para o cálculo de aumento de salário
print(1500 + (1500 * 5 / 100))

## Exercício 2.3 ##
print("Maurício Humberto Vancine")

## Exercício 2.4 ##
a = 3
b = 5
print(2 * a * 3 * b)
 
## Exercício 2.5 ##
a = 2
b = 3
c = 4
print(a + b + c)

## Exercício 2.6 ##
salário = 750
aumento = 15
print(salário + (salário * aumento / 100))

#########################################
# Aqui estao os mesmos exercicios feitos pelo Bernardo!
# Vejam como as solucoes variam!

###############
# Exercicio 2.3

nome = 'Bernardo Niebuhr'
print (nome)

###############
# Exercicio 2.4

a = 3
b = 5
resultado = 2*a * 3*b
print (resultado)

###############
# Exercicio 2.5

a = 2
b = 3
c = 1
print(a + b + c)

###############
# Exercicio 2.6

salario = 750
aumento = 15
novo_salario = salario * (100 + aumento)/100

print (novo_salario)

750 * 1.15
750.0 * 1.15

# Vejam a diferenca

salario = 750.0
aumento = 15
novo_salario2 = salario * (100 + aumento)/100

print (novo_salario, novo_salario2)
# Precisamos prestar atencao!!
