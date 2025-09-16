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



|# Tabla de Variables del Algoritmo de Ascenso/Descenso

| Variable           | Tipo       | Descripción                                                                 |
|--------------------|------------|-----------------------------------------------------------------------------|
| alt_actual         | Entrada    | Altitud actual del avión (ft).                                              |
| alt_final          | Entrada    | Altitud deseada o final (ft).                                               |
| distancia_destino  | Entrada    | Distancia horizontal hasta el destino (NM, convertida a ft en el cálculo).  |
| velocidad_aeronave | Entrada    | Velocidad horizontal de la aeronave (kt).                                   |
| etapa_vuelo        | Entrada    | Etapa del vuelo: `"A"` = Ascenso, `"D"` = Descenso.                         |
| delta_altitud      | Proceso    | Diferencia de altitud: `alt_final - alt_actual`.                            |
| angulo             | Proceso    | Ángulo calculado: `arctan(|delta_altitud| / distancia_destino)`.            |
| ajuste_razon       | Proceso    | Razón vertical correspondiente al ángulo: `tan(angulo) * velocidad * 101    |
| es_seguro          | Proceso    | Variable lógica que indica si el ángulo está dentro del rango seguro.       |
| rango_descenso     | Constante  | Rango permitido para descenso: 3° a 6°.                                     |
| rango_ascenso      | Constante  | Rango permitido para ascenso: 10° a 25°.                                    |



```
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
```

(pedi a la ia que me diera un posible metodo para realizar el pseudocodigo y ahi pude analizarlo, corregirlo y modificarlo a necesidad)









2. eficiencia de una aeronave en crucero

Se desea determinar si un Airbus A320 puede volar hasta un destino con el combustible cargado, considerando viento y velocidad de crucero. Para este problema se asume que el consumo en crucero del A320 es constante e igual a 5400 lb/h.


| Variable              | Tipo    | Descripción                                                              |
|-----------------------|---------|--------------------------------------------------------------------------|
| combustible_lb        | Entrada | Combustible cargado en libras (lb).                                      |
| consumo_lb_h          | Entrada | Consumo promedio en libras por hora (lb/h).                              |
| velocidad_kts         | Entrada | Velocidad de crucero en nudos (kt).                                      |
| viento_kts            | Entrada | Velocidad del viento en nudos (positivo a favor, negativo en contra).    |
| distancia_objetivo_nm | Entrada | Distancia al destino en millas náuticas (NM).                            |
| tiempo_horas          | Salida  | Autonomía máxima en horas de vuelo.                                      |
| distancia_max_nm      | Salida  | Distancia máxima que puede recorrer la aeronave en millas náuticas (NM). |
|consumo_lb_h           |Constante| la autonomia del airbus a320 en condiciones estandar                     |




```
INICIO

repetir = "r"

MIENTRAS repetir = "r":
      escribir "Ingrese combustible en lb:"
      leer combustible_lb

      escribir "Ingrese velocidad en kts:"
      leer velocidad_kts

      escribir "Ingrese viento en kts (positivo a favor, negativo en contra):"
      leer viento_kts

      escribir "Ingrese distancia al destino en NM:"
      leer distancia_objetivo_nm

      consumo_lb_h = 5400

      tiempo_horas = combustible_lb / consumo_lb_h
      velocidad_efectiva_kts = velocidad_kts + viento_kts

      SI velocidad_efectiva_kts <= 0 :
            escribir "error, valores no validos"
      SINO
            distancia_max_nm = velocidad_efectiva_kts * tiempo_horas

            escribir "Autonomía en horas:", tiempo_horas
            escribir "Distancia máxima en NM:", distancia_max_nm

            SI distancia_max_nm >= distancia_objetivo_nm :
                  escribir "Vuelo POSIBLE."
            SINO
                  escribir "Vuelo no posible, busque un destino alternativo."
            FIN SI
      FIN SI

      escribir "¿Desea realizar otro calculo? (r):"
      leer repetir

FIN MIENTRAS

FIN
```

(pedi a la ia que me diera un posible metodo para realizar el pseudocodigo y ahi pude analizarlo, corregirlo y modificarlo a necesidad)


3. patron de espera
un a320 se encuentra en un patron de espera ya que hay una emergencia en el aeropuerto, esta realizando patrones de espera
y necesita saber cuanto tiempo queda restante de espera antes de tener que ir al aeropuerto alternativo

el codigo pide al piloto primero la distancia con su aeropuero alternativo, luego le pide el combustible actual, el sistema
calcula cuanto combustible gasta en ir a ese aeropuerto dejando la reserva de combustible obligatoria, luego calcula cuanto tiempo
se puede hacer el patron de espera antes de que el piloto tenga que ir a su alternativo.



| Variable                      | Tipo     | Descripción                                                                 |
|-------------------------------|----------|-----------------------------------------------------------------------------|
| aerop_alt                     | Entrada  | Distancia con el aeropuerto alternativo (NM).                               |
| combustible                   | Entrada  | Combustible restante en el tanque (lb).                                     |
| velocidad_promedio            | Entrada  | Velocidad promedio del A320 en crucero hacia el alternativo (kt).           |
| consumo_por_hora              | Entrada  | Consumo promedio del A320 en crucero (lb/h).                                |
| consumo_por_minuto            | Entrada  | Consumo promedio en patrón de espera (lb/min).                              |
| factor_viento                 | Entrada  | Factor que ajusta consumo según viento (ej. 1.1 si hay viento en contra).   |
| factor_espera                 | Entrada  | Factor que ajusta consumo en patrón de espera (ej. 1.05 por maniobras).     |
| reserva_combustible           | Proceso  | Combustible obligatorio de reserva (ej. 2000 lb).                           |
| tiempo_vuelo_alt              | Proceso  | Tiempo estimado de vuelo al alternativo: `aerop_alt / velocidad_promedio`.  |
| consumo_vuelo_alt             | Proceso  | Combustible necesario para llegar al alternativo con viento.                |
| combustible_disponible_espera | Proceso  | Combustible que se puede usar solo en espera.                               |
| tiempo_espera                 | Proceso  | Tiempo máximo que se puede permanecer en espera.                            |

```
Inicio
repetir = "r"

MIENTRAS repetir = "r"

      LEER aerop_alt
      LEER combustible
      LEER velocidad_promedio
      LEER consumo_por_hora
      LEER consumo_por_minuto
      LEER factor_viento
      LEER factor_espera

      reserva_combustible = 2000

      tiempo_vuelo_alt = aerop_alt / velocidad_promedio
      consumo_vuelo_alt = tiempo_vuelo_alt * consumo_por_hora * factor_viento
      combustible_disponible_espera = combustible - (consumo_vuelo_alt + reserva_combustible)

      SI combustible_disponible_espera <= 0 ENTONCES
            ESCRIBIR = "Ir inmediatamente al aeropuerto alternativo"
      SINO
            tiempo_espera = (combustible_disponible_espera / (consumo_por_minuto * factor_espera))
            ESCRIBIR = "Tiempo máximo de espera: " + tiempo_espera + " minutos"
      FIN SI

      escribir "¿Desea repetir el cálculo? (r)"
      leer repetir

FIN MIENTRAS

FIN
```

(pedi a la ia que me diera un posible metodo para realizar el pseudocodigo y ahi pude analizarlo, corregirlo y modificarlo a necesidad)




































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



2. Ajuste de Altitud para Mantener Margen Seguro   (problema desechado)

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


```
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
```



## uso de IA
-para inspiración y crear los problemas
