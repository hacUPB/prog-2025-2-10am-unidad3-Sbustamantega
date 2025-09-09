'''
Crear una funcion llamada menu()
Parametros de entrada: Ninguno
Lo que realiza: Muestra un menu y muestra a el usuario que seleccione una opcion.
Valor de retorno: La opcion seleccionada
'''

def menu ():
    print ("1. entradas\n 2. fuertes\n 4. bebidas\n 3. postres\n 5. salir")
    opción = int(input("Elija una opcion: "))
    return opción

def entradas ():
    print("1. pandebono\t\t $3000")
    print("2. Empanada\t\t $3500")
    print("3. nachos \t\t $4000")
    
def fuertes ():
    print("1. Bandeja Paisa\t\t $20.000")
    print("2. changua\t\t       $15.000")
    print("3. solomo\t\t        $50.000")
    print("4. pollo a la plancha\t\t $25.000")
    print("5. mojarra frito\t\t $30.000")
    
def bebidas ():
    print("1. Cocacola\t\t $4000")
    print("2. limonada\t\t $3000")
    print("3. cerveza\t\t $5000")

def postres ():
    print("1. Pie de limon\t\t $4000")
    print("2. Postre de maracuya\t\t $3500")
    print("3. Helado\t\t $7000")
    print("4. Flan\t\t $6000")         


#funcion  principal

def main():
    eleccion = menu()  
    print (eleccion)

    match (eleccion):    
        case 1:
            entradas()
        case 2:
            fuertes()
        case 3:
            bebidas()
        case 4:
            postres()
        case _:
            print("opcion no valida")

#aqui se llama a la funcion principal
if __name__ == "__main__":
    main()