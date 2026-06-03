# Análisis de Ventas de una Pequeña Empresa

Trabajo Práctico N°01 – Organización Empresarial  
Tecnicatura Universitaria en Programación – Universidad Tecnológica Nacional  
Año Lectivo: 2026

---

## Integrante

| Nombre | Rol |
|--------|-----|
| Gonzalo Agustin Erizaga Boggia | P1 – Líder / P2 – Desarrollador / P3 – Revisor |

---

## Escenario elegido

**Escenario B – Análisis de Ventas de una Pequeña Empresa**

Se trabaja con un dataset simulado de ventas comerciales para generar indicadores básicos que permitan interpretar el desempeño de la empresa a lo largo del tiempo.

---

## Dataset utilizado

Archivo: `datos/ventas.csv`

Dataset de elaboración propia con registros de ventas de productos tecnológicos durante el período enero–agosto 2024.

| Columna | Descripción |
|---------|-------------|
| `id` | Identificador único de la transacción |
| `producto` | Nombre del producto vendido |
| `cantidad` | Unidades vendidas |
| `precio` | Precio unitario en pesos |
| `fecha_venta` | Fecha de la transacción (YYYY-MM-DD) |

---

## Indicadores calculados

- **Ventas totales**: suma del ingreso de todas las transacciones (cantidad × precio)
- **Producto más vendido**: producto con mayor cantidad acumulada de unidades vendidas
- **Ventas por mes**: ingreso total agrupado por mes para analizar la evolución temporal

---

## Estructura del repositorio

```
repo-proyecto/
│
├── datos/
│   └── ventas.csv
│
├── scripts/
│   └── analisis_ventas.py
│
├── resultados/
│   ├── resumen_ventas.csv
│   └── grafico_ventas.png
│
├── README.md
│
└── .gitignore
```

---

## Instrucciones para ejecutar el script en Google Colab

1. Clonar el repositorio dentro de Colab:
```bash
!git clone https://github.com/{TU_USUARIO}/{TU_REPO}.git
%cd {TU_REPO}
```

2. Ir a la carpeta de scripts:
```bash
%cd scripts
```

3. Ejecutar el script:
```bash
!python analisis_ventas.py
```

4. Los resultados se guardan automáticamente en la carpeta `/resultados`.

---

## Trazabilidad con Jira

| Issue | Descripción |
|-------|-------------|
| PROY-1 | Inicialización del repositorio y estructura de carpetas |
| PROY-2 | Desarrollo del script de análisis de ventas |
| PROY-3 | Revisión, documentación y merge final |

---

## Tecnologías utilizadas

- Python 3 (pandas, matplotlib)
- Git / GitHub
- Google Colab
- Jira (gestión de tareas)
