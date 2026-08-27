import pandas as pd
datos = {
    'Producto': ['Laptop', 'Mouse', 'Teclado'],
    'Ventas': [1500, 25, 45]
}
df = pd.DataFrame(datos)

print(df.iloc[1,0])