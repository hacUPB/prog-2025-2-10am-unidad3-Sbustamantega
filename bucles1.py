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



'''''''''''''''
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
'''''''''

'''''''''
# otro ejemplo
bunero = int(input("Ingrese el numero de los terminos de la serie: "))
if numero <= 0:
    print("Ingrese un numero entero positivo")
elif numero == 1:
    print("Serie de Fibonacci hasta")
    print(0)
else:
    a=0
    b=1
    contador = 2
    print("Serie de Fibonacci:")
    print(a)    
    print(b)
    while contador < numero:
        siguiente = a + b
        print(siguiente)
        a = b
        b = siguiente
        contador += 1

'''''''''
'''''''''''''''
#ejercicio de la tabla de multiplicar

numero = int(input("Ingrese un numero entero positivo:"))
contador = 1

while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1
'''''''''
    
'''''''''
#ejercicio con range
#no se puedne ingresar negativos y no puede pasar hasta que se ingrese un positivo

n = int(input("Ingrese un numero entero positivo:"))
while n < 1:
     n = int(input("Error. Ingrese un numero entero positivo:"))

suma = 0
for n in range (1, n+1 , 1):
    if n % 2 == 0:
     suma += n
print(f"La suma de los pares entre 1 y {n}: {suma}")

 '''''



#que se imprima un mensaje un numero determinado de veces
mensaje = "Universidad Pontificia Bolivariana"
numero = int(input("Ingrese un numero entero positivo:"))
while numero < 1:
     numero = int(input("Error. Ingrese un numero entero positivo:"))
for _ in range (1, numero + 1, 1):
    print(f"{mensaje}")