#assim como outros codigos, existem modulos que podem ser importados, no caso eu importei o modulo time (tempo). só para aplicar a uma condiçao.

import time 


# O While é um tipo de laço de Repetiçao, significa Enquanto, quer dizer que enquanto tal açao esta ocorrendo ela continua ocorrendo.
# vamos para um exemplo simples, vamos definir que o usuario deve acertar um numero, se o mesmo errar o numero que queremos que ele acerte
# ele devera tentar novamente.

numero_sorteado = 8

numero_escolhido = int(input('informe um numero de 1 a 10: '))

while numero_escolhido != numero_sorteado:
    print('Errou, tente denovo')
    numero_escolhido = int(input('informe um numero de 1 a 10: ')) #Tem que colocar a funçao novamente para que o usuario possa tentar, caso contrario o programa entra em loop infinito

# tudo que estiver, como se diz, para 'frente'do while, vai ocorrer dentro dele, se eu conseguir sair do laço de repetiçao e querer que o codigo
# de sequencia eu devo fazer com que a coluna que esteja iniciando esteja na mesma linha do while

#exemplo:
# while:
#      o que vai ocorrer enquanto while funcionar
# o que vai ocorrer quando o while acabar

"""
essa jogada para frente ocorre sempre que uma condiçao é importa, e o que estiver dentro dessa jogada para frente vai sempre ocorrer 
naquela condiçao, tando para o if, elif, else, while, for... assim que o python interpreta o codigo, sempre que acabar e dar sequencia na
condiçao, lembrar de 'apagar' esse espaçamento extra que é gerado, afim de indicar que o que esta sendo passado agora nao pertence a
aquela condiçao.
"""

#vamos a um exemplo de while para uma repetiçao de contador

contador = 0

while contador <= 10: #enquanto contador for menor = a dez faça...
    print(contador)
    contador = contador + 1
    time.sleep(5.0) #isso faz que cada while ocorra a cada 5 segundos :)
print('Terminooooou uhuul!')

