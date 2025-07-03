import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def main():
    st.header("🎲 Probabilidades")

    st.markdown("""
    En esta sección exploraremos conceptos básicos de probabilidad a través de visualizaciones y simulaciones.
    
    A continuación puedes elegir una distribución y ver su comportamiento.
    """)

    distribucion = st.selectbox("Selecciona una distribución", ["Binomial", "Normal", "Poisson"])

    if distribucion == "Binomial":
        n = st.slider("Número de ensayos (n)", 1, 100, 10)
        p = st.slider("Probabilidad de éxito (p)", 0.0, 1.0, 0.5)
        x = np.arange(0, n+1)
        y = stats.binom.pmf(x, n, p)
        st.bar_chart(y)

    elif distribucion == "Normal":
        mu = st.slider("Media (μ)", -10.0, 10.0, 0.0)
        sigma = st.slider("Desviación estándar (σ)", 0.1, 10.0, 1.0)
        x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
        y = stats.norm.pdf(x, mu, sigma)
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title("Distribución Normal")
        st.pyplot(fig)

    elif distribucion == "Poisson":
        lam = st.slider("Lambda (λ)", 1, 20, 5)
        x = np.arange(0, 30)
        y = stats.poisson.pmf(x, lam)
        st.bar_chart(y)
