#!/usr/bin/env python3

# Importando biblioteca para poder usar função sys.argv e sys.exit()
import sys

# Recebendo os argumentos do usuário e transformando em string para utilizar o método .isdigit() e .isalpha()
dna = str(sys.argv[1]) # sys.argv é usado para receber a entrada do usuário
dna = dna.upper() # Convertendo a sequência para maiúsculas
n1 = str(sys.argv[2])
n2 = str(sys.argv[3])
n3 = str(sys.argv[4])
n4 = str(sys.argv[5])
n5 = str(sys.argv[6])
n6 = str(sys.argv[7])

# Verificando se os argumentos recebidos são do tipo correto
if not dna.isalpha():
 print ("Erro: A sequência de DNA deve ser composta somente por letras") # .isalpha() percorre a string para ver se ela é composta somente por letras
 sys.exit() # sys.exit() é usado para interromper a execução do script caso os argumentos não atenderem às condições

if not (n1.isdigit() and n2.isdigit() and n3.isdigit() and n4.isdigit() and n5.isdigit() and n6.isdigit()):
 print ("Erro: Valor dado para os argumentos n1, n2, n3, n4, n5 e n6 devem ser números inteiros positivos") # .isdigit() verifica se a string tem somente números
 sys.exit()

# Convertendo os números para inteiros
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
n4 = int(n4)
n5 = int(n5)
n6 = int(n6)

# Verificando se nenhum dos inteiros é maior que a sequencia de dna
numero_maximo = max(n1, n2, n3, n4, n5, n6)

if len(dna) < numero_maximo:
 print ("Erro: Os valores fornecidos não podem ser maiores que a sequência de dna")
 sys.exit()

# Extraindo CDS 1 da sequência de DNA e conferindo se inicia com códon ATG

CDS1 = dna [n1-1 : n2] # Necessário subtrair 1 para igualar índice com número da base de DNA
if dna[n1-1 : n1+2] != "ATG" :
 print ("Erro: CDS 1 deve iniciar com o códon ATG")
 sys.exit()

# Extraindo CDS 2 da sequência de DNA
CDS2 = dna [n3-1 : n4]

# Extraindo CDS 3 e conferindo se termina com algum dos 3 códons de parada. Caso verdadeiro, poderemos concatenar as três CDS.
CDS3 = dna [n5-1 : n6]
if dna[n6-3 : n6] == "TAG" or dna[n6-3 : n6] == "TAA" or dna[n6-3 : n6] == "TGA":
 print (CDS1 + CDS2 + CDS3)
else:
 print ("Erro: CDS 3 deve finalizar com um dos códons de parada - TAG / TAA / TGA")


