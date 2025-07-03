import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    st.header("📈 Estadística Descriptiva")

    st.markdown("""
    En esta sección puedes cargar un archivo de datos (CSV) y calcular medidas de tendencia central y dispersión,
    además de visualizar histogramas y diagramas de caja.
    """)

    # Subida de archivo
    archivo = st.file_uploader("📂 Sube un archivo CSV", type=["csv"])

    if archivo is not None:
        df = pd.read_csv(archivo)
        st.subheader("📊 Vista previa de los datos")
        st.write(df.head())

        columnas_numericas = df.select_dtypes(include=np.number).columns.tolist()

        if columnas_numericas:
            columna = st.selectbox("Selecciona una variable numérica", columnas_numericas)

            st.subheader("📌 Medidas estadísticas")
            st.write(f"**Media:** {df[columna].mean():.2f}")
            st.write(f"**Mediana:** {df[columna].median():.2f}")
            st.write(f"**Desviación estándar:** {df[columna].std():.2f}")
            st.write(f"**Mínimo:** {df[columna].min():.2f}")
            st.write(f"**Máximo:** {df[columna].max():.2f}")

            # Histogram
            st.subheader("📉 Histograma")
            fig1, ax1 = plt.subplots()
            ax1.hist(df[columna], bins=20, color="skyblue", edgecolor="black")
            ax1.set_title(f"Histograma de {columna}")
            st.pyplot(fig1)

            # Boxplot
            st.subheader("📦 Diagrama de caja")
            fig2, ax2 = plt.subplots()
            ax2.boxplot(df[columna], vert=False)
            ax2.set_title(f"Boxplot de {columna}")
            st.pyplot(fig2)

        else:
            st.warning("⚠️ El archivo no contiene columnas numéricas.")
    else:
        st.info("📥 Esperando que cargues un archivo CSV.")
