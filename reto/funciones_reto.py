import math

def calcular_ascenso_descenso(etapa_vuelo, alt_final, alt_actual, velocidad_aeronave, distancia_destino):
    """Calcula el ángulo y la velocidad vertical para ascenso o descenso."""
    
    # Conversiones
    velocidad_aeronave_fps = velocidad_aeronave * (6076 / 60)
    distancia_destino_ft = distancia_destino * 6076
    delta_altitud = alt_final - alt_actual
    
    # Cálculo del ángulo
    if distancia_destino_ft == 0:
        return "Error: la distancia no puede ser cero.", None
        
    angulo = math.atan(abs(delta_altitud) / distancia_destino_ft) * (180 / math.pi)
    
    # Cálculo de la velocidad vertical
    velocidad_vertical = math.tan(math.radians(angulo)) * velocidad_aeronave_fps
    
    if etapa_vuelo == "D":
        velocidad_vertical *= -1
    
    return angulo, velocidad_vertical

def calcular_eficiencia_crucero(combustible_lb, velocidad_kts, altitud_ft, viento_kts, distancia_deseada):
    """Calcula la autonomía y la distancia máxima en crucero."""
    
    consumo_base = 6000
    factor_reduccion = (altitud_ft / 1000) * 0.005
    consumo_ajustado = consumo_base * (1 - factor_reduccion)

    if consumo_ajustado < 1000:
        consumo_ajustado = 1000
    
    tiempo_horas = combustible_lb / consumo_ajustado
    velocidad_ef = velocidad_kts + viento_kts

    distancia_max = 0
    if velocidad_ef > 0:
        distancia_max = velocidad_ef * tiempo_horas
    
    return tiempo_horas, distancia_max, consumo_ajustado, velocidad_ef

def calcular_patron_espera(aerop_alt, combustible, velocidad_prom, altitud_espera):
    """Calcula el tiempo de espera disponible en un patrón de espera."""
    
    reserva_combustible = 15000
    consumo_por_minuto = 55
    consumo_base_por_hora = 6000 
    
    factor_reductor = (altitud_espera / 1000) * 0.005
    consumo_ajustado_h = consumo_base_por_hora * (1 - factor_reductor)
    
    if consumo_ajustado_h < 1000:
        consumo_ajustado_h = 1000
        
    tiempo_vuelo = aerop_alt / velocidad_prom
    consumo_alternativo = tiempo_vuelo * consumo_ajustado_h
    combustible_espera = combustible - (consumo_alternativo + reserva_combustible)
    
    tiempo_espera = 0
    if combustible_espera > 0:
        tiempo_espera = combustible_espera / consumo_por_minuto
    
    return combustible_espera, tiempo_espera
