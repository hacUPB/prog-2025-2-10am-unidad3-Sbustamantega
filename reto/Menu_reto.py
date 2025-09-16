
#empezar haciendo un texto de bienvenida y codigo del menú

print("bienvenido al menu de problemas")
print("a. Problema angulo de ataque\n b. problema de ajuste de altitud\n c. problema de patron de espera\n s. salir")

opción = input("ingrese que programa desea usar: ")

match opción:
    case "a":
        print ("problema taza de descenso y ascenso")
        repetir = "r"

        while repetir = "r"
            alt_final = 
        
        


         


'''''''''
INICIO

mientras repetir = "r"

      leer alt_final
      leer distancia_destino
      leer velocidad_aeronave      
      distancia_destino = distancia_destino * 6076
      delta_altitud = alt_final - alt_actual
      angulo = arctan( |delta_altitud| / distancia_destino ) * (180 / π)

      

      Si etapa_vuelo = "D"
            escribir "Ángulo de descenso:", angulo, "grados"
            SI angulo >= 3 Y angulo_descenso <= 6 :
                  escribir "El descenso es SEGURO."
                  ajuste_razon = tan(angulo * π / 180) * velocidad_aeronave * 101.27    \\ aqui se uso la ia en el metodo para el angulo de descenso
                  ESCRIBIR "Razón de descenso:", ajuste_razon, "ft/min"
            SINO
                  escribir "El descenso NO es seguro." 
            FIN SI
      si no 
            escribir "Ángulo de Ascenso:", angulo, "grados"
            SI angulo >= 10 Y angulo_descenso <= 25 ENTONCES
                  escribir "El ASCENSO ES SEGURO."
                  ajuste_razon = tan(angulo * π / 180) * velocidad_aeronave * 101.27
                  ESCRIBIR "Razón de ascenso:", ajuste_razon, "ft/min"

            SINO
                  escribir "El ascenso NO es seguro."

            Fin si
      Fin si
      escribir "si desea repetir el proceso (r), si no (n)"
      leer repetir
FIN MIENTRAS

FIN
'''''''''





















    case  "b":
        print("problema de ajuste de altitud")
        
        altitud = float(input("ingrese la altitud en metros: "))

       


    




















    case "c": 
        print("problema de patron de espera")
       





    case "s":
        print("saliendo del programa")  
    case _:
        print("opcion no valida, por favor intente de nuevo.")