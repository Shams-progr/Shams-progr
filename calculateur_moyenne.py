# Script pour calculer ma moyenne générale (Parcoursup / Terminale)
# Ce programme gère les notes, les coefficients et les erreurs de saisie.

def calculer_moyenne():
    print("--- Calculateur de Moyenne de Terminale ---")
    
    notes = []
    coefficients = []
    
    try:
        nb_matieres = int(input("Combien de notes veux-tu entrer ? "))
        
        for i in range(nb_matieres):
            print(f"\n--- Matière n°{i+1} ---")
            note = float(input(f"Entrez la note (sur 20) : "))
            coeff = float(input(f"Entrez le coefficient : "))
            
            # On ajoute les données dans nos listes
            notes.append(note)
            coefficients.append(coeff)
        
        # Calcul de la moyenne pondérée : Somme de (note * coeff) / Somme des coeffs
        somme_ponderee = sum(n * c for n, c in zip(notes, coefficients))
        total_coeffs = sum(coefficients)
        
        if total_coeffs == 0:
            print("\nErreur : Le total des coefficients ne peut pas être nul.")
        else:
            moyenne_finale = somme_ponderee / total_coeffs
            print("\n" + "="*30)
            print(f"TA MOYENNE GÉNÉRALE EST DE : {moyenne_finale:.2f}/20")
            print("="*30)

    except ValueError:
        print("\nErreur : Veuillez entrer des chiffres valides (utilisez le point pour les décimales).")

if __name__ == "__main__":
    calculer_moyenne()
