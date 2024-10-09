import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import calendar
import datetime
#Définir la forme des bouttons
st.markdown("""
    <style>
    .stButton button {background-color: green;
        color: white;
        padding-top: 10px;
        padding-bottom:10px;
    }
    </style>
    """, unsafe_allow_html=True)

#choix_bloc_Toilettes=st.selectbox("Voir le programme de netoyage des toillettes du bloc: ",["bloc A","bloc B"])
# Initialiser l'état de session

#if 'selected_person' not in st.session_state:
    #st.session_state['selected_person'] = None

# Membres du Bloc A
membres_blocA = ["TIAO Eliasse", "SOME Pascal", "SOME Kpargnin", "Dah", "KONE Ajouba", "David"]

# Définir les dates de début et de fin
start_date = datetime.date(2024, 10, 4)
end_date = datetime.date(2025, 7, 30)

# Initialiser une liste pour stocker les dimanches
sundays = []

# Parcourir chaque jour entre les deux dates
current_date = start_date
while current_date <= end_date:
    if current_date.weekday() == 6:  # 6 correspond à dimanche
        sundays.append(current_date)
    current_date += datetime.timedelta(days=1)

# Assigner les dimanches aux membres
sundays_count = {}
i = 0
for elt in sundays:
    sundays_count[elt] = membres_blocA[i]
    if i < 5:
        i += 1
    else:
        i = 0
if 'show_weekends' not in st.session_state:
            st.session_state.show_weekends = False
def taggle_text():
       st.session_state.show_weekends = not st.session_state.show_weekends 

if st.button("Le Programme de netoyage des toillettes du Bloc A"):
    taggle_text()
if st.session_state.show_weekends:
        
    # Créer un selectbox pour choisir une personne
    Netoyage_personne_specifie = st.selectbox("**Voir le programme de nettoyage des toilettes de :**", membres_blocA)

    #
    # Afficher le programme de nettoyage si une personne est sélectionnée
    
    programme_netoyage = [cle for cle, valeur in sundays_count.items() if valeur == Netoyage_personne_specifie]
    st.write(pd.DataFrame(programme_netoyage, columns=["Programme de nettoyage de " + Netoyage_personne_specifie]))

#""""""""""""PROGRAMME DE NETOYAGE DU BLOC B"""""""""""



membres_blocA=["TIAO Eliasse","SOME Pascal","SOME Kpargnin","Dah","KONE Ajouba","David"]
import datetime

            # Définir les dates de début et de fin
start_date = datetime.date(2024, 10, 4)
end_date = datetime.date(2025, 7, 30)

            # Initialiser une liste pour stocker les dimanches
sundays = []

            # Parcourir chaque jour entre les deux dates
current_date = start_date
while current_date <= end_date:
                if current_date.weekday() == 6:  # 6 correspond à dimanche
                    sundays.append(current_date)
                current_date += datetime.timedelta(days=1)
sundays_count={}
i=0
for elt in sundays:
                sundays_count[elt]=membres_blocA[i]
                if i<5:
                    i=i+1
                else:
                    i=0
if 'show_weekends2' not in st.session_state:
           st.session_state.show_weekends2 = False
def taggle_text2():
       st.session_state.show_weekends2 = not st.session_state.show_weekends2

if st.button("Le Programme de netoyage des toillettes du Bloc B"):
    taggle_text2()
if st.session_state.show_weekends2:
    #st.session_state['show_selectbox'] = True
    Netoyage_personne_specifie=st.selectbox("**Voir le programme de netoyage des toilletes de :**", membres_blocA)
    #if Netoyage_personne_specifie:
        #st.session_state['selected_person'] = Netoyage_personne_specifie
    #if st.session_state['selected_person']:
                            #st.button("Le Programme de netoyage des toillettes du Bloc B")==True
    programme_netoyage=[cle for cle, valeur in sundays_count.items() if valeur == Netoyage_personne_specifie]
    st.write(pd.DataFrame(programme_netoyage, columns=["Programme de netoyage de "+ Netoyage_personne_specifie]))
    


#" Revenir à la page d'Accueil"
if st.button("Page d'Accueil"): 
    st.switch_page("Page_d'Accueil.py")
#  """ Voir la page A PROPOS DE NOUS"""""

if st.button("A PROPOS DE NOUS"):
    st.switch_page("pages/5_Contact.py")