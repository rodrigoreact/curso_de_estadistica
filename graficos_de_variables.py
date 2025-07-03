import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Configuración inicial
    st.set_page_config(page_title="Estadística con Python", layout="centered")

    st.title("📊 Curso de Estadística con Python")
    st.header("Identificación de Gráficos y Tipos de Variables")

    st.write("""
    A continuación verás distintos gráficos generados con Python y deberás:
    - Identificar el **tipo de variable** que representan.
    - Identificar **qué medida de tendencia central es más adecuada** para cada caso.
    """)

    # Preguntas y correctas
    questions = [
        {
            "title": "Gráfico 1: Gráfico de Barras",
            "desc": "Número de estudiantes por carrera.",
            "options_var": ["Cualitativa nominal", "Cualitativa ordinal", "Cuantitativa discreta", "Cuantitativa continua"],
            "correct_var": "Cualitativa nominal",
            "options_central": ["Media", "Mediana", "Moda"],
            "correct_central": "Moda"
        },
        {
            "title": "Gráfico 2: Histograma",
            "desc": "Distribución de edades de estudiantes.",
            "options_var": ["Cualitativa nominal", "Cualitativa ordinal", "Cuantitativa discreta", "Cuantitativa continua"],
            "correct_var": "Cuantitativa continua",
            "options_central": ["Media", "Mediana", "Moda"],
            "correct_central": "Mediana"
        },
        {
            "title": "Gráfico 3: Boxplot",
            "desc": "Tiempo de resolución de exámenes en minutos.",
            "options_var": ["Cualitativa nominal", "Cualitativa ordinal", "Cuantitativa discreta", "Cuantitativa continua"],
            "correct_var": "Cuantitativa continua",
            "options_central": ["Media", "Mediana", "Moda"],
            "correct_central": "Mediana"
        }
    ]

    # Función para resetear respuestas
    def reset_answers():
        for idx in range(len(questions)):
            st.session_state[f"var_{idx}"] = ""
            st.session_state[f"central_{idx}"] = ""

    if st.button("🧹 Borrar respuestas"):
        reset_answers()

    score = 0
    total_questions = len(questions) * 2  # 2 preguntas por gráfico

    for idx, q in enumerate(questions):
        st.subheader(q["title"])
        st.write(q["desc"])

        # Generación de gráficos
        fig, ax = plt.subplots()
        if idx == 0:
            carreras = ['Ing.', 'Medicina', 'Derecho', 'Arte']
            cantidad = [30, 25, 15, 20]
            ax.bar(carreras, cantidad, color='skyblue')
            ax.set_ylabel("Cantidad de estudiantes")
        elif idx == 1:
            edades = np.random.normal(22, 3, 100)
            ax.hist(edades, bins=10, color='lightgreen', edgecolor='black')
            ax.set_xlabel("Edad")
            ax.set_ylabel("Frecuencia")
        elif idx == 2:
            tiempos = np.random.normal(60, 10, 100)
            ax.boxplot(tiempos, vert=False)
            ax.set_xlabel("Minutos")

        st.pyplot(fig)

        # Selectbox para tipo de variable con opción vacía inicial
        selected_var = st.selectbox(
            f"¿Qué tipo de variable representa este gráfico?",
            options=[""] + q["options_var"],
            key=f"var_{idx}"
        )

        if selected_var == "":
            st.warning("⚠️ Por favor, selecciona un tipo de variable para continuar.")
        else:
            if selected_var == q["correct_var"]:
                st.success("✅ Correcto en tipo de variable")
                score += 1
            else:
                st.error(f"❌ Incorrecto. Respuesta correcta: {q['correct_var']}")

        # Selectbox para medida de tendencia con opción vacía inicial
        selected_central = st.selectbox(
            f"¿Qué medida de tendencia central es más adecuada aquí?",
            options=[""] + q["options_central"],
            key=f"central_{idx}"
        )

        if selected_central == "":
            st.warning("⚠️ Por favor, selecciona una medida de tendencia central para continuar.")
        else:
            if selected_central == q["correct_central"]:
                st.success("✅ Correcto en tendencia central")
                score += 1
            else:
                st.error(f"❌ Incorrecto. Respuesta correcta: {q['correct_central']}")

    st.markdown("---")

    percentage = (score / total_questions) * 100
    grade = 1 + (score / total_questions) * 6
    grade = min(7, grade)
    grade = round(grade, 1)

    st.subheader("📈 Resultados")
    st.write(f"✅ Respuestas correctas: **{score} de {total_questions}**")
    st.write(f"📊 Porcentaje de acierto: **{percentage:.1f}%**")
    st.write(f"🎓 Nota estimada: **{grade} (escala 1-7)**")

    if percentage == 100:
        st.balloons()
