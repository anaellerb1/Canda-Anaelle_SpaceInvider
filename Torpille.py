"""
Anaëlle ROBIN  & Sanjay CANDA 3ETI
07/11/2024
Fichier de la classe Torpille
"""
class Torpille:
    MAX_TORPILLES = 1

    def __init__(self, canvas, x, y):
        """Initialisation de la torpille"""
        self.canvas = canvas
        self.x = x
        self.y = y
        self.vitesse = 20
        self.id = canvas.create_rectangle(
            self.x - 2, self.y - 20,  # Position de départ de la torpille
            self.x + 2, self.y - 30,  # Taille du rectangle
            fill="red",  # Couleur
        )

    def deplacer(self, torpilles):
        """Déplacement de la torpille vers le haut."""
        self.y -= self.vitesse
        self.canvas.coords(self.id, self.x - 2, self.y - 20, self.x + 2, self.y - 30)
        if self.y < 0:
            self.canvas.delete(self.id)
            torpilles.remove(self)

    @classmethod #classe en premier argument (cls) au lieu de l'instance (self).
    def tirer(cls, canvas, x, y, torpilles=list):
        """Créer une torpille et l'ajouter à la liste des torpilles"""
        if len(torpilles) < cls.MAX_TORPILLES:
            torpille = Torpille(canvas, int(x), int(y))
            torpilles.append(torpille)
            torpille.deplacer(torpilles) 

    


