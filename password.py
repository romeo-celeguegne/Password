import re
import hashlib
while True:
    mdp = input("Veuillez inserer un mot de passe valide: ")
    if (len(mdp) < 8):
        print("Mot de passe invalide")
    elif not re.search("[a-z]", mdp):
        print("Mot de passe invalide")
    elif not re.search("[A-Z]", mdp):
        print("Mot de passe invalide")
    elif not re.search("[@*.?$]", mdp):
        print("Mot de passe invalide")
    elif not re.search("[0-9]", mdp):
        print("Mot de passe invalide")
    else:
        print("Bienvenue")
        break

encode = mdp.encode('utf-8')
maj_encode = hashlib.sha256()
maj_encode.update(encode)
print("Mot de passe crypté: " + maj_encode.hexdigest())
