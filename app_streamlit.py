import streamlit as st
import time

st.set_page_config(page_title="Formulaire Étudiant", page_icon="🎓")

st.title("🎓 Formulaire Étudiant")

# Formulaire
with st.form("form_etudiant"):

    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    age = st.number_input("Âge", min_value=15, max_value=100, step=1)

    sexe = st.selectbox(
        "Sexe",
        ["Homme", "Femme", "Autre"]
    )

    filiere = st.selectbox(
        "Filière",
        ["Informatique", "Mathématiques", "Physique", "Économie"]
    )

    niveau = st.radio(
        "Niveau",
        ["Licence", "Master", "Doctorat"]
    )

    email = st.text_input("Email")

    date_inscription = st.date_input("Date d'inscription")

    commentaire = st.text_area("Commentaire")

    submit = st.form_submit_button("Enregistrer")

# Traitement
if submit:

    data = {
        "Nom": nom,
        "Prénom": prenom,
        "Âge": age,
        "Sexe": sexe,
        "Filière": filiere,
        "Niveau": niveau,
        "Email": email,
        "Date d'inscription": date_inscription,
        "Commentaire": commentaire
    }

    st.success("Étudiant enregistré avec succès ✅")

    st.subheader("Informations enregistrées")
    st.write(data)

    # Tableau
    df = pd.DataFrame([data])
    st.dataframe(df)