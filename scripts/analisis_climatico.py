# =============================================================================
# ANÁLISIS CLIMÁTICO - UTN TUP 2026
# =============================================================================

temperaturas = [22, 24, 19, 30, 28, 26, 21]

# Procesamiento de datos
promedio = sum(temperaturas) / len(temperaturas)
max_temp = max(temperaturas)
min_temp = min(temperaturas)

# Resultados
print("===================================")
print("ANÁLISIS CLIMÁTICO EJECUTADO")
print("===================================")

print("Datos:", temperaturas)
print("Promedio de temperatura:", round(promedio, 2))
print("Temperatura máxima:", max_temp)
print("Temperatura mínima:", min_temp)

# Interpretación simple
if promedio > 25:
    print("Conclusión: Temperatura elevada en el período analizado.")
else:
    print("Conclusión: Temperatura dentro de valores moderados.")
