"""
Anaëlle ROBIN  & Sanjay CANDA 3ETI
07/11/2024
Fichier de la classe Jeu
Status: 
       EN COURS
"""
import tkinter as tk
from Alien import Alien
from Player import Player
from Torpille import Torpille

class Jeu:
    def __init__(self, interface):
        # Initialisation des variables
        self.aliens = []  
        self.score = 0
    
        self.interface = interface
        self.interface.title("Space Invader - Sanjay x Anaëlle")

        # Fenêtre
        self.HAUTEUR = self.interface.winfo_screenheight()  # Ajuster la hauteur pour laisser de la place en bas
        self.LARGEUR = self.interface.winfo_screenwidth() // 3
        self.center_window(self.LARGEUR, self.HAUTEUR)
        
        self.Canvas = tk.Canvas(self.interface, width=self.LARGEUR, height=self.HAUTEUR -100, bg='black')
        self.Canvas.pack(anchor=tk.CENTER, expand=True)

        self.frame = tk.Frame(self.interface)
        self.frame.pack()

        # En-tête
        self.Canvas.create_text(
            (self.HAUTEUR / 3, self.LARGEUR / 6),
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
        screen_width = self.interface.winfo_screenwidth()
        screen_height = self.interface.winfo_screenheight()

        x = (screen_width / 2) - (width / 2) 
        y = 0
        self.interface.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

    def initialiser_jeu(self):
        self.score = 0
        self.update_score()
        self.Canvas.delete("all")
        self.aliens = []

    def start_game(self):
        """Code pour démarrer la partie."""
        self.initialiser_jeu()
        for i in range(5):
            for j in range(3):
                x = 100 + i * 50
                y = 50 + j * 50
                alien = Alien(self.Canvas, int(x), int(y), 0.1, self.LARGEUR)
                self.aliens.append(alien)

        self.joueur = Player(self.Canvas, self.LARGEUR, self.HAUTEUR, self.interface)

        self.update_game()

    def update_score(self):
        """Met à jour l'affichage du score."""
        self.score_label.config(text=f"Score: {self.score}")

    def deplacer_aliens(self):
        """Déplace tous les aliens à chaque intervalle."""
        for alien in self.aliens:
            alien.deplacer_aliens(self.aliens)
        
    def is_collision(self):
        """Vérifie les collisions entre les torpilles et les aliens."""
        for torpille in list(Torpille.torpilles): 
            torpille_coords = self.Canvas.coords(torpille.id) 
            if not torpille_coords:
                continue  
            for alien in list(self.aliens):  
                alien_coords = self.Canvas.coords(alien.id)  
                if not alien_coords:
                    continue 
                # Vérifier les collisions en comparant les rectangles
                if (
                    torpille_coords[0] < alien_coords[2] and
                    torpille_coords[2] > alien_coords[0] and
                    torpille_coords[1] < alien_coords[3] and
                    torpille_coords[3] > alien_coords[1]
                ):
                    # Supprimer les objets en cas de collision
                    self.Canvas.delete(alien.id)
                    self.aliens.remove(alien)
                    self.Canvas.delete(torpille.id)
                    Torpille.torpilles.remove(torpille)
                    
                    # Mettre à jour le score
                    self.score += 1
                    self.update_score()
                    break

    def update_game(self):
        """Mise à jour de l'état du jeu."""
        # Déplacer les aliens
        for alien in self.aliens:
            alien.deplacer_aliens(self.aliens)
            
        # Déplacer les torpilles
        for torpille in list(Torpille.torpilles): 
            torpille.deplacer()
        
        # Vérifier les collisions
        self.is_collision()

        # Relancer l'update après un délai
        self.interface.after(32, self.update_game)


# Lancer l'interface
interface = tk.Tk() 
game = Jeu(interface)
interface.mainloop()