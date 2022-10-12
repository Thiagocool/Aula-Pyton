
import sys
from wsgiref.simple_server import sys_version

print("Versão do pyton")

print(sys.version)

print("informação da versão da instalação")
print(sys._version_info)


#programa converta metros em centimetros

print('\t ----conversão de medidas----')
metros = int(input('informe o valor em metros:'))
print('o valor em centimetro é:', metros *100 ,"CM" )



#Mostrar a tabuada de 1 a 10 

print('\t ----Tabuada----')
numero = int(input('informe o numero para ver a tabuada: '))

print('\n Tabuada de', numero, ":")

for i in range(1, 11):

    print(numero, "x" , i, '=' , (numero * i))
print(i*2)






    
