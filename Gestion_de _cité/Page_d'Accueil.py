
import streamlit as st

# Configurer la mise en page



# Configurer la mise en page et le thème
st.set_page_config(
    page_title="Mon Application Streamlit",
    page_icon=":rocket                           :",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Ajouter du CSS personnalisé
st.markdown("""
    <style>
    .stButton button {background-color: green;
        color: white;
        padding-top: 20px;
        padding-bottom:40px;
    }
    </style>
    """, unsafe_allow_html=True)

# Utiliser la classe CSS dans votre application
st.markdown('<p class="big-font">Bienvenue dans application GESTION DE LA CITE!</p>', unsafe_allow_html=True)
st.write("Cette application donne le programme de Nétoyage de la cité et des paiements de factures ")
if st.button("Consultez le Programme de Nétoyage de la cité"):
    st.switch_page("pages/2_Propreté.py")
if st.button("Consultez le Programme de paiement des factures"):
    st.switch_page("pages/1_Facture.py")

if st.button('Quitter l\'application'):
    st.stop()