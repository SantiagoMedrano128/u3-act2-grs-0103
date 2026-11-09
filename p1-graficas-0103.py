import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Definición de los datos de Cryptos (Nombre, Símbolo, Es_Codigo_Abierto, Año, Precio_USD)
btc = ['Bitcoin', 'BTC', True, 2009, 1000]
eth = ['Ethereum', 'ETH', True, 2015, 800]
sol = ['Solana', 'SOL', True, 2020, 600]
ada = ['Cardano', 'ADA', True, 2017, 250]
xrp = ['Ripple', 'XRP', False, 2012, 400]

# 2. Creamos la lista de listas (conformando la tabla)
listas_cryptos = [btc, eth, sol, ada, xrp]

# 3. Utilizar pandas para organizar la tabla (DataFrame)
# A cada columna le ponemos nombre acorde a la estructura solicitada
df_cryptos = pd.DataFrame(
    listas_cryptos,
    columns=['Nombre', 'Simbolo', 'Es_Codigo_Abierto', 'Año', 'Precio_USD'],
)
print(df_cryptos)

# Guardar en archivo CSV (opcional)
# df_cryptos.to_csv("cryptos.csv", index=False)

# 4. Crear gráfica de líneas (Eje X: Nombre, Eje Y: Precio_USD)
plt.plot(df_cryptos['Nombre'], df_cryptos['Precio_USD'])
plt.title('Gráfica Cryptos 0103 - Precio')
plt.xlabel('Nombre de las Cryptos')
plt.ylabel('Precio (USD)')
plt.show()

# 5. Crear gráfica de puntos (Scatter)
plt.scatter(df_cryptos['Nombre'], df_cryptos['Precio_USD'])
plt.title('Dispersión Cryptos - Precio')
plt.xlabel('Nombre de las Cryptos')
plt.ylabel('Precio (USD)')
plt.show()

# 6. Gráfica de barras simple
plt.bar(df_cryptos['Nombre'], df_cryptos['Precio_USD'])
plt.title('Cryptos 0103')
plt.xlabel('Las Cryptos')
plt.ylabel('Precio (USD)')
plt.show()

# 7. Ordenar la gráfica de barras de manera descendente
df_cryptos_ordenar = df_cryptos.sort_values('Precio_USD', ascending=False)
plt.bar(df_cryptos_ordenar['Nombre'], df_cryptos_ordenar['Precio_USD'])
plt.title('Cryptos Ordenadas (Mayor a Menor Precio)')
plt.xlabel('Las Cryptos')
plt.ylabel('Precio (USD)')
plt.show()

# 8. Coloreando la gráfica de barras ordenada
plt.bar(
    df_cryptos_ordenar['Nombre'],
    df_cryptos_ordenar['Precio_USD'],
    color=['b', 'g', 'c', 'm', 'y'],  # Ajustado a 5 colores por las 5 cryptos
)
plt.title('Cryptos Ordenadas con Color')
plt.xlabel('Las Cryptos')
plt.ylabel('Precio (USD)')
plt.show()

# 9. Gráfica de pastel (Pie chart)
plt.pie(df_cryptos['Precio_USD'], labels=df_cryptos['Nombre'])
plt.title('Distribución de Precios Cryptos')
plt.show()