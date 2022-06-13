
import streamlit as st
from streamlit_option_menu import option_menu


#1. as sidebar menu
selected=option_menu(
        menu_title="Carol",#required
        options=["Home"," 💻 Cargá tu receta desde tu dispositivo","📸 Sacá una foto de tu receta"],
        icons=["house"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
   )
if selected =="Home":
    st.title(f"{selected}")
    st.write("# Bienvenid@ a Carol 👋")
    st.markdown(
        """
       ### Desde ahora, comprar tus medicamentos será más fácil y rápido.

       ### Cómo querés cargar tu receta?
        """
        )
    st.button(' 💻 Cargá tu receta desde tu dispositivo',)
    st.button(" 📸 Sacá una foto de tu receta")


if selected =="💻 Cargá tu receta desde tu dispositivo":
    st.title(f"{selected}")
    st.markdown(
        """
       ### Cargá tu receta desde tu dispositivo

        """
        )
    image = st.file_uploader("", type=["png", "jpg", "jpeg", "pdf"])

    if image is not None:
        st.image(image, use_column_width=True)
        st.write("<h3 style='text-align: center; color: white;'>Cargaste tu receta!</h3>", unsafe_allow_html=True)
        st.write("<h5 style='text-align: center; color: light green;'>Continuemos👇🏽</h5>", unsafe_allow_html=True)

if selected ==(f"📸 Sacá una foto de tu receta"):
    st.title(f"{selected}")
