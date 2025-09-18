# Importa el módulo que contiene las funciones de cálculo
import funciones_reto as op_aero
import math

# Función principal para manejar el menú
def main():
    repetir_menu = "C"
    while repetir_menu == "C":
        print("--------------------------------")
        print("bienvenido al menu de problemas")
        print("a. Problema angulo de ataque\nb. problema de eficiencia en crucero\nc. problema de patron de espera\ns. salir")

        opcion = input("ingrese que programa desea usar: ").lower() # Convertir a minúsculas para consistencia

        match opcion:
            case "a":
                print("--------------------------------")
                print("problema angulo de ascenso y descenso")
                repetir = "r"
                while repetir == "r":
                    print("--------------------------------")
                    etapa_vuelo = input("¿que etapa desea calcular? Ascenso (A), Descenso (D)").upper()
                    alt_final = float(input("ingrese la altitud a la que quiere llegar (ft)"))
                    alt_actual = float(input("ingrese su altitud actual (ft)"))
                    velocidad_aeronave = float(input("ingrese la velocidad de la aeronave (knots)"))
                    distancia_destino = float(input("ingrese la distancia de destino (NM)"))
                    delta_altitud = alt_final - alt_actual

                    # Llamada a la función del módulo externo
                    angulo, velocidad_vertical = op_aero.calcular_ascenso_descenso(etapa_vuelo, alt_final, alt_actual, velocidad_aeronave, distancia_destino)
                    
                    if etapa_vuelo == "D":
                        print("--------------------------------")
                        print("Ángulo de descenso:", round(angulo, 2), "grados")
                        if velocidad_vertical > -2500:
                            print("El descenso es seguro")
                        else:
                            print("el descenso no es seguro, el descent rate sería:", round(velocidad_vertical, 2), "ft/min")
                    elif etapa_vuelo == "A":
                        print("--------------------------------")
                        print("Angulo de ascenso:", round(angulo, 2), "grados")
                        if velocidad_vertical <= 4500:
                            print("el ascenso es seguro")
                        else:
                            print("el ascenso no es seguro", "el climb rate seria:", round(velocidad_vertical, 2), "ft/min")

                    repetir = input("si desea repetir el calculo ingrese (r) ").lower()
            
            case "b":
                print("--------------------------------")
                print("problema de eficiencia en crucero")
                repetir = "r"
                while repetir == "r":
                    combustible_lb = float(input("ingrese el combustible en la aeronave (lb)"))
                    velocidad_kts = float(input("ingrese la velocidad en las aeronaves (kts)"))
                    altitud_ft = float(input("ingrese la altitud de crucero (ft)"))
                    viento_kts = float(input("ingrese viento en kts (positivo a favor, negativo en contra)"))
                    distancia_deseada = float(input("ingrese distancia al destino en NM"))
                    
                    # Llamada a la función del módulo externo
                    tiempo_horas, distancia_max, consumo_ajustado, velocidad_ef = op_aero.calcular_eficiencia_crucero(combustible_lb, velocidad_kts, altitud_ft, viento_kts, distancia_deseada)
                    
                    if velocidad_ef <= 0:
                        print("error, valores no validos. viento en contra excesivo")
                    else:
                        print("--------------------------------")
                        print("autonomia en horas:", round(tiempo_horas, 2), "h")
                        print("distancia maxima en NM:", round(distancia_max, 2), "NM")
                        print("consumo de combustible ajustado:", round(consumo_ajustado, 2), "lb/h")

                        if distancia_max >= distancia_deseada:
                            print("el vuelo es posible")
                        else:
                            print("vuelo no posible, busque un destino alternativo")
                    
                    repetir = input("si desea realizar otro calculo ingrese (r)").lower()
            
            case "c": 
                print("--------------------------------")
                print("problema de patron de espera")
                repetir = "r"
                while repetir == "r":
                    print("--------------------------------")
                    aerop_alt = float(input("ingrese distancia al aeropuerto alternativo (NM):"))
                    velocidad_prom = float(input("ingrese velocidad promedio de la aeronave (kts):"))
                    combustible = float(input("ingrese cantidad de combustible actual (lb):"))
                    altitud_espera = float(input("ingrese altitud en la que se realizara la espera (ft):"))
                    
                    # Llamada a la función del módulo externo
                    combustible_espera, tiempo_espera = op_aero.calcular_patron_espera(aerop_alt, combustible, velocidad_prom, altitud_espera)
                    
                    if combustible_espera <= 0:
                        print("Ir inmediatamente al aeropuerto alternativo")
                    else:
                        print("tiempo maximo de espera:", round(tiempo_espera, 2), "minutos o", round(tiempo_espera / 60, 2), "horas")
                    
                    repetir = input("si desea repetir el calculo ingrese (r)").lower()
            
            case "s":
                print("saliendo del programa")
                return # Salir de la función main()
            
            case _:
                print("opcion no valida, por favor intente de nuevo.")
                
        repetir_menu = input("si desea repetir el menu presione (c)").upper()

if __name__ == "__main__":
    main()