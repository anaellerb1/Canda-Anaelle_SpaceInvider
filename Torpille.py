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
        self.y -= self.vitesse
        self.canvas.coords(self.id, self.x - 2, self.y - 20, self.x + 2, self.y - 30)


    @classmethod #classe en premier argument (cls) au lieu de l'instance (self).
    def tirer(cls, canvas, x, y):
        """Créer une torpille et l'ajouter à la liste des torpilles"""
        torpille = Torpille(canvas, x, y)
        cls.torpilles.append(torpille)
        torpille.deplacer()  # Lance immédiatement le déplacement de la torpille

    


