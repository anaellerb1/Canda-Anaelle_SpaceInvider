"""
Anaëlle ROBIN  & Sanjay CANDA 3ETI
07/11/2024
Fichier de la classe Torpille
"""
import random
class Torpille:
    MAX_TORPILLES_joueur = 10
    MAX_TORPILLES_alien = 1

    def __init__(self, canvas, x, y, direction):
        """Initialisation de la torpille"""
        self.canvas = canvas
        self.x = x
        self.y = y
        self.direction = direction
        self.vitesse = 20
        self.id = canvas.create_rectangle(
            self.x - 2, self.y - 20,  # Position de départ de la torpille
            self.x + 2, self.y - 30,  # Taille du rectangle
            fill="red",  # Couleur
        )

    def deplacer(self, torpilles,):
        """Déplacement de la torpille vers le haut."""
        self.y -= self.vitesse * self.direction
        self.canvas.coords(self.id, self.x - 2, self.y - 20, self.x + 2, self.y - 30)
        if self.y < 0 or self.y > 600:
            self.canvas.delete(self.id)
            torpilles.remove(self)

    @classmethod #classe en premier argument (cls) au lieu de l'instance (self).
    def tirer(cls, canvas, x, y, torpilles_joueur=list):
        """Créer une torpille et l'ajouter à la liste des torpilles"""
        if len(torpilles_joueur) < cls.MAX_TORPILLES_joueur:
            torpille = Torpille(canvas, int(x), int(y), direction=1)
            torpilles_joueur.append(torpille)
            torpille.deplacer(torpilles_joueur) 
    
    @classmethod
    def tire_alien(cls, aliens, torpilles_alien):
        """Un alien aléatoire tire une torpille"""
        alien = random.choice(aliens)
        if len(torpilles_alien) < cls.MAX_TORPILLES_alien:
            torpille = Torpille(alien.canvas, alien.x, alien.y, direction=-1)
            torpille.canvas.itemconfig(torpille.id, fill="yellow")
            torpilles_alien.append(torpille)
            torpille.deplacer(torpilles_alien)


