"""
Anaëlle ROBIN  & Sanjay CANDA 3ETI
07/11/2024
Fichier de la classe pour définir le vaisseau du joueur
"""

class Torpille:
    torpilles = []  # Liste partagée de toutes les torpilles dans le jeu

    def __init__(self, canvas, x, y):
        """Initialisation de la torpille"""
        self.canvas = canvas
        self.x = x
        self.y = y
        self.vitesse = 30  # Vitesse de la torpille
        
        # Création de la torpille sous forme de rectangle
        self.id = canvas.create_rectangle(
            self.x - 2, self.y - 20,  # Position de départ de la torpille
            self.x + 2, self.y - 30,  # Taille du rectangle
            fill="red",  # Couleur
        )

    def deplacer(self):
        """Déplacement de la torpille vers le haut."""
        self.y -= self.vitesse  # Déplacer la torpille vers le haut

        # Met à jour la position de la torpille
        self.canvas.coords(self.id, self.x - 2, self.y - 20, self.x + 2, self.y - 30)
        print(self.torpilles)
        # Si la torpille sort de l'écran, la supprimer
        if self.y < 0:
            self.canvas.delete(self.id)
            Torpille.torpilles.remove(self)  # Retirer la torpille de la liste
        
        else:
            # Relancer le déplacement de la torpille
            self.canvas.after(20, self.deplacer)

    @classmethod #classe en premier argument (cls) au lieu de l'instance (self).
    def tirer(cls, canvas, x, y):
        """Créer une torpille et l'ajouter à la liste des torpilles"""
        torpille = Torpille(canvas, x, y)
        cls.torpilles.append(torpille)
        torpille.deplacer()  # Lance immédiatement le déplacement de la torpille

    


