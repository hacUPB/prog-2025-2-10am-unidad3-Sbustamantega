# Ideas para el reto:

1.  Corrección de Ángulo de Descenso según Razón Vertical
Descripción:

un avion se encuentra en decenso desde una altitud indicada, 
se pide que el pilto ingrese su altitud y la altitud deseada para el descenso
Se calcula si la razón de descenso es apropiada según distancia y altitud.

Se pide:

Altitud actual

Altitud del destino

Distancia hasta destino

Se calcula el ángulo de descenso y se evalúa si es seguro (entre 3° y 6°).

Si no, pide ajustar altitud.



| Variable          | Tipo      | Descripción                                                                |
|-------------------|-----------|----------------------------------------------------------------------------|
| alt_actual        | Entrada   | Altitud actual del avión (ft o m).                                         |
| alt_final         | Entrada   | Altitud deseada o final del descenso (ft o m).                             |
| distancia_destino | Entrada   | Distancia horizontal hasta el destino (NM o km).                           |
| delta_altitud     | Proceso   | Diferencia de altitud                                                      |
| angulo_descenso   | Proceso   | Ángulo calculado del descenso: arctan(delta_altitud / distancia_destino).  |
| rango_inclinacion | Proceso   | Rango permitido de ángulo seguro (3° a 6°).                                |
| es_seguro         | Proceso   | Variable lógica que indica si el ángulo está dentro del rango seguro.      |
| ajuste_altitud    | Salida    | Recomendación de nueva altitud si el ángulo no es seguro.                  |

FUNCION calcular_angulo(razon_descenso, velocidad_horizontal)
    angulo = arctan(razon_descenso / velocidad_horizontal) * (180 / π)
    RETORNAR angulo
FIN FUNCION


INICIO

    repetir = VERDADERO

    MIENTRAS repetir = VERDADERO HACER

        LEER alt_actual
        LEER alt_final
        LEER distancia_destino
        LEER velocidad_horizontal   // GS en nudos o m/s
        LEER razon_descenso         // ft/min

        delta_altitud = alt_actual - alt_final

        // Se calcula el ángulo con la función
        angulo_descenso = calcular_angulo(razon_descenso, velocidad_horizontal)

        IMPRIMIR "Ángulo calculado:", angulo_descenso, "grados"

        SI angulo_descenso >= 3 Y angulo_descenso <= 6 ENTONCES
            IMPRIMIR "El descenso es SEGURO."
            repetir = FALSO
        SINO
            IMPRIMIR "El descenso NO es seguro."
            ajuste_razon = tan(4.5° * π / 180) * velocidad_horizontal
            IMPRIMIR "Razón de descenso recomendada:", ajuste_razon, "ft/min"

            LEER "¿Desea intentar de nuevo con otra razón de descenso? (S/N)" -> opcion
            SI opcion = "N" ENTONCES
                repetir = FALSO
            FIN SI
        FIN SI

    FIN MIENTRAS

FIN

(pedi a la ia que me diera un ejemplo de como podia ser el codigo y ahi pude analizarlo, corregirlo y modificarlo a mi necesidad)


2.  Ajuste de Altitud para Mantener Margen Seguro

Descripción: se fija una altitud para el vuelo, cada 2 minutos se lee la altitud simulando un altimetro, el rango seguro es mas o menos 500 pies de diferencia de la altitud seleccionada,
cuando se pide la altitud, si esta se pasa del rango permitido el codigo enviara un 
mensaje de advertencia de peligro que hay una desviacion en la altitud, y segun la 
desviacion le dira al piloto que suba o baje, seguira pidiendo y repitiendo cada 30
segundos esto hasta que el avion haya estado dentro del rango 8 veces, y manda un mensaje que dice
de vuelta en el nivel crucero, y vuelve a pedir cada 5 minutos



| Variable             | Tipo      | Descripción                                                                 |
|----------------------|-----------|-----------------------------------------------------------------------------|
| altitud_objetivo     | Entrada   | Altitud seleccionada de crucero (ft).                                       |
| altitud_actual       | Entrada   | Altitud leída del altímetro cada intervalo de tiempo.                       |
| rango_seguro         | Proceso   | Margen permitido de ±500 ft respecto a la altitud objetivo.                 |
| desviacion           | Proceso   | Diferencia entre altitud actual y altitud objetivo.                         |
| contador_estabilidad | Proceso   | Número de veces consecutivas que el avión se mantiene dentro del rango.     |
| intervalo_lectura    | Proceso   | Tiempo de espera entre lecturas (30 s o 5 min).                             |
| mensaje              | Salida    | Advertencia o confirmación enviada al piloto.                               |



