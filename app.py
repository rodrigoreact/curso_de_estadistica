import streamlit as st
import graficos_de_variables
import estadistica_descriptiva
import probabilidades
import inferencia_estadistica

st.set_page_config(page_title="Curso de Estadística", layout="wide")
st.sidebar.title("📘 Curso de Estadística")

menu = st.sidebar.radio("Selecciona una sección", [
    "Portada",
    "Gráficos de variables",
    "Estadística descriptiva",
    "Probabilidades",
    "Inferencia"
])

if menu == "Portada":
    st.title("Bienvenido al Curso de Estadística")
    st.write("Selecciona una sección del menú para comenzar.")

elif menu == "Gráficos de variables":
    graficos_de_variables.main()

elif menu == "Estadística descriptiva":
    estadistica_descriptiva.main()

elif menu == "Probabilidades":
    probabilidades.main()

elif menu == "Inferencia":
    inferencia_estadistica.main()
