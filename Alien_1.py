"""
Sanjay CANDA 3ETI
07/11/2024
Fichier de la classe pour définir le vaisseau du joueur
"""
LARGEUR = 600
HAUTEUR = 400

# Définition de la classe des vaisseaux ennemis niveau 1
class Alien:
    def __init__(self, canvas, x, y, width, height, vitesse_x):
        self.canvas = canvas
        self.id = canvas.create_rectangle(x - 15, y - 15, x + 15, y + 15, fill="yellow") # dessin Alien
        self.vitesse_x = 2
        self.vitesse_y = -1
        self.direction = 1 # 1 : se déplacer vers la droite (gauche=-1)
        self.life=25 #vie Alien

    def deplacement_alien(self):
        """Initialisation des déplacement du vaisseau ennemi """
        x1, y1, x2, y2 = self.canvas.coords(self.id)
        if x2 >= LARGEUR or x1 <= 0:
            self.direction *= -1
            """self.canvas.move(self.id, 0, 20)"""  # Descend lorsque atteint le bord
        self.canvas.move(self.id, self.vitesse_x * self.direction, 0)
