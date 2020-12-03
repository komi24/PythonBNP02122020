# from PackageBNP.mon_module import dire_bonjour
from PackageBNP import say_hi, dire_bonjour

# faite deux modules french, english
# Dans french.py definir dire_bonjour
# Dans english.py definir say_hi
# Chacune de ses fonctions prend obligatoirement first_name et last_name.
# En paramètre otpionnel on aura age (30) et city (Paris)
# Elle doivent afficher "Hello I am first_name last_name. I live in city and I'm age y.o."

dire_bonjour("Martin", "Meuriot", 35, "Bordeaux")
say_hi("Mélanie", "Dupont", city="Valence")
