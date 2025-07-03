import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def main():
    st.header("📐 Inferencia Estadística")

    st.markdown("""
    En esta sección podrás calcular intervalos de confianza y realizar pruebas de hipótesis para una muestra.
    """)

    # Subida de archivo
    archivo = st.file_uploader("📂 Sube un archivo CSV", type=["csv"])

    if archivo is not None:
        df = pd.read_csv(archivo)
        columnas_numericas = df.select_dtypes(include=np.number).columns.tolist()

        if columnas_numericas:
            columna = st.selectbox("Selecciona una variable numérica", columnas_numericas)
            data = df[columna].dropna()

            st.subheader("📊 Resumen")
            st.write(f"**Media muestral:** {data.mean():.2f}")
            st.write(f"**Tamaño de muestra:** {len(data)}")
            st.write(f"**Desviación estándar:** {data.std():.2f}")

            st.markdown("---")

            st.subheader("📏 Intervalo de confianza para la media")

            nivel_confianza = st.slider("Nivel de confianza", 80, 99, 95)
            alfa = 1 - (nivel_confianza / 100)
            n = len(data)
            media = np.mean(data)
            desv = np.std(data, ddof=1)
            error = stats.t.ppf(1 - alfa / 2, df=n - 1) * (desv / np.sqrt(n))
            li = media - error
            ls = media + error

            st.write(f"**Intervalo de confianza del {nivel_confianza}%:** [{li:.2f}, {ls:.2f}]")

            st.markdown("---")

            st.subheader("📉 Prueba de hipótesis para la media")

            mu_hipotesis = st.number_input("Valor hipotético de la media (H₀)", value=0.0)
            tipo_prueba = st.radio("Tipo de prueba", ["Bilateral", "Unilateral izquierda", "Unilateral derecha"])

            t_stat = (media - mu_hipotesis) / (desv / np.sqrt(n))
            p_value = {
                "Bilateral": 2 * (1 - stats.t.cdf(abs(t_stat), df=n - 1)),
                "Unilateral izquierda": stats.t.cdf(t_stat, df=n - 1),
                "Unilateral derecha": 1 - stats.t.cdf(t_stat, df=n - 1)
            }[tipo_prueba]

            st.write(f"**Estadístico t:** {t_stat:.3f}")
            st.write(f"**Valor p:** {p_value:.4f}")

            if p_value < alfa:
                st.success("🚨 Se rechaza H₀.")
            else:
                st.info("✅ No se rechaza H₀.")

        else:
            st.warning("⚠️ El archivo no contiene columnas numéricas.")
    else:
        st.info("📥 Sube un archivo CSV para comenzar.")
