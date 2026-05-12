
import os
import matplotlib.pyplot as plt

# Crear carpeta resultados
os.makedirs("resultados", exist_ok=True)

# Datos climáticos
temperaturas = [22, 24, 19, 30, 28, 26, 21]

# Procesamiento
promedio = sum(temperaturas) / len(temperaturas)
max_temp = max(temperaturas)
min_temp = min(temperaturas)

# Mostrar resultados
print("===================================")
print("ANÁLISIS CLIMÁTICO")
print("===================================")

print("Temperaturas:", temperaturas)
print("Promedio:", round(promedio, 2))
print("Máxima:", max_temp)
print("Mínima:", min_temp)

# Generar gráfico
plt.plot(temperaturas)
plt.title("Temperaturas registradas")
plt.xlabel("Días")
plt.ylabel("Temperatura")

# Guardar gráfico
plt.savefig("resultados/grafico_temperaturas.png")

print("Gráfico generado correctamente")
