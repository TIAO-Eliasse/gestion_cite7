import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import calendar
from datetime import datetime, timedelta
st.title("Programmme de paiment de facture et de netoyage de la cité")

st.markdown("""
    <style>
    .stButton button {background-color: green;
        color: white;
        padding-top: 10px;
        padding-bottom:10px;
    }
    </style>
    """, unsafe_allow_html=True)




#precision_netoyage=st.selectbox("Voulez vous consulter le programme de netoyage des toilettes ou des blocs",["toilettes", "blocs"])
if st.button("* Consultez le Programme de netoyage des couloirs entre le mois d'Octobre 2024 et Juillet 2025* "):
    st.switch_page("pages/4_Couloirs.py")

       
        
if st.button("Consultez le Programme Netoyage des toillettes"):
    st.switch_page("pages/3_Toillettes.py")


if st.button("Consultez le Programme de paiement des factures"):
    st.switch_page("pages/1_Facture.py")

#" Revenir à la page d'Accueil"
if st.button("Page d'Accueil"): 
    st.switch_page("Page_d'Accueil.py")

#if st.button("A PROPOS DE NOUS"):
    #st.switch_page("pages/5_Contact.py")

    



