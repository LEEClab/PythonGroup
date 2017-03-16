# PythonGroup
Grupo de estudos de Python para Análises Espaciais

## Objetivos
Nosso objetivo é estudar Python para automatizar análises espaciais no [GRASS GIS](https://grass.osgeo.org) através do módulo *grass.script*, [QGIS](http://www.qgis.org/en/site/) e [ArcGIS](https://www.arcgis.com/features/index.html) através do módulo *ArcPy*.


## Estratégia do grupo
Fazemos reuniões semanais para estudar o livro "Introdução à Programação com Python" do Nilo Ney Coutinho Menezes e fazer resolução de exercícios de cada capítulo. O livro segue a versão do Python 3, mas iremos realizar os exercícios em Python 2, pois os softwares utilizam essa versão. 
Depois de estudar esse livro, iremos estudar os módulos *grass.script* e *ArcPy* para automatizar processos SIG.

## Interpretador do Python
Estamos utilizando o interpretador [Rodeo](http://rodeo.yhat.com) para executar os comandos. Abaixo segue um tutorial para configurar o Rodeo para a versão Python 2.

### Tutorial de instalação do Rodeo com Python 2
1. Baixe e instale o software Rodeo para seu Sistema Operacional (SO).
(https://www.yhat.com/products/rodeo)

2. Baixe e instale o software Anaconda para Python 2.
(https://www.continuum.io/downloads)

3. Abra o software Rodeo, depois siga o caminho no alto da Barra de Ferramentas: Rodeo > Preferences > Python.
OBS.: Para usuários Linux, pode aparecer uma mensagem de erro ao abrir o programa. Se isso ocorrer, tente inicia-lo pelo terminal usando o comando `/opt/Rodeo/rodeo`.

4. Em *Default Working Directory*, clique nos três pontos e siga para a pasta "C:\Users\nome_do_seu_computador\Anaconda2".

5. Feche e abra o Rodeo. Faça um teste, digitando no *Terminal*: print "Python 2". Se o *Terminal* imprimir *Python 2* está tudo certo para começar a utilizar o software.

6. Para conferir qual é a versão do Python que você está utilizando no Rodeo, rode os comandos abaixo:
```[Python]
# Importando a funcao "python_version" do modulo "platform"
from platform import python_version

# Rodando e imprimindo a versao na tela:
print (python_version())
```
