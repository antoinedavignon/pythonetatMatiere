from typing import Final

from scipy import constants

TRILLION: Final = constants.exa
ZÉRO_ABSOLU: Final = -constants.zero_Celsius

print("Quelle est la température de l'eau?")
température = float(input("Température de l'eau:"))

if température < ZÉRO_ABSOLU:
    print("Impossible, vérifiez la valeur saisie.")
elif température < 0:
    print("Solide : glace.")
elif température < 100:
    print("Liquide.")
elif température < 2200:
    print("Gaz avec moins de 3% d'atomes libres.")
elif température < 12e3:  # notation scientifique
    print("Gaz avec un certain % d'atomes libres.")
elif température < 4 * TRILLION:
    print("Gaz ionisé (plasma) d'hydrogène et d'oxygène.")
else:
    print("Ce n'est clairement plus de l'eau.")
