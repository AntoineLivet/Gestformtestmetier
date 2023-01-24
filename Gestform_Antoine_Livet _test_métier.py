# initialisation des chaînes de caractères
a="" 
b=""
c=""
# choix du nombre
print("Veuillez choisir un nombre"),
n = input()
# étendu des valeurs possible de n
if int(n) > -10000 and int(n) < 10000:
    # n divisible par 3
    if int(n) % 3 == 0 and int(n) % 5 != 0:
        a="Geste"
    # n divisible par 5
    elif int(n) % 3 != 0 and int(n) % 5 == 0:
        b = "Forme"
    # n divisible par 3 et par 5
    elif int(n) % 3 == 0 and int(n) % 5 == 0:
        c = "Gestform"
    # Autre cas par défault
    else:
        print("", n),
    #écriture du mot
    print("",a,b,c)