# a Repetiçao For significa Para, cria uma repetiçao dentro de uma estrutura.

for variavel in range(10): #para uma determinada variavel dentro de uma faixa de 0 a 9, execute tal codigo
    print(variavel)
    
#a funçao range começa em 0, e vai até o numero que colocou -1, por isso imprimou até o numero 9
#se quiser que ele execute iniciando apartir do 1, voce pode colocar de qual numero ele vai iniciar
print('contando de 1 a 10')
for variado in range (1, 11):
    print(variado)

#se tu coloca só um numero no range, ele vai fazer aquela quantidade de range
#se tu coloca duas, ele começa no numero que tu indicou e vai até o numero que tu colocou-1
#se tu coloca 3 numeros, o terceiro é a quantidade de numero que ele vai pular, exemplo abaixo

for pular in range (0, 100, 5):
    print(pular)

#mas isso é aplicado tambem junto a input ou outras funçoes. vamos fazer agora com um input para o usuario ir preenchendo

soma = 0 #declarei essa variavel para mostrar uma funçao de somar valores dentro do for.

for i in range(1, 4):
    nota = float(input(f'informe sua nota {i}: ')) #para adcionar uma variavel a uma string, voce antes dos aspas coloca o f, e a variavel entre chaves

    soma = soma + nota

print('a soma dos valores informados é ', soma)
print('a sua media ficou em: ', soma/3)