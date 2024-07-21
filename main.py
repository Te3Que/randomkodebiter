import math

def finn_lengden(vektor):
    """
    Denne funksjonen har i oppgave aa ta en vektor 
    som en liste og returnerer lengden på vektoren.
    """

    # Oppretter en variabel slik vi kan lagre kvadratsummen av elementene i vektoren
    kvadratsum = 0

    #  Her gaar vi over alle elementene i vektoren
    for tall in vektor:
        # Kvadrer hvert element og legger til kvadratsummen
        kvadratsum += tall ** 2

    # Beregn lengden ved å ta kvadratroten av kvadratsummen
    lengde = math.sqrt(kvadratsum)

    # Returner den beregna lengda
    return lengde

# 2D vektorane som er ment vi skal rekne ut
a = [4, -3]
b = [14, 5]
c = [5, -3]

# Finn lengda på vektorane a, b og c og lagre dem i variabler
a_Lengden = finn_lengden(a)
b_Lengden = finn_lengden(b)
c_Lengden = finn_lengden(c)

# Skriv ut produktet vi har reknet ut
print(f"Lengden på vektor a er: {a_Lengden}")
print(f"Lengden på vektor b er: {b_Lengden}")
print(f"Lengden på vektor c er: {c_Lengden}")
