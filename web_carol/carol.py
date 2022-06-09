import streamlit as st
import pandas as pd
from gcloud import detect_text, predict, get_drugs
import numpy as np

with open("style.css") as f:
     st.markdown(f'<style>(f.read())</style>', unsafe_allow_html=True)

# with open('style.css')as f:
#    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

header=st.container()
dataset=st.container()
features = st.container()
modelTraining=st.container()

a = st.sidebar.radio('Proceso de carga de tus medicamentos:',["Cargar tu receta","Confirmar medicamentos"])

# Bienvenida
'''
# **Bienvenid@ a Carol!**
'''
'''
### Ahora podés comprar tus medicamentos de una manera más fácil, rápida y segura.
'''
st.write("#")
st.write("#")
st.write("#")
st.write("#")

# Cargar receta

'''
## 1️⃣ Cargá tu receta médica acá 👇🏽
'''
drugs = []
image = st.file_uploader("", type=["png", "jpg", "jpeg", "pdf"])
if image is not None:
    st.image(image, use_column_width=True)
    st.write("<h3 style='text-align: center; color: white;'>Cargaste tu receta!</h3>", unsafe_allow_html=True)
    st.write("<h5 style='text-align: center; color: light green;'>Continuemos👇🏽</h5>", unsafe_allow_html=True)

    # Detect text
    word_list = detect_text(image.getvalue())
    print(word_list)

    #
    st.markdown(word_list)
    prediction = predict(word_list)

    print('prediction:', prediction)

    drugs = get_drugs(prediction)
    st.markdown(drugs)

# Botón cámara
'''
### También podés intentar sacando una foto de tu receta 📸
'''

#camera = st.camera_input("")
#if camera is not None:
#   st.image(camera, use_column_width=True)

# Acá abajo, va el resultado de la lectura de la receta, formato texto

#st.markdown('Resultado de la lectura de la receta:')

# COnfirmar medicamentos y cantidad
#st.write("#")
#st.write("#")
#st.write("#")
#st.write("#")
#st.write("#")
#st.write("#")
#st.write("#")

'''
## 2️⃣Confirmá tus medicamentos acá 👇🏽
'''
# options = []
# for drug in drugs:
#     print(drug)
#     options.append(drug['id'] + " " + drug['description'] + " " + drug['publicPrice'])

#st.selectbox('Seleccioná tus medicamentos', drugs['description'])
#drugs.style.hide_index()
st.dataframe(drugs[['description', 'prices']].style.hide_index())

'''
## Este es el precio de tu medicamento
'''
st.write("<h5 style='text-align: center; color: light green;'>🤑🤑Acá va el precio luego del query🤑🤑</h5>", unsafe_allow_html=True)
