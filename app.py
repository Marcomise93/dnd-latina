
import streamlit as st
import random

# Messaggio di benvenuto
st.title("Benvenuto a Dungeons & Dragons Latina!")

# Scelta del dado
st.subheader("Scegli il tipo di dado")
dice_type = st.selectbox("Tipo di dado", [4, 6, 8, 10, 12, 20])

# Numero di dadi da tirare
num_dice = st.number_input("Quanti dadi vuoi tirare?", min_value=1, value=1, step=1)

# Bottone per lanciare i dadi
if st.button("Lancia i dadi"):
    results = [random.randint(1, dice_type) for _ in range(num_dice)]
    total = sum(results)
    st.write(f"Risultati dei dadi: {results}")
    st.write(f"Totale: {total}")
