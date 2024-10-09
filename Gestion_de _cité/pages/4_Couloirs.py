import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import calendar
from datetime import datetime, timedelta
st.markdown("""
    <style>
    .stButton button {background-color: green;
        color: white;
        padding-top: 10px;
        padding-bottom:10px;
    }
    </style>
    """, unsafe_allow_html=True)



def get_last_weekend_dates(start_year, start_month, end_year, end_month):
    current_year = start_year
    current_month = start_month
    last_weekends = []

    while (current_year < end_year) or (current_year == end_year and current_month <= end_month):
        # Dernier jour du mois
        last_day = calendar.monthrange(current_year, current_month)[1]
        last_date = datetime(current_year, current_month, last_day)

        # Trouver le dernier samedi et dimanche
        last_saturday = last_date - timedelta(days=(last_date.weekday() + 2) % 7)
        last_sunday = last_saturday + timedelta(days=1)

        last_weekends.append((last_saturday, last_sunday))

        # Passer au mois suivant
        if current_month == 12:
            current_month = 1
            current_year += 1
        else:
            current_month += 1

    return last_weekends

# Utilisation de la fonction
start_year, start_month = 2024, 10
end_year, end_month = 2025, 7
weekends = get_last_weekend_dates(start_year, start_month, end_year, end_month)

dernier_weekend=[ ]

for saturday, sunday in weekends:
        dernier_weekend.append(f"Samedi: {saturday.strftime('%Y-%m-%d')}, Dimanche: {sunday.strftime('%Y-%m-%d')}")

#precision_netoyage=st.selectbox("Voulez vous consulter le programme de netoyage des toilettes ou des blocs",["toilettes", "blocs"])



        # Utiliser une variable d'état pour suivre l'affichage
if 'show_weekends' not in st.session_state:
            st.session_state.show_weekends = False

        # Définir le texte du bouton en fonction de l'état
button_text = 'Afficher les week-ends de nettoyage' if not st.session_state.show_weekends else 'Masquer les week-ends de nettoyage'

        # Afficher le bouton et gérer l'état
if st.button(button_text):
        st.session_state.show_weekends = not st.session_state.show_weekends

        #Afficher ou masquer les week-ends en fonction de l'état
if st.session_state.show_weekends:
            st.write("Les week-ends de nettoyage de la cité entre le mois d'Octobre 2024 et Juillet 2025 sont :")
            st.write(pd.DataFrame(dernier_weekend, columns=["Weekend      "]))
        #if bloc=="Bloc A":

taille=len(dernier_weekend) 
Equipe1_jour=[]
Equipe2_jour=[]
for i in range(1, taille):
            if i %2==0:
                Equipe1_jour.append(dernier_weekend[i])
            else:
                Equipe2_jour.append(dernier_weekend[i])
st.title("***Programme de Nétoyage des équipes***")
if st.button("Programme de Nétoyage des équipes 1 des deux blocs"):
            st.write(" Les weekend de Nétoyage des Equipes 1 des deux blocs sont:")
            st.write(pd.DataFrame(Equipe1_jour, columns=["Weekend       "]))
if st.button("Programme de Nétoyage des équipe 2 des deux blocs"):
            st.write(" Les weekend de Ne2oyage des Equipe 2 des deux blocs sont:")
            st.write(pd.DataFrame(Equipe2_jour, columns=["Weekend         "]))


choix_weekend=st.selectbox("Choisissez un weekend de netoyage et voir les membres chargés du nétoyage",dernier_weekend) 
if choix_weekend in Equipe1_jour:
            st.write("Les équipes de netoyage pour " +" "+ "le" + " " + choix_weekend + " sont les équipes 1 des deux blocs ")
            EquipeA=["SOME Pascal", "TIAO ELiasse", "DAH Fongnemen"," Bonkoungou Emmanuel"]
            EquipeB=["BAMOGO Karim","OUOBA Abel", "KABORE Azaria"]
            st.write(" L'équipe 1 du bloc A est constituée de : ")
            st.write(pd.DataFrame(EquipeA,columns=["Nom et prenom            "]))
            st.write(" L'équipe 1 du bloc B est constituée de : ")
            st.write(pd.DataFrame(EquipeB,columns=["Nom et prenom              "]))
else:
            st.write("Les équipes de netoyage pour " +" "+ "le" + " " + choix_weekend + " sont les équipes 2 des deux blocs ")
            EquipeA=["KONE Ayouba","NIKIEMA David", "SOME Renaud", "BANHORO Donald"]
            EquipeB=["SEBEGO Stephane","NITIEMA Joris"]
            st.write(" L'équipe 2 du bloc A est constituée de : ")
            st.write(pd.DataFrame(EquipeA, columns=["Nom et prenom            "]))
            st.write(" L'équipe 2 du bloc B est constituée de : ")
            st.write(pd.DataFrame(EquipeB,columns=["Nom et prenom             "]))


#" Revenir à la page d'Accueil"
if st.button("Page d'Accueil"): 
    st.switch_page("Page_d'Accueil.py")


if st.button("A PROPOS DE NOUS"):
    st.switch_page("pages/5_Contact.py")