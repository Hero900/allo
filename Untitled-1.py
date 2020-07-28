import random

nombre_m = random.randint(0, 10)
nombre = input("Quel est le nombre mystère ? ")
if nombre.isdigit():
    nombre = int(nombre)
    if nombre > nombre_m:
        print(f"Le nombre mystère est plus petit que {nombre}")
    elif nombre < nombre_m:
        print(f"Le nombre mystère est plus grand que {nombre}")
    else:
        print("Bravo, vous avez trouvé le nombre mystère !")
else:
    print("SVP, entrez un nombre valide.")    