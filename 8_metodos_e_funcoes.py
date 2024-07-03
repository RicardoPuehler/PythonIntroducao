#para a lista temos muitos metodos que podemos utilizar junto, como o append, insert, extend dentre outros, vamos ver cada um deles a seguir

lista = [1, 3 , 12, 8, 7]

#o metodo é uma funçao atrelada a uma variavel, vamos ver agora o append
print('antes do append', lista)

lista.append(5) #isso adciona um elemento ao final da lista

print('depois do append', lista)

#agora vamor ver o insert, ele assim como o append, adciona um novo elemento, mas na posiçao que voce quer

lista.insert(2, 55) #o primeiro numero é a posiçao que queremos adcionar, o segundo é o elemento a ser adcionado

print(lista)

#agora se tivermos mais listas, e quisermos adcionar outra lista junto a primeira lista, usamos o extend, que adciona os elementos da segunda lista ao final

lista2 = [1, 2, 3]

lista.extend(lista2) #dentro da lista, estou adcionando o lista 2.

print(lista)

#outro metodo é o pop, que apaga o ultimo elemento da lista

lista.pop() 

print('lista apos o pop', lista)

#se tu declarar uma posiçao no pop, ele vai eliminar o elemento na posiçao solicitada

lista.pop(0) # o 0 é o primeiro elemento

print('lista apos o pop', lista)

#temos tambem o remove, esse comando remove o elemento que voce quer apagar, nao na posiçao, mas na descriçao, e se tiver mais de 
#um elemento com o mesmo valor, ele vai apagar somento o primeiro com aquele valor

lista.remove(55)
print(lista)

#temos tambem o metodo count, que conta quantas vezes um elemento aparece na lista, veja o exemplo a seguir

lista3 = [1, 2, 3, 3, 3, 3, 4, 5]
print('o numero 3 aparece',lista3.count(3), 'vezes na lista3')

#temos o index, que da o indice de um determinado elemento na na lista, dai voce procura qual elemento voce esta procurando

print('o numero 8 esta no indice:',lista.index(8))

#para concluir sobre os metodos, vamos ver o metodo sort, ele serve para ordenar sua lista de forma crescente

lista.sort()
print(lista)
lista.sort(reverse=True)#com esse comando reverse=True, colocamos a lista no decrescente
print(lista)

#Vamos ver algumas funçoes, uma delas nós ja vimos que e a len, entao essa ja vamos pular

#vamos ver a sum, essa funçao soma todos os elementos da sua lista, vamos ver na pratica

print('soma dos elementos',sum(lista))

#a funçao max da o maior numero de sua lista, bem simples
print('maior elemento',max(lista))

#a funçao min da o menor valor da sua lista, tambem bem simples

print('menor elemento',min(lista))