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

        self.verifier_collision()

        if self.y < 0:
            self.canvas.delete(self.id)
            Torpille.torpilles.remove(self) 
        else:
            self.canvas.after(20, self.deplacer)

    def verifier_collision(self):
        """Vérifie si la torpille touche un alien"""
        for alien in self.canvas.winfo_children():
            if isinstance(alien, Alien):
                if self.collision(alien):
                    self.canvas.delete(alien.id) 
                    self.canvas.delete(self.id)   
                    Torpille.torpilles.remove(self)  
                    break  
    
    def collision(self, alien):
        """Vérifier si la torpille touche un alien"""
        # Obtenez les coordonnées de la torpille et de l'alien
        tx1, ty1, tx2, ty2 = self.canvas.coords(self.id)  # Coordonnées de la torpille
        ax1, ay1, ax2, ay2 = self.canvas.coords(alien.id)  # Coordonnées de l'alien

        # Vérifier si les boîtes englobantes de la torpille et de l'alien se chevauchent
        if tx2 > ax1 and tx1 < ax2 and ty2 > ay1 and ty1 < ay2:
            return True
        return False               

    @classmethod #classe en premier argument (cls) au lieu de l'instance (self).
    def tirer(cls, canvas, x, y):
        """Créer une torpille et l'ajouter à la liste des torpilles"""
        torpille = Torpille(canvas, x, y)
        cls.torpilles.append(torpille)
        torpille.deplacer()  

    