INICIO

  LEER altitud_objetivo
  rango_seguro =b  500
  contador_estabilidad = 0
  intervalo_lectura = 30 segundos

  MIENTRAS contador_estabilidad < 8 HACER
        ESPERAR intervalo_lectura
        LEER altitud_actual

        desviacion = altitud_actual - altitud_objetivo

        SI |desviacion| <= rango_seguro ENTONCES
              contador_estabilidad = contador_estabilidad + 1
              IMPRIMIR "Dentro del rango seguro. Contador:", contador_estabilidad
        SINO
              contador_estabilidad ← 0
              SI desviacion > 0 ENTONCES
                   mensaje = "Advertencia: Altitud alta. Descienda."
              SINO
                   mensaje = "Advertencia: Altitud baja. Ascienda."
              FIN SI
              IMPRIMIR mensaje
        FIN SI
  FIN MIENTRAS

  IMPRIMIR "De vuelta en el nivel de crucero."
  intervalo_lectura = 5 minutos

  MIENTRAS VERDADERO HACER
        ESPERAR intervalo_lectura
        LEER altitud_actual
        desviacion = altitud_actual - altitud_objetivo

        SI |desviacion| > rango_seguro ENTONCES
              contador_estabilidad = 0
              intervalo_lectura = 30 segundos
              IMPRIMIR "Se detectó desviación. Retomando monitoreo cada 30 segundos."
              (Volver al primer bucle de control)
        FIN SI
  FIN MIENTRAS

FIN







3. un a320 se encuentra en un patron de espera ya que hay una emergencia en el aeropuerto, esta realizando patrones de espera
y necesita saber cuanto tiempo queda restante de espera antes de tener que ir al aeropuerto alternativo

el codigo pide al piloto primero la distancia con su aeropuero alternativo, luego le pide el combustible actual, el sistema
calcula cuanto combustible gasta en ir a ese aeropuerto dejando la reserva de combustible obligatoria, luego calcula cuanto tiempo
se puede hacer el patron de espera antes de que el piloto tenga que ir a su alternativo.

|variables|tipo|descripcion|
|---------|----|-----------|
|aerop_alt|entrada|la distancia con el aeropuerto alternativo
|combustible|entrada|el combustible restante en el tanque|
|




| Variable                  | Tipo      | Descripción                                                                 |
|---------------------------|-----------|-----------------------------------------------------------------------------|
| aerop_alt                 | Entrada   | Distancia con el aeropuerto alternativo (NM o km).                          |
| combustible               | Entrada   | Combustible restante en el tanque (kg o L).                                |
| consumo_vuelo_alt         | Proceso   | Combustible necesario para llegar al alternativo.                           |
| reserva_combustible       | Proceso   | Combustible obligatorio de reserva (ej. 30 min).                           |
| combustible_disponible_espera | Proceso | Combustible que se puede usar solo en espera.                               |
| consumo_por_minuto        | Proceso   | Consumo estimado por minuto durante espera.                                |
| tiempo_espera             | Proceso   | Tiempo máximo que se puede permanecer en espera.                           |
| decision                  | Salida    | Indicación de si se puede seguir esperando o debe ir al alternativo ya.    |


```
INICIO

  LEER aerop_alt
  LEER combustible

  reserva_combustible = valor_estándar (ej. 2000 kg)
  consumo_por_minuto = valor_estándar (ej. 80 kg/min)

  consumo_vuelo_alt = aerop_alt * consumo_promedio_por_nm

  combustible_disponible_espera = combustible - (consumo_vuelo_alt + reserva_combustible)

  SI combustible_disponible_espera <= 0 ENTONCES
        decision = "Ir inmediatamente al aeropuerto alternativo"
        IMPRIMIR decision
  SINO
        tiempo_espera = combustible_disponible_espera / consumo_por_minuto
        decision = "Tiempo máximo de espera: " + tiempo_espera + " minutos"
        IMPRIMIR decision
  FIN SI

FIN
```










## Extra. Cálculo de Consumo de Combustible en Etapas de Vuelo
Descripción:

El avión realiza 10 tramos de vuelo uno cada 10 minutos.

En cada tramo, el usuario ingresa el tipo de vuelo:

Subida = 80 L

Crucero = 50 L

Descenso = 30 L

Se usa un bucle para pedir los datos.

Se acumula el consumo total.

Si en algún tramo no hay suficiente combustible, se muestra un mensaje de que hay combustible bajo.





## uso de IA
-para inspiración y crear los problemas