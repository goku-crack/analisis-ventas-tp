# =============================================================================
# PROY-2: Análisis de Ventas de una Pequeña Empresa
# Script: analisis_ventas.py
# Descripción: Procesa un dataset de ventas simuladas y genera indicadores
#              básicos de desempeño comercial junto con un gráfico de evolución.
# Autor: [Tu Nombre]
# Fecha: 2026
# =============================================================================

import pandas as pd
import matplotlib.pyplot as plt
import os

# -----------------------------------------------------------------------------
# 1. CONFIGURACIÓN DE RUTAS
# Usamos rutas relativas para garantizar la reproducibilidad en Google Colab.
# Todos los archivos se organizan según la estructura del repositorio.
# -----------------------------------------------------------------------------
RUTA_DATOS     = "../datos/ventas.csv"
RUTA_RESULTADOS = "../resultados/"

# Crear la carpeta /resultados si no existe (por si se ejecuta por primera vez)
os.makedirs(RUTA_RESULTADOS, exist_ok=True)

# -----------------------------------------------------------------------------
# 2. CARGA DEL DATASET
# Leemos el CSV de ventas. Convertimos la columna de fecha a tipo datetime
# para poder agrupar los datos por mes correctamente.
# -----------------------------------------------------------------------------
df = pd.read_csv(RUTA_DATOS, parse_dates=["fecha_venta"])

print("=== Vista previa del dataset ===")
print(df.head())
print(f"\nRegistros totales: {len(df)}")
print(f"Columnas: {list(df.columns)}")

# -----------------------------------------------------------------------------
# 3. CÁLCULO DE INDICADORES
# Calculamos los indicadores solicitados por la consigna:
#   - Ventas totales (suma de ingresos)
#   - Producto más vendido (por cantidad)
#   - Ventas por mes (para detectar tendencias temporales)
# -----------------------------------------------------------------------------

# 3a. Ventas totales: multiplicamos cantidad por precio para obtener el ingreso
#     de cada transacción, luego sumamos todo.
df["ingreso"] = df["cantidad"] * df["precio"]
ventas_totales = df["ingreso"].sum()

# 3b. Producto más vendido: agrupamos por producto y sumamos cantidades vendidas
ventas_por_producto = df.groupby("producto")["cantidad"].sum().sort_values(ascending=False)
producto_top = ventas_por_producto.index[0]
cantidad_top = ventas_por_producto.iloc[0]

# 3c. Ventas por mes: extraemos el período mes/año y sumamos ingresos
df["mes"] = df["fecha_venta"].dt.to_period("M")
ventas_por_mes = df.groupby("mes")["ingreso"].sum()

# Mostramos los resultados en consola
print("\n=== INDICADORES DE VENTAS ===")
print(f"Ventas totales:        $ {ventas_totales:,.2f}")
print(f"Producto más vendido:  {producto_top} ({cantidad_top} unidades)")
print("\nVentas por mes:")
print(ventas_por_mes.to_string())

# -----------------------------------------------------------------------------
# 4. EXPORTAR TABLA DE RESULTADOS
# Guardamos los indicadores en un CSV dentro de /resultados para
# que queden disponibles como evidencia reproducible del análisis.
# -----------------------------------------------------------------------------
resumen = pd.DataFrame({
    "mes": ventas_por_mes.index.astype(str),
    "ingreso_total": ventas_por_mes.values
})
resumen.to_csv(RUTA_RESULTADOS + "resumen_ventas.csv", index=False)
print("\n✔ Tabla de resultados guardada en /resultados/resumen_ventas.csv")

# -----------------------------------------------------------------------------
# 5. GRÁFICO: EVOLUCIÓN DE VENTAS POR MES
# Generamos un gráfico de línea que muestra la evolución mensual de ingresos.
# Lo guardamos como PNG en /resultados para incluirlo en el informe.
# -----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(
    ventas_por_mes.index.astype(str),
    ventas_por_mes.values,
    marker="o",
    color="#1F5C99",
    linewidth=2,
    markersize=6
)

# Rotamos las etiquetas del eje X para mejorar la legibilidad
ax.set_xticklabels(ventas_por_mes.index.astype(str), rotation=45, ha="right")

ax.set_title("Evolución de Ventas Mensuales", fontsize=14, fontweight="bold")
ax.set_xlabel("Mes", fontsize=11)
ax.set_ylabel("Ingreso Total ($)", fontsize=11)
ax.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig(RUTA_RESULTADOS + "grafico_ventas.png", dpi=150)
plt.show()
print("✔ Gráfico guardado en /resultados/grafico_ventas.png")
