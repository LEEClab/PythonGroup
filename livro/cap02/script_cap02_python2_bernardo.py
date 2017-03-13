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

salario = 750.0 # ou float(750)
aumento = 15
novo_salario2 = salario * (100 + aumento)/100

print (novo_salario, novo_salario2)
# Precisamos prestar atencao com numeros reais (numeros de ponto flutuante ou float), 
# pois quando fazemos operacoes sem prestar atencao nisso podemos acabar tendo um resultado inesperado!

# Uma dica, ao usarmos python 2, eh sempre importarmos a funcao division do modulo __future__
# Vejam a diferenca em python 2

from __future__ import division

salario = 750
aumento = 15
novo_salario = salario * (100 + aumento)/100

print (novo_salario) #;-)
