#!/usr/bin/env python3

# Importando biblioteca para poder usar função sys.argv e sys.exit()
import sys

# Recebendo os argumentos do usuário e transformando em string para utilizar o método .isdigit()
a = str(sys.argv[1]) # sys.argv é usado para receber a entrada do usuário
b = str(sys.argv[2])

# Verificando se os argumentos recebidos são números inteiros
if not a.isdigit():
 print ("Valor dado para o argumento \'a\' deve ser um número inteiro positivo")
 sys.exit() # sys.exit() é usado para interromper a execução do script caso os argumentos não atenderem às condições

if not b.isdigit():
 print ("Valor dado para o argumento \'b\' deve ser um número inteiro positivo")
 sys.exit()

# Transformando os argumentos em inteiros novamente
a = int(a)
b = int(b)

# Verificando se os argumentos estão dentro do intervalo estabelecido
if a <= 0 or a >= 500:
 print ("Valor dado para o argumento \'a\' deve ser um inteiro positivo menor que 500")
 sys.exit()

if b <= 0 or b >= 500:
 print ("Valor dado para o argumento \'b\' deve ser um inteiro positivo menor que 500")
 sys.exit()

# Calculando o quadrado da hipotenusa a partir da Fórmula de Pitágoras
quad_hipotenusa = a**2 + b**2

# Imprimindo o resultado para o usuário
print ("O quadrado da hipotenusa para o triângulo retângulo com lados a=" , a , "e b=" , b, "é", quad_hipotenusa)



