# Ideas para el reto:

1. 5. Corrección de Ángulo de Descenso según Razón Vertical
💡 Descripción:

Se calcula si la razón de descenso es apropiada según distancia y altitud.

Se pide:

Altitud actual

Altitud del destino

Distancia hasta destino

Se calcula el ángulo de descenso y se evalúa si es seguro (entre 3° y 6°).

Si no, pide ajustar altitud.



2. Cálculo de Consumo de Combustible en Etapas de Vuelo

✅ Aprobada según el enunciado.

💡 Descripción:

El avión realiza 10 tramos de vuelo.

En cada tramo, el usuario ingresa el tipo de vuelo:

Subida = 80 L

Crucero = 50 L

Descenso = 30 L

Se usa un bucle para pedir los datos.

Se acumula el consumo total.

Si en algún tramo no hay suficiente combustible, se muestra un mensaje.



3. Ajuste de Altitud para Mantener Margen Seguro
💡 Descripción:

Se fija una altitud deseada (ej. 10,000 ft).

En cada paso, el usuario introduce la altitud actual medida (simulando altímetro).

El programa evalúa si está dentro del margen permitido (ej. ±300 ft).

Si no, recomienda subir o bajar.

El proceso se repite hasta que el avión mantenga estabilidad durante 3 ciclos seguidos.
