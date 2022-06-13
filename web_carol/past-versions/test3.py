import streamlit as st
from streamlit_option_menu import option_menu



def my_widget(key):
    st.write("# Bienvenid@ a Carol 👋")

    st.markdown(
        """
       ### Desde ahora, comprar tus medicamentos será más fácil y rápido.

       ### Cómo querés cargar tu receta?
        """
        )
    return st.button("Empezá por acá " + key)

if st.button(' 💻 Cargá tu receta desde tu dispositivo'):
        cargar_foto()
# This works in the main area
clicked = my_widget("first")

# And within an expander
my_expander = st.expander("Expand", expanded=True)
with my_expander:
    clicked = my_widget("second")

# AND in st.sidebar!
with st.sidebar:
    clicked = my_widget("third")
