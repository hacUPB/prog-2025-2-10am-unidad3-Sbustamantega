##tarea
| Operador | Explicación                          |
| -------- | ------------------------------------ |
| +      | Suma                                 |
| -      | Resta                                |
| *      | Multiplicación                       |
| /      | División decimal                     |
| //     | División entera (descarta decimales) |
| %      | Módulo (residuo)                     |
| **     | Potencia                             |


| Operador | Explicación   |
| -------- | ------------- |
| ==     | Igual a       |
| !=     | Diferente de  |
| >      | Mayor que     |
| <      | Menor que     |
| >=     | Mayor o igual |
| <=     | Menor o igual |







print("Ingresa tu nombre y apellido")
nombre = input ()
print("Bienvenido: ")
print(nombre)
#Opción 2
print("Bienvenido: ", nombre)
#Calcular el IMC de esa persona
#Leer peso, altura
peso = input ("Ingresa tu peso en kg: ")
peso = float(peso)
altura = input ("Ingresa tu talla en metros: ")
altura = float(altura)
#Cálculos
imc = peso/altura**2
#Mostrar imc
print("Tu IMC= ", imc)

if imc < 18.5:
  mensaje = "Bajo peso"
elif imc < 25:
  mensaje = "Peso normal"
elif imc < 35:
  mensaje = "obesidad tipo 1"
elif imc < 40:
  mensaje = "obesidad tipo 2"
else:
  mensaje = "obesidad extrema"

Print (f"paciente {nombre}, tiene un IMC de {imc:0.2f} y su condición es {mensaje}.")



