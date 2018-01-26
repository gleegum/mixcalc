"""calculadora mezcla aceite/nafta 2T
"""
import os
#limpia pantalla
os.system('cls||clear')

#titulo
title = '**** calculadora mezcla aceite/nafta 2T ****'
print(str.upper(title))

#ingreso de datos
ratio = int(input('Ingrese la relación de mezcla, ej: 50 para 50:1 \n'))
print(str(ratio)+str(':1'))
gas = float(input("ingrese la cantidad de nafta a preparar \n"))

#lineas de impresión
to = 'Para preparar'
gasAdd = 'de combustible debe agregar'
grs = 'gramos de aceite.'
#cálculo
oil = (gas / ratio)*1000

#litros cambia a litro si se ingresa 1
liter = 'litros'
if int(gas) is 1:
    liter = 'litro'
else:
    liter = 'litros'

#imprime resultado
print(to, str(gas), liter, gasAdd, str(int(oil)), grs)
