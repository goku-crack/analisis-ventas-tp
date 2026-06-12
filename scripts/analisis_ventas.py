"""
Script de análisis de ventas.
Calcula: ventas totales, producto más vendido y ventas por mes.
Genera un gráfico de evolución mensual y guarda los resultados
en la carpeta /resultados.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

RUTA_DATOS = "../datos/ventas.csv"
RUTA_RESULTADOS = "../resultados/"

os.makedirs(RUTA_RESULTADOS, exist_ok=True)

df = pd.read_csv(RUTA_DATOS)
df["total_venta"] = df["cantidad"] * df["precio"]

ventas_totales = df["total_venta"].sum()
print(f"Ventas totales: ${ventas_totales:,.2f}")

producto_mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()
cantidad_mas_vendida = df.groupby("producto")["cantidad"].sum().max()
print(f"Producto más vendido: {producto_mas_vendido} ({cantidad_mas_vendida} unidades)")

df["fecha_venta"] = pd.to_datetime(df["fecha_venta"])
df["mes"] = df["fecha_venta"].dt.to_period("M")
ventas_por_mes = df.groupby("mes")["total_venta"].sum()
print("\nVentas por mes:")
print(ventas_por_mes)

resumen = pd.DataFrame({
    "metrica": ["Ventas totales", "Producto más vendido", "Cantidad más vendida"],
    "valor": [ventas_totales, producto_mas_vendido, cantidad_mas_vendida]
})

ventas_por_mes_df = ventas_por_mes.reset_index()
ventas_por_mes_df.columns = ["mes", "total_ventas"]
ventas_por_mes_df["mes"] = ventas_por_mes_df["mes"].astype(str)

with open(os.path.join(RUTA_RESULTADOS, "resumen_ventas.csv"), "w") as f:
    resumen.to_csv(f, index=False)
    f.write("\n")
    ventas_por_mes_df.to_csv(f, index=False)

plt.figure(figsize=(10, 6))
ventas_por_mes_df.plot(x="mes", y="total_ventas", kind="line", marker="o", legend=False, ax=plt.gca())
plt.title("Evolución mensual de ventas")
plt.xlabel("Mes")
plt.ylabel("Total de ventas ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(RUTA_RESULTADOS, "grafico_ventas.png"))
plt.close()

print("\n✔ Análisis finalizado correctamente.")
print(f"Archivos generados en: {RUTA_RESULTADOS}")
