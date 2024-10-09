import streamlit as st
st.title("A PROPOS DE NOUS")
st.subheader("auteur: TIAO ELIASSE")
st.write("eamil:eliassetiao@gmail.com")

st.markdown("""
    <style>
    .stButton button {background-color: green;
        color: white;
        padding-top: 5px;
        padding-bottom:5px;
    }
    </style>
    """, unsafe_allow_html=True)


#" Revenir à la page d'Accueil"
if st.button("Page d'Accueil"): 
    st.switch_page("Page_d'Accueil.py")

if st.button('Quitter l\'application'):
    st.stop()