"""
Sanjay CANDA 3ETI
07/11/2024
Fichier de la classe pour définir le vaisseau du joueur
"""
height = 600
width = 400

# Définition de la classe des vaisseaux ennemis niveau 2
class Alien_2:
    def __init__(self, canvas, x, y):
        """Initialisation de l'object vaisseau ennemi """
        self.canvas = canvas
        self.id = canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="orange")
        self.vitesse_x = 2
        self.vitesse_y = 1
        self.direction = 1
        self.life=50

    def deplacement_alien(self):
        """Initialisation des déplacement du vaisseau ennemi """
        x1, y1, x2, y2 = self.canvas.coords(self.id)
        if x2 >= width or x1 <= 0:
            self.direction *= -1
            """self.canvas.move(self.id, 0, 20)"""  # Descend lorsque atteint le bord
        self.canvas.move(self.id, self.vitesse_x * self.direction, 0)