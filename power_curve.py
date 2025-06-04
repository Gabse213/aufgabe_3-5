import pandas as pd
import matplotlib.pyplot as plt

def load_data(path='data/activities/activity.csv'):
    df = pd.read_csv(path)
    t_end = len(df)
    time = pd.Series(range(t_end))
    df["time"] = time
    return df

def create_powercurve_df(df, window_sizes=[1, 5, 10, 30, 60, 300, 600, 1800,3600]):
    all_effort = []
    for window in window_sizes:
        # Gleitender Durchschnitt für das jeweilige Zeitfenster und davon der höchste Wert
        best_power = find_best_effort(df["PowerOriginal"], window)
        all_effort.append(best_power)
    df_2 = pd.DataFrame({
    'time': window_sizes,
    'power': all_effort
})
    return df_2

def find_best_effort(series, window_size):
    best_effort=series.rolling(window=window_size).mean().max()

    return best_effort

def plot_best_effort_curve(df_2):
    #durations = df_2(window_size)
    #powers = list(all_effort.values())

    fig, ax = plt.subplots(figsize=(10, 5))
    
    ax.plot(df_2, marker="o")
    ax.set_xscale("log")
    
    xtick_labels = []
    ax.set_xticks()
    ax.set_xticklabels(xtick_labels)
    
    ax.set_xlabel("Dauer")
    ax.set_ylabel("Power (W)")
    ax.set_title("Power Curve")
    ax.grid(True)
    
    fig.tight_layout()
    plt.show()
    fig.savefig("power_curve.png")  # Optional: Speichere die Grafik als PNG-Datei

    return fig  # Optional: damit du die Figure später speichern oder weiterverwenden kannst


if __name__ == "__main__":
    

    df_1=load_data()
    print(df_1.head())
    print(df_1["PowerOriginal"])
    best_effort=find_best_effort(df_1["PowerOriginal"],120)
    print(best_effort)
    versuch =create_powercurve_df(df_1)
    print(versuch)
    plot_best_effort_curve



