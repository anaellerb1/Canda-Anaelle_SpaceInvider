"""
Anaëlle ROBIN  & Sanjay CANDA 3ETI
07/11/2024
Fichier de la classe pour définir le vaisseau du joueur
"""


class Alien:
    def __init__(self, canvas, x, y, width, height, vitesse_x, largeur_jeu):
        """Initialisation d'un alien."""
        self.canvas = canvas
        self.id = canvas.create_rectangle(x - 15, y - 15, x + 15, y + 15, fill="yellow")  # Dessin Alien
        self.vitesse_x = vitesse_x
        self.vitesse_y = -1
        self.direction = 1  # 1 : se déplacer vers la droite (gauche=-1)
        self.life = 25 
        self.niveau = 1
        self.largeur_jeu = largeur_jeu 

    def deplacer_aliens(self, aliens):
        """Méthode pour déplacer tous les aliens à chaque intervalle."""
        # Vérifier les aliens aux extrémités (à gauche et à droite)
        aliens_bords = self.get_bord(aliens)
        
        # Si un alien touche un bord, changer la direction et faire descendre tous les aliens
        if aliens_bords['Gauche'] or aliens_bords['Droite']:
            for alien in aliens:
                alien.direction *= -1  # Changer la direction de tous les aliens
                alien.canvas.move(alien.id, 0, 20)  # Descendre tous les aliens

        # Déplacer chaque alien horizontalement
        for alien in aliens:
            alien.canvas.move(alien.id, alien.vitesse_x * alien.direction, 0)

    def get_bord(self, aliens):
        """Retourne si un alien aux extrémités (gauche/droite) touche un bord."""
        bords = {'Gauche': False, 'Droite': False}
        
        # Vérifier si l'alien le plus à gauche touche un bord
        x1, y1, x2, y2 = self.canvas.coords(aliens[0].id)
        if x1 <= 0:  # Alien à gauche
            bords['Gauche'] = True
        
        # Vérifier si l'alien le plus à droite touche un bord
        x1, y1, x2, y2 = self.canvas.coords(aliens[-1].id)
        if x2 >= self.largeur_jeu:  # Alien à droite
            bords['Droite'] = True
        return bords