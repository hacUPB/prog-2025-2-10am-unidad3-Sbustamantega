# solicitar al usuario dos cumeros e imprimir los pares entre ellos
''' ''''''''''''''''''''
numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el segundo numero: "))     
if numero_1 > numero_2:
    mayor = numero_1
    menor = numero_2
else:
    mayor = numero_2
    menor = numero_1    

while menor <= mayor:
    if menor % 2 == 0:
        print(menor)
    menor += 1

'''''''''''''''''

#calculadora




control = True

while control : True
    num1 = int(input("Ingrese el primer numero "))
    num2 = int(input("Ingrese el segundo numero "))
 print("S. sumar\n R. resta\n M. multiplicacion\n D. division\n E. salir")
 opcion = input("elija una opcion: ")
    match opcion:
        case "S":
            print("modo seleccionado sumar")
            resultado = num1 + num2
        case "R":
            print("modo seleccionado resta")
            resultado = num1 - num2
        case "M":
            print("modo seleccionado multiplicacion")
            resultado = num1 * num2
        case "D":
            if numero_2 != 0:
                print("modo seleccionado division")
                resultado = num1 / num2
        case "E":
            control = False
        case _:
            print("Opcion no valida")
    
 print(f"El resultado es:{resultado}")
:                   
