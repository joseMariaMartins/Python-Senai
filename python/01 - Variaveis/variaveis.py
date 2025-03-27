# String = Texto
a = 3
b = 7
print(f'O alor do valor da variável A é {a} e o valor da variável B é {b}')
# Regra 1 Iniciar com a Letra F
# Regra 2 Demarcar as Variáveis com {}
# Esse 'f' indica pro python q vai ter interpolação naoquela linha

nome = input('Digite seu nome')
print(f'Ola {nome}, Seja Bem Vindo')

# Numweo com casas decimais 
# Float os numeros tem que ser com um ponto '.'
print(10.99)

# O Python permite meter os underline para facilitar a leitura de numeros extensos
var = 10_000_000
print(var)


f'{1.111113332: .3f}'

# Arredondando valores decimais -f'{}' : .n
print(f'{1.111111: .2}')
print(f'{1.111111: .3}')
print(f'{1.111111: .4}')

# Arredondando valores decimais - roud()
round(1.2345, 3)

var1 = 1.112223
var2 = round( var1, 2)
print(var2)

divisao = 10 / 3
round( divisao, 2 )

preco = 15.2313131313131

print(f'Valor total: { round(preco, 2) }')

nome = 'Julia'
idade = 15
cidade = 'Sorocaba'

print(f'''ALUNO:
Nome: {nome}
Idade: {idade}
Cidade: {cidade}
''')

# O método float()do Python irá converter inteiros em floats.
# Para usar essa função, adicione um inteiro entre parênteses:
# O Python também possui uma função integrada para converter floats em inteiros: int().
# Neste caso, 390.8será convertido em 390.
# 