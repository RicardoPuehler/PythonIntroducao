# Estrutura condicionais são estruturas que, a um determinado resultado ou desição, nos leva a outros objetivo, como por exemplo um login
# se vo coloca o login e senha corretos, voce se conecta a uma conta, porem caso nao o faça corretamente, um erro aparece e voce não é 
# redirecionado para a conta que voce esta tentando conectar.

# Para se ter uma boa estrutura condicional, é muito indicado que uma estrutura de fluxo seja montada, para que voce possa fazer a codificação
# corretamente, como se fosse um mapa, essa estrutura de fluxo é chamado de fluxograma.

#para uma estrutura condicional pratica, voce aplica uma comparação, vamos utilizar nesse caso o if e o else. veja abaixo um exemplo dessa estrutura

idade = int(input('qual a sua idade?' ))

if idade >= 18: #o if em traduçao direta significa 'Se', nesse caso eu quero saber se a idade é maior ou igual a 18, se for, ele imprime a mensagem abaixo
    print('Você é maior de Idade!')

else: #o else em traduçao direta significa 'Se não', se a solicitaçao anterior nao responder ao esperado, ele vai responder a mensagem abaixo.
    print('Você é menor de Idade!')

"""
O Se e o Senão me da duas possibilidades de caminho, porem em um fluxograma eu tenho muitos mais caminhos possiveis, para estes casos 
eu vou utilizando o elif, que seria como 'E se', tipo: Se x, E Se xx, E Se xy, Senão yy, sempre começando a condiçao com Se e terminando com Se Não.
"""

# Entendendo a explicaçao acima, vamos a um exemplo pratico, a media de notas nesse caso

nota1 = float(input('primeira nota: '))
nota2 = float(input('segunda nota: '))
nota3 = float(input('terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

if media >= 7: #um detalhe, apos a condiçao, no if, elif e else tem que haver os ':' dois pontos
    print('voce foi APROVADO')

elif media >= 5:
    print('voce esta de RECUPERAÇÃO')

else:
    print('voce esta REPROVADO')

"""
Quando eu quero colocar mais condiçoes para ocorrer em cada etapa da vericaçao, eu coloco cada condição separado pela palavra 'and'
o and é a condiçao E.
isso quer dizer, por exemplo, se um aluno tirar mais de 7 E tiver mais de 75% de presença, ele da uma condiçao que tem que respeitar Ambas as solicitaçoes.
alem do and, temos o 'or', que em ingles significa Ou, que precisa que uma das ocasioes ocorram, ou tenha a nota ou a presença para que a condiçao ocorra.
"""