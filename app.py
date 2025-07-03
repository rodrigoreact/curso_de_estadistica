import streamlit as st

st.set_page_config(page_title="Curso de Estadística", layout="wide")

# Panel lateral (Menú de navegación)
st.sidebar.title("📘 Curso de Estadística")
menu = st.sidebar.radio("Selecciona una sección", [
    "Portada",
    "Gráficos de variables",
    "Estadística descriptiva",
    "Probabilidades",
    "Inferencia"
])

# Contenido central
if menu == "Portada":
    st.title("Bienvenido al Curso de Estadística")
    st.write("""
        Este curso está diseñado para visualizar conceptos clave de estadística utilizando Python y Streamlit.
        Selecciona una sección del menú para comenzar.
    """)

elif menu == "Gráficos de variables":
    # Ejecuta el contenido de otro archivo
    exec(open("graficos_de_variables.py").read())

elif menu == "Estadística descriptiva":
    exec(open("estadistica_descriptiva.py").read())

elif menu == "Probabilidades":
    exec(open("probabilidades.py").read())

elif menu == "Inferencia":
    exec(open("inferencia_estadistica.py").read())
