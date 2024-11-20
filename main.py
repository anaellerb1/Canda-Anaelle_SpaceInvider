"""
Anaëlle ROBIN  & Sanjay CANDA 3ETI
07/11/2024
Fichier de la classe pour créer le jeu
Status: 
       EN COURS
"""
import tkinter as tk
from Alien import Alien
from Player import Player

class Jeu:
    def __init__(self, interface):
        # Initialisation des variables
        self.aliens = []  
        self.score = 0
        self.LARGEUR = 200
        self.HAUTEUR = 400

        self.interface = interface
        self.interface.title("Space Invader - Sanjay x Anaëlle")

        # fenêtre
        self.center_window(self.LARGEUR, self.HAUTEUR)
        self.Canvas = tk.Canvas(interface, width=self.LARGEUR, height=self.HAUTEUR, bg='black')
        self.Canvas.pack(anchor=tk.CENTER, expand=True)

        self.frame = tk.Frame(self.interface)
        self.frame.pack()

        # En-tête
        self.Canvas.create_text(
            (300, 100),
            text="Space Invader",
            fill="yellow",
            font=('arial', 24, "bold")
        )
        
        # Score
        self.score_label = tk.Label(self.interface, text=f"Score: {self.score}", font=("Arial", 14), fg="black")
        self.score_label.pack()

        # Start button
        start_button = tk.Button(self.frame, text="Démarrer", command=self.start_game)
        start_button.pack(side=tk.LEFT, padx=10)

        # Menu 'option'
        menubar = tk.Menu(self.interface)
        self.interface.config(menu=menubar)

        game_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Options", menu=game_menu)
        game_menu.add_command(label="Quitter", command=self.interface.quit)

        

    def center_window(self, width, height):
        """Centre la fenêtre sur l'écran."""
        screen_width = self.interface.winfo_screenwidth()  # Largeur de l'écran
        screen_height = self.interface.winfo_screenheight()  # Hauteur de l'écran

        # Calculer la position pour centrer la fenêtre
        position_top = int(screen_height / 2 - height / 2)
        position_left = int(screen_width / 2 - width / 2)

        # Appliquer la géométrie de la fenêtre
        self.interface.geometry(f'{width}x{height}+{position_left}+{position_top}')

    def start_game(self):
        """Code pour démarrer la partie."""
        self.score = 0
        self.update_score()
        
        """Partie Alien"""
        for alien in self.aliens:
            self.Canvas.delete(alien.id)
        self.aliens = []  # Réinitialiser la liste

        for i in range(5):  # 5 colonnes
            for j in range(3):  # 3 rangées
                x = 100 + i * 50
                y = 50 + j * 50
                alien = Alien(self.Canvas, x, y, 40, 40, 0.1, self.LARGEUR) 
                self.aliens.append(alien)

        self.deplacer_aliens()

        """Partie Joueur"""
        self.joueur = Player(self.Canvas, self.LARGEUR, self.HAUTEUR, interface)
    

    def update_score(self):
        """Met à jour l'affichage du score."""
        self.score_label.config(text=f"Score: {self.score}")

    def deplacer_aliens(self):
        """Déplace tous les aliens à chaque intervalle."""
        # Déplacer tous les aliens
        for alien in self.aliens:
            alien.deplacer_aliens(self.aliens)

        # Relancer le mouvement après un court délai
        self.interface.after(16, self.deplacer_aliens)
    


# Lancer l'interface
interface = tk.Tk() 
game = Jeu(interface)
interface.mainloop()