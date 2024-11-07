"""
Sanjay CANDA 3ETI
07/11/2024
Fichier de la classe pour définir le vaisseau du joueur
"""

height = 600
width = 400

# Définition de la classe vaisseau joueur
class Player :
    def __init__(self, canvas):
        """Initialisation de l'objet joueur"""
        self.canvas = canvas
        self.vitesse = 15
        self.id = canvas.create_polygon(self.x - 15, self.x + 15, self.y + 10, fill="white")
        self.x = width * (3/4)
        self.y = height - 200

    def deplacement(self, direct):
        """Initialisation des déplacment du joueur"""
        self.x += self.vitesse * direct
        if self.x < 0:
            self.x = 0
        elif self.x > width:
            self.x = width
        self.canvas.coords(self.id, self.x - 15, self.y - 10, self.x + 15, self.y + 10)


