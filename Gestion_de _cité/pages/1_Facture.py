import streamlit as st
st.title("Programme de paiement des factures")
cite_membre=["SOME PASCAL","KABORE Azaria","NITIEMA Joris","BANHORO Donald", "NIKIEMA David","DAH Fongnemen","BAMOGO Karim",
                 "OUOBA Abel","SEBEGO Stephane","KONE Ajouba","TIAO Eliasse", "BONKOUNGOU Emmanuel","SOME Renaud"]
    # Définir les dates de début et de fin
    
    # Initialiser une liste pour stocker les mois
months= ["Octobre 2024", "Novembre 2024", "Décembre 2024","Janvier 2025","Mars 2025","Avril 2025","Mai 2025",
              "Juin 2025", "Juillet 2025", "Aout 2025", "septembre 2025", "Octobre 2025"]

    # Parcourir chaque mois entre les deux dates
    
Mois_paiement=st.selectbox("Chosisis le mois de paiement de la facture: ",months)
st.write(" les factures du mois de " +Mois_paiement +" seront payées par :"+ cite_membre[months.index(Mois_paiement)])

if st.button("Le Programme de netoyage de la cité"):
    st.switch_page("pages/2_Propreté.py")

st.markdown("""
    <style>
    .stButton button {background-color: green;
        color: white;
        padding-top: 20px;
        padding-bottom:40px;
    }
    </style>
    """, unsafe_allow_html=True)

##""" A PROPOS DE NOUS"
if st.button("A PROPOS DE NOUS"):
    st.switch_page("pages/5_Contact.py")