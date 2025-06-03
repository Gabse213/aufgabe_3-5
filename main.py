import streamlit as st
import read_data # Ergänzen Ihr eigenes Modul
from PIL import Image
from read_pandas import read_my_csv, erstelle_hr_zonen_plot, berechne_durchschnittswerte

# Eine Überschrift der ersten Ebene
st.write("# EKG-App")


# Eine Überschrift der zweiten Ebene
st.write("## Versuchsperson auswählen")

# Legen Sie eine neue Liste mit den Personennamen an indem Sie ihre 
# Funktionen aufrufen
person_dict = read_data.load_person_data()
person_names = read_data.get_person_list(person_dict)
# bzw: wenn Sie nicht zwei separate Funktionen haben
# person_names = read_data.get_person_list()

# Nutzen Sie ihre neue Liste anstelle der hard-gecodeten Lösung
st.session_state.current_user = st.selectbox(
    'Versuchsperson',
    options = person_names, key="sbVersuchsperson")


# Anlegen des Session State. Bild, wenn es kein Bild gibt
if 'picture_path' not in st.session_state:
    st.session_state.picture_path = 'data/pictures/none.jpg'

# ...

# Suche den Pfad zum Bild, aber nur wenn der Name bekannt ist
if st.session_state.current_user in person_names:
    st.session_state.picture_path = read_data.find_person_data_by_name(st.session_state.current_user)["picture_path"]

# ...

# Öffne das Bild und Zeige es an
image = Image.open(st.session_state.picture_path)
st.image(image, caption=st.session_state.current_user)

# Eine Überschrift der zweiten Ebene
st.write("## Herzfrequenz-/Leistungsdiagramm")
#Maximale Herzfrequenz eingeben
max_hr = st.number_input("Gib deine maximale Herzfrequenz (Max HR) ein:",
                        min_value=100, max_value=225, value=190)

# Aktivitätsdaten laden
try:
    df = read_my_csv()
    st.success("Daten erfolgreich geladen!")
    
    # Plot erzeugen
    erstelle_hr_zonen_plot(df, max_hr)

        # Durchschnittswerte berechnen und anzeigen
    durchschnitt_hf, durchschnitt_leistung = berechne_durchschnittswerte(df)

    st.subheader("📊 Durchschnittswerte")
    col1, col2 = st.columns(2)
    col1.metric("Ø Herzfrequenz (bpm)", f"{durchschnitt_hf:.1f}")
    col2.metric("Ø Leistung (W)", f"{durchschnitt_leistung:.1f}")


except FileNotFoundError:
    st.error("Die Aktivitätsdatei konnte nicht gefunden werden.")
except Exception as e:
    st.error(f"Fehler beim Einlesen oder Plotten: {e}")
