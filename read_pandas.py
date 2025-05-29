# Paket für Bearbeitung von Tabellen
import numpy as np
import pandas as pd


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

max_hr = float(input("Gib deine maximale Herzfrequenz (Max HR) ein: "))
zone1 = (round(max_hr * 0.50), round(max_hr * 0.60))
zone2 = (round(max_hr * 0.60), round(max_hr * 0.70))
zone3 = (round(max_hr * 0.70), round(max_hr * 0.80))
zone4 = (round(max_hr * 0.80), round(max_hr * 0.90))
zone5 = (round(max_hr * 0.90), round(max_hr * 1.00))


print(zone1)


def make_plot(df):
    

    # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
    fig = px.line(df.head(2000), x= "time", y=["PowerOriginal", "HeartRate"])
    return fig

if __name__=="__main__":
    
    # Lese die Daten ein
    df = read_my_csv()
    print(df.head())
    fig = make_plot(df)
    # Zeige den Plot an
    dfzone1 = df["HeartRate"] == zone1
    filter2 = df["HeartRate"] == "zone2"
    filter3 = df["HeartRate"] == "zone3"
    filter4 = df["HeartRate"] == "zone4"
    filter5 = df["HeartRate"] == "zone5"
    df = df.where(dfzone1 | filter2 | filter3 | filter4 | filter5)
    fig.show()
#df = read_my_csv()
#fig = make_plot(df)

#fig.show()

