#el profucto final con funciones esta en codigo_reto.py
#empezar haciendo un texto de bienvenida y codigo del menú
repetir_menu = "C"
while repetir_menu == "C":
      print("--------------------------------")
      print("bienvenido al menu de problemas")
      print("a. Problema angulo de ataque\nb. problema de eficiencia en crucero\nc. problema de patron de espera\ns. salir")

      opcion = input("ingrese que programa desea usar: ")

      match opcion:
            case "a":
                  import math
                  print("--------------------------------")
                  print ("problema angulo de ascenso y descenso")
                  repetir = "R"

                  while repetir == "R":
                        print("--------------------------------")
                        etapa_vuelo = input("¿que etapa desea calcular? Ascenso (A), Descenso (D)").upper()
                        alt_final = float(input("ingrese la altitud a la que quiere llegar (ft)"))
                        alt_actual = float(input("ingrese su altitud actual (ft)"))
                        velocidad_aeronave = float(input("ingrese la velocidad de la aeronave (knots)"))* (6076 / 60)
                        distancia_destino = float(input("ingrese la distancia de destino (NM)"))* 6076
                        delta_altitud = alt_final - alt_actual
                        angulo = math.atan(abs(delta_altitud)/distancia_destino) * (180/math.pi)
                        
                  
                        if etapa_vuelo == "D":
                              print("--------------------------------")
                              print("Ángulo de descenso:",round(angulo, 2),"grados")
                              ajuste_razon = -(math.tan(math.radians(angulo)) * velocidad_aeronave)
                              if ajuste_razon > -2500:
                                    print("El descenso es seguro","la velocidad vertical seria: -", round(ajuste_razon, 2),"ft/min")
                                    
                              else :
                                    print("el descenso no es seguro, el descent rate sería:", round(ajuste_razon, 2),"ft/min")
                        
                        elif etapa_vuelo == "A":
                              print("--------------------------------")
                              print("Angulo de ascenso:", round(angulo, 2),"grados" )
                              ajuste_razon = math.tan(math.radians(angulo)) * velocidad_aeronave
                              if ajuste_razon <= 4500:
                                    print("el ascenso es seguro", "la velocidad vertical seria:", round(ajuste_razon, 2),"ft/min")
                                    
                              else:
                                    print("el ascenso no es seguro", "el climb rate seria:", round(ajuste_razon, 2),"ft/min")
                        
                        repetir = input("si desea repetir el calculo ingrese (r) ").upper()

            

            case "b":
                  print("--------------------------------")
                  print("problema de eficiencia en crucero")
                  repetir = "R"
                  while repetir == "R":
                        combustible_lb = float(input("ingrese el combustible en la aeronave (lb)"))
                        velocidad_kts = float(input("ingrese la velocidad en las aeronaves (kts)"))
                        altitud_ft = float(input("ingrese la altitud de crucero (ft)"))
                        viento_kts = float(input("ingrese viento en kts (positivo a favor, negativo en contra)"))
                        distancia_deseada = float(input("ingrese distancia al destino en NM"))

                        consumo_base = 6000  #consumo en lb/horas
                        factor_reduccion = (altitud_ft / 1000) * 0.005
                        consumo_ajustado = consumo_base * (1 - factor_reduccion)

                        if consumo_ajustado < 1000:
                              consumo_ajustado = 1000
                        
                        tiempo_horas = combustible_lb/consumo_ajustado
                        velocidad_ef = velocidad_kts + viento_kts

                        if velocidad_ef <= 0:
                              print("error, valores no validos. viento en contra excesivo")
                        
                        else:
                              distancia_max = velocidad_ef * tiempo_horas
                        
                        print("autonomia en horas:", round(tiempo_horas, 2),"h")
                        print("distancia maxima en NM:", round(distancia_max, 2),"NM")
                        print("consumo de combustible ajustado:", round(consumo_ajustado, 2),"lb/h")

                        if distancia_max >= distancia_deseada:
                              print("el vuelo es posible")
                        else:
                              print("vuelo no posible, busque un destino alternativo")
                        
                        repetir = input("si desea realizar otro calculo ingrese (r)").upper()

                  
            
            case "c": 
                  
                  print("problema de patron de espera")
                  repetir = "R"
                  while repetir == "R":
                        print("--------------------------------")
                        aerop_alt = float(input("ingrese distancia al aeropuerto alternativo (NM):"))
                        velocidad_prom = float(input("ingrese velocidad promedio de la aeronave (kts):"))
                        combustible = float(input("ingrese cantidad de combustible actual (lb):"))
                        altitud_espera = float(input("ingrese altitud en la que se realizara la espera (ft):"))
                        
                        reserva_combustible = 15000 #reserva minima obligatoria en lb
                        consumo_por_minuto = 55  #consumo en lb/min
                        consumo_base_por_hora = 6000 #consumo en lb/h

                        factor_reductor = (altitud_espera / 1000) * 0.005
                        consumo_ajustado_h = consumo_base_por_hora * (1 - factor_reductor)
                        
                        if consumo_ajustado_h < 1000:
                              consumo_ajustado_h = 1000
                        
                        tiempo_vuelo = aerop_alt / velocidad_prom
                        consumo_alternativo = tiempo_vuelo * consumo_ajustado_h
                        combustible_espera = combustible - (consumo_alternativo + reserva_combustible)

                        if combustible_espera <= 0:
                              print("Ir inmediatamente al aeropuerto alternativo")
                        
                        else:
                              tiempo_espera = combustible_espera / consumo_por_minuto
                              print("tiempo maximo de espera:", round(tiempo_espera, 2),"minutos o", round(tiempo_espera/60, 2),"horas")

                        repetir = input("si desea repetir el calculo ingrese (r)").upper()
                  

            case "s":
                  print("saliendo del programa")  
            case _:
                  print("opcion no valida, por favor intente de nuevo.")
                  
      repetir_menu = input("si desea repetir el menu presione (c)").upper()