#primeiro codigo
print("Hello World") 
#primeira variavel 
texto = 'Tudo de Boas?'
#mostrando a utilização da variavel / obs: texto sempre entre aspas
print(texto)

#Tipos de variaveis, iniciar sempre com minuscula:
# int : numeros inteiros, sem ponto, positivo ou negativo.
# float: numeros reais, com ponto, positivo ou negativo
# str : tambem conhecida como string, é o texto.
# bool: é o famoso Boleano, True ou False.

#segue exemplos abaixo

idade = 30 # Variavel tipo int.
altura = 1.90 # Variavel tipo float.
nome = 'Ricardo Puehler' # Variavel tipo str
estudando = True # Variavel do tipo bool

# O comando type mostra qual o tipo da variavel.
print( type(idade)) 
print( type(altura))
print( type(nome))
print( type(estudando))

# para obter algo escrito do usuario, utilizamos o input, exemplo abaixo

linguagem = input('Qual Linguagem de Progamaçao tu estuda? ')

# para imprimir mais de um conteudo por vez, tu coloca uma virgula e coloca 
# uma variavel que voce quer que seja atribuida junto, exemplo abaixo

print('Que legal que tu estuda ', linguagem)