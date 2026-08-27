import pandas as pd
import plotly.graph_objects as go
import openpyxl
from openpyxl.drawing.image import Image

# 1. Leemos los datos consolidados que ya procesamos
archivo_datos = "reporte_impuestos_consolidado.xlsx"
df = pd.read_excel(archivo_datos)

# 2. CREAMOS EL GRÁFICO CON PLOTLY
# Usamos el submódulo graph_objects (go) para construir la figura
fig = go.Figure()

# Añadimos un trazo de barras (go.Bar)
fig.add_trace(go.Bar(
    x=df["Tipo"],
    y=df["Precio_USD"],
    # Aplicamos colores que combinan con nuestro diseño azul corporativo
    marker_color=["#1F497D", "#4F81BD"], 
    name="Precio Promedio"
))

# 3. PERSONALIZAMOS EL DISEÑO (LAYOUT)
# Aquí estructuramos títulos y fuentes para un look sumamente ejecutivo
fig.update_layout(
    title={
        'text': "Precio Promedio de Productos por Tipo",
        'font': {'family': "Arial", 'size': 16, 'color': "#1F497D"},
        'x': 0.5,
        'xanchor': 'center'
    },
    xaxis={
        'title': "Categoría de Producto",
        'title_font': {'family': "Arial", 'size': 12},
        'tickfont': {'family': "Arial", 'size': 10}
    },
    yaxis={
        'title': "Precio Promedio (USD)",
        'title_font': {'family': "Arial", 'size': 12},
        'tickfont': {'family': "Arial", 'size': 10},
        'gridcolor': "#E5E5E5"  # Rejilla sutil gris claro
    },
    template="simple_white",   # Aplicamos un tema limpio de fondo blanco
    width=550,                 # Definimos tamaño controlado para Excel
    height=400,
    margin={'l': 50, 'r': 30, 't': 50, 'b': 50}
)

# 4. GUARDAMOS EL GRÁFICO COMO IMAGEN
# Kaleido trabaja por detrás para exportar el gráfico estático de forma transparente
imagen_salida = "grafico_precios.png"
fig.write_image(imagen_salida)
print("--- ¡Gráfico exportado como imagen con éxito! ---")

# 5. CARGAMOS TU EXCEL ESTILIZADO E INSERTAMOS EL GRÁFICO
archivo_excel = "reporte_impuestos_estilizado.xlsx"
wb = openpyxl.load_workbook(archivo_excel)
ws = wb.active

# Cargamos el archivo de imagen en openpyxl
img_excel = Image(imagen_salida)

# Insertamos la imagen en la celda F2 (al lado de nuestra tablita)
ws.add_image(img_excel, "F2")

# Guardamos el libro final unificado
archivo_reporte_final = "reporte_final_con_grafico.xlsx"
wb.save(archivo_reporte_final)

print(f"¡Espectacular! Reporte final generado en: '{archivo_reporte_final}'")
