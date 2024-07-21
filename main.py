import math

def finn_lengden(vektor):
    """
    Denne funksjonen har i oppgave aa tar en vektor 
    som en liste og returnerer lengden på vektoren.

    Args:
        vektor: En liste som representerer en vektor med tall.

    Returns:
        Lengden på vektoren som et flyttall.
    """

    # Oppretter en variabel slik vi kan lagre kvadratsummen av elementene i vektoren
    kvadratsum = 0

    #  Her gaar vi over alle elementene i vektoren
    for tall in vektor:
        # Kvadrer hvert element og legg til kvadratsummen
        kvadratsum += tall ** 2

    # Beregn lengden ved å ta kvadratroten av kvadratsummen
    lengde = math.sqrt(kvadratsum)

    # Returner den beregnede lengden
    return lengde

# 2D vektorane vi skal rekne ut
a = [4, -3]
b = [14, 5]
c = [5, -3]

# Finn lengden på vektorane a, b og c og lagre dem i variabler
lengde_a = finn_lengden(a)
lengde_b = finn_lengden(b)
lengde_c = finn_lengden(c)

# Skriv ut produktet vi har reknet ut
print(f"Lengden på vektor a er: {lengde_a}")
print(f"Lengden på vektor b er: {lengde_b}")
print(f"Lengden på vektor c er: {lengde_c}")
