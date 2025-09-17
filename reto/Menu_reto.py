
#empezar haciendo un texto de bienvenida y codigo del menú
repetir_menu = "C"
while repetir_menu == "C":
      print("bienvenido al menu de problemas")
      print("a. Problema angulo de ataque\nb. problema de eficiencia en crucero\nc. problema de patron de espera\ns. salir")

      opcion = input("ingrese que programa desea usar: ")

      match opcion:
            case "a":
                  import math
                  print ("problema angulo de ascenso y descenso")
                  repetir = "R"

                  while repetir == "R":
                        etapa_vuelo = input("¿que etapa desea calcular? Ascenso (A), Descenso (D)").upper()
                        alt_final = float(input("ingrese la altitud a la que quiere llegar (ft)"))
                        alt_actual = float(input("ingrese su altitud actual (ft)"))
                        velocidad_aeronave = float(input("ingrese la velocidad de la aeronave (knots)"))* (6076 / 60)
                        distancia_destino = float(input("ingrese la distancia de destino (NM)"))* 6076
                        delta_altitud = alt_final - alt_actual
                        angulo = math.atan(abs(delta_altitud)/distancia_destino) * (180/math.pi)
                        
                  
                        if etapa_vuelo == "D":
                              print("Ángulo de descenso:",round(angulo, 2),"grados")
                              ajuste_razon = -(math.tan(math.radians(angulo)) * velocidad_aeronave)
                              if ajuste_razon > -2500:
                                    print("El descenso es seguro")
                                    print("la velocidad vertical seria: -", round(ajuste_razon, 2),"ft/min")
                              else :
                                    print("el descenso no es seguro, el descent rate sería:", round(ajuste_razon, 2),"ft/min")
                        
                        elif etapa_vuelo == "A":
                              print("Angulo de ascenso:", round(angulo, 2),"grados" )
                              if 0 <= angulo <= 25:
                                    print("el ascenso es seguro")
                                    ajuste_razon = math.tan(math.radians(angulo)) * velocidad_aeronave
                                    print("la velocidad vertical seria:", round(ajuste_razon, 2),"ft/min")
                              else:
                                    print("el ascenso no es seguro")
                        
                        repetir = input("si desea repetir el calculo ingrese (r) ").upper()

            




            case "b":
                  print("problema de eficiencia en crucero")







                  
            
            case "c": 
                  print("problema de patron de espera")
                  





            case "s":
                  print("saliendo del programa")  
            case _:
                  print("opcion no valida, por favor intente de nuevo.")
                  
      repetir_menu = input("si desea repetir el menu presione (c)").upper()