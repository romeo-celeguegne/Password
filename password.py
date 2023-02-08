import re  # Import la librairie “Re”
import hashlib  # Import la librairie "Hashlib"
while True:  # Tant que
    mdp = input("Inserer mot de passe: ")
    if (len(mdp) <= 8):  # mdp inférieur à 8
        print("Mot de passe invalide")
    # mdp recherche et ne trouve pas de lettre minuscule entre a et z
    elif not re.search("[a-z]", mdp):
        print("Mot de passe invalide")
    # mdp recherche et ne trouve pas de lettre majuscule entre A et Z
    elif not re.search("[A-Z]", mdp):
        print("Mot de passe invalide")
    # mdp recherche et ne trouve pas de chiffre entre 0 et 9
    elif not re.search("[0-9]", mdp):
        print("Mot de passe invalide")
    # mdp recherche et ne trouve pas de caractère spéciale
    elif not re.search("[._@$]", mdp):
        print("Mot de passe invalide")
    else:  # sinon, mot de passe valide
        print("Mot de passe valide")
        break  # stop la boucle

encode = mdp.encode('utf-8')  # encode grâce à utf-8
maj_encode = hashlib.sha256()  # implante hashlib avec sha256
maj_encode.update(encode)  # implante maj encode avec utf-8
# dévoile le mdp crypté en hexadecimal
print("Mot de passe crypté: " + maj_encode.hexdigest())
