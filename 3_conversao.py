# Vamos ver aqui sobre Conversão de Tipos de Variaveis.

# Vamos a um exemplo abaixo, que vamos converter str para int, vou declarar numeros sobre '' para o python reconhecer
# como um texto.

idade = '20'
numero1 = '50'
numero2 = '100'

# para confirmar, vou mandar um type para ele mostrar o tipo da variavel, no terminal deve aparecer <class 'str'>.

print( type(idade)) 
print( type(numero1))
print( type(numero2))

# se eu tentar fazer uma operação por exemplo, ele nao vai somar os valores, mais vai juntar eles, deixando concatenados.

print (numero1 + numero2) # ao invez de somar dando o resultado de 150, ele vai dar o valor de 50100, pois somando texto ele concatena.

# para converter, devemos declarar o tipo de variavel que queremos aplicar, nesse caso vai ser int, veja abaixo um exemplo:
# quando vamos fazer uma variavel com mais de uma palavra, deve ter o underline separando ela, espaço ocasiona erro.
idade_inteiro = int(idade)

#abaixo para teste, o resultado deve aparecer o numero, e o tipo dela deve aparecer <class 'int'>
print(idade_inteiro, type(idade_inteiro))

"""
Esse tipo de conversão feita anteriormente é chamada de Conversão Explicita, o qual eu faço manualmente declarando uma variaçao e falando
diretamente o que eu quero que ocorra, no caso converter os numero que estao em str para int.
a conversão dara errado caso tenha letras, por exemplo, se ao invez do numero, tivesse a palavra falando o numero (50 = cinquenta)

no caso em questão, eu converti um str() para int(), porem é possivel fazer tambem para str(), float() e bool() que são os tipos de variaveis
existentes.
"""
# se eu colocar um input para o usuario preencher e não declarar qual vai ser o tipo de dado recebido, mesmo se o usuario digitar um numero
# o mesmo sera considerado como str().
# para isso, podemos ja declarar qua o tipo variavel que vai ser inserido, deixando o input dentro da tipo de variavel, exemplo abaixo

altura = float(input('qual sua altura? ')) #veja que o float esta 'abraçando'o input, se eu tentar declarar algo com letra vai dar erro

# detalhe, numero que para nós seriam com ','virgula devem ser posto com '.' ponto, pois o sistema americano é o inverso do nosso nesse sentido.

"""
Essa conversão é mais pratica, ja que voce limita qual tipo de variavel voce precisa colocar, assim deixando o codigo
mais limpo e rapido, com menos linhas de codigo.
"""