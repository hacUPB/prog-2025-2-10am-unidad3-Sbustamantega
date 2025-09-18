from mod_reto import *
# menu principal
repetir_menu = "C"
while repetir_menu == "C":
      print("--------------------------------")
      print("bienvenido al menu de problemas")
      print("a. Problema angulo de ataque\nb. problema de eficiencia en crucero\nc. problema de patron de espera\ns. salir")

      opcion = input("ingrese que programa desea usar: ")

      match opcion:
            case "a":
                  problema_descenso()
            case "b":
                  problema_eficiencia_crucero()
            case "c": 
                 problema_patron_espera()
            case "s":
                  print("saliendo del programa")  
            case _:
                  print("opcion no valida, por favor intente de nuevo.")
                  
      repetir_menu = input("si desea repetir el menu presione (c)").upper()