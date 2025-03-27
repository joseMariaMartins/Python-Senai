numero1 = input('Digite um número:')
numero2 = input('Digite outro número:')

print(f'A soma dos números é {numero1 + numero2}')

# Função TYPE()
# String = Texto
# Int = Intiger -> Número inteiro
# Float = Número decimal (Número com ponto flutuante)

print( type('5') )
print( type(5) )
print( type(5.5) )

numero = input('Digite um numero')
type( numero )

# Converter números em Python
# Int('5') - Converte de texto para número inteiro
# float('5') - Converte de texto para número de ponto flutuante
# Str('5') - Converte de texto para Booleano

# Número inteiro - int()
a = int('5')
type(a)

# Número decimal - float()
b = float('5')
type(b)

# Texto - str()
c = str('5')
type(c)

# Booleano - bool()
d = bool('Verdadeiro')
type(d)

x = int('8')
y = int('7')
print( x + y )

# 02 Resolução
numero1 = input('Digite um número')
numero2 = input('Digite um número')

# Sobrescreve o valor da variável
numero1 = int(numero1)
numero2 = int(numero2)
res = numero1 + numero2

print(res)

numero1 = int( input('Digite um número') )
numero2 = int ( input('Digite um número') )
res = int( numero1 + numero2 )

print(res)
type(res)