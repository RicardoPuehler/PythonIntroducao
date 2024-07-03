# Vamos falar sobre Listas, é uma estrutura de Dados list(), é uma variavel que consegue armazenar varias tipos de variaveis dentro dela
#nela, ao inves de parenteses(), voce utiliza conchetes[]

"""
sem lista, para ter tres variaveis de notas, teriamos que criar as 3 
ex:
nota1 = 57
nota2 = 55 
nota3 = 64

com lista fica mais facil, como no exemplo abaixo, utilizando virgula para separar as informaçoes.

notas = [57, 55, 64]

toda variavel que for com [] sera uma lista, mesmo que vazia
"""

# Vamos a um exemplo pratico abaixo

notas = [5.6, 6.5, 7.7]
lista = []
lista = list() #esse é o lista de cima, é uma lista vazia
exemplo = [30, "Ricardo Puehler", 1.90, 150, True] #voce pode colocar qualquer tipo de variavel nela
lista_de_lista = [10, [90, 50]] #é possivel fazer uma lista de listas


#nós temos um termo falado Indexação, que é a palavra para dizer que estamos acessando um elemento atravez de um indice
#tipo, acessar o primeiro elemento de da lista
#exemplo a seguir

print(exemplo[0]) #o python sempre começa a contar pelo 0, então o primeiro item da lista é o item na posiçao 0
print(exemplo[-1]) #o -1 é o ultimo item da lista, -2 o penultimo, e assim sucessivamente
print(exemplo[0:3]) #colocando com dois pontos :, ele pega os itens da lista dentro daquele intervalo

#vamos utilizar um for para imprimir todos os elementos da lista? para isso é simples, segue o exemplo

for elemento in notas:
    print(elemento)

#existe tambem uma funçao muito legal para voce descobrir quantos elementos tem dentro de uma lista, essa funçao é o len
#utilize junto ao print para ele te mostrar essa info

print('voce tem um total de', len(exemplo), 'elementos na sua lista')

#o len tambem serve para voce saber quantos caracteres, contando o espaço, tem em uma str, como no exemplo abaixo.
texto = 'Muitas Pessoas'

print(len(texto))