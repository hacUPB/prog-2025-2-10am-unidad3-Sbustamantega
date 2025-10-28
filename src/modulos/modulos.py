

'''''''''
#Función principal
numero = int(input("Ingrese un número entero mayor que 1: "))
primo(numero)
variable = int(input("Ingrese el número de términos de la serie de Fibonacci: "))
fibonacci(variable)
multiplicando = int(input("Ingrese el número entero: "))
tabla(multiplicando)
 
'''''''''

from modulos.mod_funciones import *
def main():
   while True:
      opc = menu()
      
      match opc:
         case 1:
            print("calcula si un numero es primo")
            valor= int(input("ingresa un valor mayor que 1 >>"))
            primo(valor)

         case 2:
            print("imprime la serie de fibonacci")
            valor= int(input("ingresa el numero de  terminos >>"))
            fibonacci(valor)
        
         case 3:
            print("imprime tabla de multiplicar")
            valor= int(input("ingresa un valor mayor que 1 >>"))
            tabla(valor)
         
         case 4:
            break
         
         case _ :
            print("opcion invalida")
            
            