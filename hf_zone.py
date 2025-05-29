def berechne_hr_zonen(max_hr):
    zone1 = (round(max_hr * 0.50), round(max_hr * 0.60))
    zone2 = (round(max_hr * 0.60), round(max_hr * 0.70))
    zone3 = (round(max_hr * 0.70), round(max_hr * 0.80))
    zone4 = (round(max_hr * 0.80), round(max_hr * 0.90))
    zone5 = (round(max_hr * 0.90), round(max_hr * 1.00))

    #print(f"Maximale Herzfrequenz: {max_hr} bpm\n")
    #print("Herzfrequenz-Zonen:")
    #print(f"Zone 1 (50-60%): {zone1[0]} - {zone1[1]} bpm")
    #print(f"Zone 2 (60-70%): {zone2[0]} - {zone2[1]} bpm")
    #print(f"Zone 3 (70-80%): {zone3[0]} - {zone3[1]} bpm")
    #print(f"Zone 4 (80-90%): {zone4[0]} - {zone4[1]} bpm")
    #print(f"Zone 5 (90-100%): {zone5[0]} - {zone5[1]} bpm")

    return zone1, zone2, zone3, zone4, zone5
#if __name__ == "__main__":
    # Beispiel: Benutzereingabe
    #try:
     #   max_hr = int(input("Gib deine maximale Herzfrequenz (Max HR) ein: "))
      #  zone1, zone2, zone3, zone4, zone5 = berechne_hr_zonen(max_hr)
    #except ValueError:
     #   print("Bitte gib eine gültige Zahl ein.")
    #print(zone1)


