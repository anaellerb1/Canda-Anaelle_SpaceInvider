"""
Anaëlle ROBIN  & Sanjay CANDA 3ETI
07/11/2024
Fichier de la classe pour définir le vaisseau du joueur
"""
from Alien import Alien

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

        # Si la torpille sort de l'écran ou touche un alien, la supprimer
        if self.y < 0:
            self.torpilles.remove(self)
            self.canvas.delete(self.id)
        else:
            # Vérifier si la torpille touche un alien
            self.toucher_alien()
        
        
        # Répéter le déplacement toutes les 10 ms
        self.canvas.after(10, self.deplacer)
    
    def toucher_alien(self):
        """
        Vérifie si la torpille touche un alien. 
        Si c'est le cas, diminue la vie de l'alien et supprime la torpille.
        """
        # Récupérer les coordonnées de la torpille
        x1, y1, x2, y2 = self.canvas.coords(self.id)
        
        # Vérifier si la torpille touche un alien
        for alien in Jeu.aliens:
            x1_alien, y1_alien, x2_alien, y2_alien = self.canvas.coords(alien.id)
            if (x1_alien < x1 < x2_alien or x1_alien < x2 < x2_alien) and (y1_alien < y1 < y2_alien or y1_alien < y2 < y2_alien):
                # La torpille touche un alien
                alien.life -= 1
                if alien.life == 0:
                    Jeu.aliens.remove(alien)
                    self.canvas.delete(alien.id)
                self.torpilles.remove(self)
                self.canvas.delete(self.id)
                break
        

    @classmethod #classe en premier argument (cls) au lieu de l'instance (self).
    def tirer(cls, canvas, x, y):
        """Créer une torpille et l'ajouter à la liste des torpilles"""
        torpille = Torpille(canvas, x, y)
        cls.torpilles.append(torpille)
        torpille.deplacer()  # Lance immédiatement le déplacement de la torpille

    


