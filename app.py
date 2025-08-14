import streamlit as st
import joblib
import numpy as np

# Cargar modelo
modelo = joblib.load('primermillon.joblib')

# Título
st.title("🎓 Predictor de Éxito Académico")

# Autor
st.markdown("**Autor: Juan Palencia**")

# Imagen
st.image("https://buscacarrera.com.co/contenido/consejo/la-clave-del-exito-academico-como-crear-un-plan-de-estudio-efectivo.jpg", use_column_width=True)

# Introducción
st.markdown("""
Bienvenido a la aplicación de predicción de éxito académico.  
Aquí podrás estimar si un estudiante logrará graduarse con éxito basándose en dos factores clave:

- **Nota IA**: desempeño en Inteligencia Artificial
- **GPA**: promedio general acumulado

Usa los deslizadores para ingresar los valores. Los valores deben estar entre 0.0 y 1.0 con precisión decimal.
""")

# Entradas del usuario
nota_ia = st.slider("Nota IA", 0.0, 1.0, 0.5, step=0.1)
gpa = st.slider("GPA", 0.0, 1.0, 0.5, step=0.1)

# Botón de predicción
if st.button("📊 Predecir éxito académico"):
    entrada = np.array([[nota_ia, gpa]])
    prediccion = modelo.predict(entrada)[0]

    if prediccion == 1:
        st.success("🎉 ¡Felicitaciones! Te vas a graduar con honores.")
    else:
        st.error("😞 No se graduará.")

# Pie de página
st.markdown("---")
st.markdown("© 2025 UNAB")
