# Paket für Bearbeitung von Tabellen
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Paket
## zuvor !pip install plotly
## ggf. auch !pip install nbformat
import plotly.express as px
import plotly.io as pio
pio.renderers.default = "browser"

def read_my_csv():
    # Einlesen eines Dataframes
    ## "\t" steht für das Trennzeichen in der txt-Datei (Tabulator anstelle von Beistrich)
    ## header = None: es gibt keine Überschriften in der txt-Datei
    df = pd.read_csv("data/activities/activity.csv")

    t_end= len(df)
    time = np.arange(0, t_end)
    df ["time"] = time
    return df

def erstelle_hr_zonen_plot(df, max_hr):
    zonen = {
        "Zone 1": (max_hr * 0.50, max_hr * 0.60),
        "Zone 2": (max_hr * 0.60, max_hr * 0.70),
        "Zone 3": (max_hr * 0.70, max_hr * 0.80),
        "Zone 4": (max_hr * 0.80, max_hr * 0.90),
        "Zone 5": (max_hr * 0.90, max_hr * 1.00),
    }

    farben = {
        "Zone 1": "blue",
        "Zone 2": "green",
        "Zone 3": "yellow",
        "Zone 4": "orange",
        "Zone 5": "red",
    }

    plt.figure(figsize=(12, 6))

    zeit = df["time"]
    hf = df["HeartRate"]

    for i in range(len(zeit) - 1):
        wert = hf[i]
        for zone, (low, high) in zonen.items():
            if low <= wert < high:
                plt.plot(zeit[i:i+2], hf[i:i+2], color=farben[zone], linewidth=2)
                break

    for zone, (low, high) in zonen.items():
        plt.axhspan(low, high, color=farben[zone], alpha=0.05, label=zone)

    plt.title("Herzfrequenzverlauf mit Trainingszonen")
    plt.xlabel("Zeit (Index)")
    plt.ylabel("Herzfrequenz (bpm)")
    plt.grid(True)
    plt.legend(loc="upper left")
    plt.tight_layout()
    plt.show()


if __name__=="__main__":
    
    # Lese die Daten ein
    df = read_my_csv()
    if df is not None:
        try:
            max_hr = float(input("Gib deine maximale Herzfrequenz ein: "))
            erstelle_hr_zonen_plot(df, max_hr)
        except ValueError:
            print("Bitte eine gültige Zahl für die maximale Herzfrequenz eingeben.")
            exit()

