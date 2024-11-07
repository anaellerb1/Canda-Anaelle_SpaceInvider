"""
Sanjay CANDA 3ETI
07/11/2024
Fichier de la classe pour définir le vaisseau du joueur
"""
height = 600
width = 400

class Torpille :
    def __init__(self, canvas, x, y):
        """ Initialisation de l'object torpille """
        self.canvas = canvas
        self.id = canvas.create_rectangle(x - 1, y - 2, x + 1, y + 2, fill="white")
        self.vitesse_y = 10
        self.direction = 1

    def deplacement(self):
        """ Initialisation des déplacement de la torpille """
        self.canvas.move(self.id, 0, self.vitesse_y)
        if self.canvas.coords(self.id)[1] < 0: 
            self.canvas.delete(self.id)
            return False  # Indique que le projectile doit être supprimé
        return True
    