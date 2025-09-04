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


|variables|Tipo|Descripcion|
|---------|----|-----------|
|alt_actual|Entrada|
|alt_final|entrada|
|taza_descenso|proceso |
|rango_inclinacion|proceso| el angulo que el avion puede tener para el descenso










2. Cálculo de Consumo de Combustible en Etapas de Vuelo
Descripción:

El avión realiza 10 tramos de vuelo uno cada 10 minutos.

En cada tramo, el usuario ingresa el tipo de vuelo:

Subida = 80 L

Crucero = 50 L

Descenso = 30 L

Se usa un bucle para pedir los datos.

Se acumula el consumo total.

Si en algún tramo no hay suficiente combustible, se muestra un mensaje de que hay combustible bajo.



3. Ajuste de Altitud para Mantener Margen Seguro
Descripción: se fija una altitud para el vuelo, cada 5 minutos se ingresa la altitud, el rango seguro es mas o menos 500 pies de diferencia de la altitud seleccionada,
cuando se pide la altitud, si esta se pasa del rango permitido el codigo enviara un 
mensaje de advertencia de peligro que hay una desviacion en la altitud, y segun la 
desviacion le dira al piloto que suba o baje, seguira pidiendo y repitiendo cada 30
segundos esto hasta que el avion haya estado dentro del rango 8 veces, y manda un mensaje que dice
de vuelta en el nivel crucero, y vuelve a pedir cada 5 minutos

Se fija una altitud deseada (ej. 10,000 ft).

En cada cierto tiempo, el usuario introduce la altitud actual medida (simulando altímetro).

El programa evalúa si está dentro del margen permitido (ej. ±300 ft).

Si no, recomienda subir o bajar.

El proceso se repite hasta que el avión mantenga estabilidad durante 3 ciclos seguidos.


4. un a320 se encuentra en un patron de espera ya que hay una emergencia en el aeropuerto, esta realizando patrones de espera
y necesita saber cuanto tiempo queda restante de espera antes de tener que ir al aeropuerto alternativo

el codigo pide al piloto primero la distancia con su aeropuero alternativo, luego le pide el combustible actual, el sistema
calcula cuanto combustible gasta en ir a ese aeropuerto dejando la reserva de combustible obligatoria, luego calcula cuanto tiempo
se puede hacer el patron de espera antes de que el piloto tenga que ir a su alternativo.

|variables|tipo|descripcion|
|---------|----|-----------|
|aerop_alt|entrada|la distancia con el aeropuerto alternativo
|combustible|entrada|el combustible restante en el tanque|
|