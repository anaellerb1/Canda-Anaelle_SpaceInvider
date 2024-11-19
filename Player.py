class Player:
    def __init__(self, canvas, largeur_jeu, hauteur_jeu, interface):
        """Initialisation de l'objet joueur"""
        self.canvas = canvas
        self.largeur_jeu = largeur_jeu
        self.hauteur_jeu = hauteur_jeu
        
        # Initialisation des positions du joueur
        self.x = largeur_jeu / 2
        self.y = hauteur_jeu * (3 / 4)
        
        # Création du vaisseau sous forme de triangle
        self.id = canvas.create_polygon(
            self.x - 15, self.y + 10,  # gauche
            self.x + 15, self.y + 10,  # droit
            self.x, self.y - 10,       # haut
            fill="red",
        )
        
        self.vitesse = 5  # Vitesse du joueur (plus bas pour un contrôle plus fin)
        self.direction = 0  # 0 = pas de mouvement, 1 = droite, -1 = gauche
        
        # Lier les événements clavier
        interface.bind("<Left>", self.deplacer_gauche)
        interface.bind("<Right>", self.deplacer_droite)
        interface.bind("<KeyRelease-Left>", self.arreter_deplacement)
        interface.bind("<KeyRelease-Right>", self.arreter_deplacement)

        # Commencer la mise à jour continue du déplacement
        self.deplacement_continue()

    def deplacement(self, direction):
        """Déplacement du joueur selon la direction."""
        self.x += self.vitesse * direction

        # Limite les déplacements à l'intérieur du jeu
        if self.x < 0:
            self.x = 0
        elif self.x > self.largeur_jeu:
            self.x = self.largeur_jeu

        # Mise à jour des coordonnées du vaisseau à chaque déplacement
        self.canvas.coords(self.id, self.x - 15, self.y + 10, self.x + 15, self.y + 10, self.x, self.y - 10)

    def deplacer_gauche(self, event):
        """Déplacer le joueur vers la gauche."""
        self.direction = -1  # Déplace à gauche

    def deplacer_droite(self, event):
        """Déplacer le joueur vers la droite."""
        self.direction = 1  # Déplace à droite
    
    def arreter_deplacement(self, event):
        """Arrêter le mouvement du joueur."""
        self.direction = 0  # Arrête le déplacement

    def deplacement_continue(self):
        """Mettre à jour la position du joueur en fonction de la direction."""
        if self.direction != 0:  # Si le joueur doit se déplacer
            self.deplacement(self.direction)
        
        # Relancer la mise à jour du mouvement après un court délai (10 ms pour 100 FPS)
        self.canvas.after(10, self.deplacement_continue)  # 100 FPS
