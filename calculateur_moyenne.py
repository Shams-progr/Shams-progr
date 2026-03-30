# Mon petit programme pour calculer ma moyenne de Terminale
# Fait pour m'entraîner sur les boucles et les listes en Python

def calculer_moyenne():
    print("--- CALCULATEUR DE MOYENNE ---")
    
    notes = []
    coefficients = []
    
    # On demande combien de matières pour savoir combien de fois boucler
    nb_notes = input("Combien de notes voulez-vous entrer ? ")
    nb_notes = int(nb_notes) 
    
    for i in range(nb_notes):
        print("Note numero", i + 1)
        
        n = float(input("Entrez la note : "))
        c = float(input("Entrez le coefficient : "))
        
        notes.append(n)
        coefficients.append(c)
    
    # Calcul de la moyenne
    somme_notes_coeff = 0
    somme_coeffs = 0
    
    for i in range(len(notes)):
        somme_notes_coeff = somme_notes_coeff + (notes[i] * coefficients[i])
        somme_coeffs = somme_coeffs + coefficients[i]
    
    if somme_coeffs != 0:
        resultat = somme_notes_coeff / somme_coeffs
        print("------------------------------")
        print("Votre moyenne est de :", resultat)
        print("------------------------------")
    else:
        print("Erreur : le total des coeffs est nul.")

# Lancement du programme
calculer_moyenne()
