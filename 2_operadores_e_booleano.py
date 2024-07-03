# Vamos ver agora sobre operadores como soma e divigir, alem da aplicaçao do Boleano.
# Abaixo tem um comentario no modelo de declaração, entre """""", tudo que estiver dentro
# daquele intervalo, sera considerado um comentario igual o utilizando # 

"""
+ Soma
- Subtração
* Multiplicação
/ Divisão
// Divisão Inteira  
% Resto da Divisão
** Potencia
"""

# Vamos a pratica, vamos declarar algumas variaveis e vamos aplicar os valores e ver como fica os resultados
# para declarar mais de uma variavel na mesma linha, utilize o ponto e virgula;
num1 = 6; num2 = 3
print('num1 =', num1, 'e num2 =', num2)
# Veja como é simples, é só colocar o operador some as variaveis para executar a função

print(num1 + num2, 'Soma')
print(num1 - num2, 'Subtração')
print(num1 * num2, 'Multiplicação')
print(num1 / num2, 'Divisão')
print(num1 // num2, 'Divisão Inteira') # essa divisão considera só o valor do resultado antes do ponto, se o resultado desse 5.6, iria aparecer somente 5.
print(num1 % num2, 'Resto Divisão') # essa Resto, mostra um valor que sobraria de uma divisão inteira, tipo, se dividissemos 5 por 3, iria aparecer 2 que seria o resto, nao mais divisivel por 3.
print(num1 ** num2, 'Potencia')

# Vamos Ver os Boleanos, ele vai determinar se algo é True ou False, parece complicado mas
# ele só vai comparar as informaçoes e confirmar elas, segue exemplo abaixo.

"""
< Menor que
<= Menor ou igual que
> Maior que
>= Maior ou igual que
== Igual que
!= Diferente que
"""

idade1 = 20; idade2= 10; altura1= 1.80; altura2 = 1.70; altura3 = altura2

print(idade1 > idade2)
print(idade1 <= idade2)
print('Python' == 'python') # o python diferencia maiuscula de minuscula, por isso vai dar False aqui
print('banana' != 'abacaxi')
print(altura1 >= altura2)
print(altura2 < altura3)

