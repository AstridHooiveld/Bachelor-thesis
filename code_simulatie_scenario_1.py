# Python-script: Simulatie voor Scenario 1 (aangepast model na tweede feedbackronde)

# Vul hieronder de juiste waarden in:
ECT = 5.5      # Randsterkte in kN/m
t = 4          # Dikte in mm
P = 1700       # Omtrek doos in mm
Gv = 0.6       # Gewicht verpakking (kg)
Gp = 5         # Gewicht product (kg)
g = 9.81       # Zwaartekracht (m/s^2)

D1 = 64        # Sensorwaarde 1 (N)
D2 = 65        # Sensorwaarde 2 (N)
D3 = 63        # Sensorwaarde 3 (N)
D4 = 64        # Sensorwaarde 4 (N)

# Bereken BCT volgens McKee-formule
BCT = 5.876 * ECT * ((t * P) ** 0.5)

# Pas praktijkfactor toe (90% van BCT gebruiken)
praktijkfactor = 0.9
BCT_correctie = BCT * praktijkfactor

# Sensoranalyse: gemiddelde, standaarddeviatie en CV
Dgem = (D1 + D2 + D3 + D4) / 4
stdev = (((D1 - Dgem) ** 2 + (D2 - Dgem) ** 2 + (D3 - Dgem) ** 2 + (D4 - Dgem) ** 2) / 4) ** 0.5

if Dgem != 0:
    CV = (stdev / Dgem) * 100
else:
    CV = 0

# Bepaal dynamische veiligheidsfactor volgens fijnmazige schaal
if CV < 16:
    f = 1.1 + 0.1 * CV
else:
    f = None  # Niet meer stapelen

# Bereken maximale stapelhoogte
totaal_gewicht = (Gv + Gp) * g

if f is not None and totaal_gewicht > 0:
    n = int(BCT_correctie / (totaal_gewicht * f))
else:
    n = 0


# Resultaten printen
print("Scenario (nieuw model):")
print("BCT (N):", round(BCT, 2))
print("BCT na praktijkfactor (N):", round(BCT_correctie, 2))
print("CV (%):", round(CV, 2))
if f is not None:
    print("Veiligheidsfactor:", round(f, 2))
    print("Maximale stapelhoogte (lagen):", n)
else:
    print("Veiligheidsfactor: niet meer stapelen (CV ≥ 16%)")
    print("Maximale stapelhoogte (lagen): 0")

