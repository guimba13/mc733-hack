# Matplotlib - Grupo 15

## O que faz? Para que serve?
Matplotlib é uma biblioteca de python utilizada para plotar figuras e gráficos. Com ela é possível gerar gráficos do tipo histogramas, spectros de potência, figuras, filtrar imagens, dentre outras funções. Essa biblioteca contém um módulo chamado pyplot que provê uma interface para Matlab. 
O script em python que importa esta biblioteca e será utilizado como benchmark realiza três funcionalidades:
- plota um gráfico e o salva como imagem do tipo jpg
- aplica diferentes filtros em uma determinada imagem salvando-a após a filtragem 
- calcula a multiplicação de uma matriz.

## Por que é bom para medir desempenho?
Com ela é possível executar algoritmos que exigem processamento excessivo para resolver problemas matemáticos e processamento de imagens, podendo, assim, avaliar o desempenho do processador. Além disso, também podemos, dessa maneira, da cache e da memória RAM.

## O que baixar
O código deste programa pode ser clonado do repositório a serguir: **git@bitbucket.org:RodrigoNMaximo/projeto1.git**

## Como compilar/instalar
Basta clonar o repositório acima e executar o script contido no mesmo, que cuida da instalação do matplotlib e das dependências necessárias. Essa instalação é realizada diretório atual do usuário.

## Como executar
É preciso apenas executar o script contido no repositório clonado.

## Como medir o desempenho
O desempenho é medido através de quatro parâmetros: o tempo de execução do script, a quantidade de branch misses, a quantidade de misses da cache L1 e da LLC Load.
O tempo medido é o tempo total de execução, uma vez que ele representa a capacidade de processamento do processador da máquina utilizada. Esse tempo é obtido a partir da média de tempos de três execuções utilizando-se da ferramenta perf. Além disso, esta ferramenta também foi utilizada para medir os outros três parâmetros citados acima. 

## Como apresentar o desempenho
O desempenho será apresentado através da criação de uma fórmula que prioriza o tempo de execução pelo fato de que os parâmetros acima estão atrelados a este, ou seja, se o tempo de execução é elevado, isso afetará o desempenho da cache e também poderá afetar o número de branch misses.
A fórmula utilizada tenta fazer com que os quatro parâmetros possuam a mesma ordem de grandeza, por isso a divisão de cada parâmetro com base aos valores medidos para a máquina que utilizamos. Além disso, consideramos um peso 3 para o tempo de execução para priorizá-lo e tomamos a média destes 4 valores.

Desempenho = (Tempo de execução * 30 + Cache Misses/10^7 + Branch Misses/10^7 + LLC Load Misses/10^6) / 6

## Medições base (uma máquina)
Os valores para os quatro parâmetros acima obtidos através do perf para a máquina clash(lab-ic) estão na tabela abaixo:

|Tempo médio(s)|Desvio Padrão(s)|Cache Misses L1(#)|Desvio Padrão (%)|Branch Misses (#)|Desvio Padrão (%)|LLC Load Misses (#)|Desvio Padrão (%)|
|--------------|----------------|------------------|-----------------|-----------------|-----------------|-------------------|-----------------|
|   105.95     |     0.36       |   8,226,009,812  |        0.30     |  4,482,091,759  |      0.20       |    891,916,040    |       0.28      |

O score é dado por um número de 0 a 5000, sendo ele calculado pela equação de Desempenho acima. Quanto maior o score obtido, pior é o desempenho da máquina avaliada com este benchmark. Valores obtidos com essa equação acima de 5000, foram setados para 5000. 

Desempenho obitdo para a máquina utilizada foi de 890.

