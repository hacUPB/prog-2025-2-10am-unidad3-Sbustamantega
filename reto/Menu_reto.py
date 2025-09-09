
#empezar haciendo un texto de bienvenida y codigo del menú

print("bienvenido al menu de problemas")
print("a. Problema angulo de ataque\n b. problema de ajuste de altitud\n c. problema de patron de espera\n s. salir")

opción = input("ingrese que programa desea usar: ")

match opción:
    case "a":
        print ("problema taza de descenso y ascenso")
        


         





























    case  "b":
        print("problema de ajuste de altitud")
        altitud = float(input("ingrese la altitud en metros: "))
       


    




















    case "c": 
        print("problema de patron de espera")
        aerop_alt = float(input("ingrese la distancia al aeropuerto alternativo en millas náuticas: "))
        combustible = float(input("ingrese el combustible disponible en kg: "))
        consumo_promedio_por_nm = 5  # Consumo promedio por milla náutica en kg
        reserva_combustible = 2000  # Reserva de combustible en kg
        consumo_por_minuto = 80  # Consumo por minuto en kg
        consumo_vuelo_alt = aerop_alt * consumo_promedio_por_nm
        combustible_disponible_espera = combustible - (consumo_vuelo_alt + reserva_combustible)
        if combustible_disponible_espera <= 0:
            decision = "Ir inmediatamente al aeropuerto alternativo"
            print(decision)
        else:
            tiempo_espera = combustible_disponible_espera / consumo_por_minuto
            decision = "Tiempo máximo de espera: " + str(tiempo_espera) + " minutos"
            print(decision)







    case "s":
        print("saliendo del programa")  
    case _:
        print("opcion no valida, por favor intente de nuevo.")