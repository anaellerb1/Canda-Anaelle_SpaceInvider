import tkinter as tk
from tkinter import Menu
from Alien import Alien
from Player import Player
from Torpille import Torpille

class Jeu:
    def __init__(self, interface):
        # Initialisation des variables
        self.aliens = []  
        self.score = 0
        self.LARGEUR = 200
        self.HAUTEUR = 400
        self.jeu_en_pause = False  # État du jeu (pause ou non)

        self.interface = interface
        self.interface.title("Space Invader - Sanjay x Anaëlle")

        # Fenêtre
        self.HAUTEUR = self.interface.winfo_screenheight() - 100
        self.LARGEUR = self.interface.winfo_screenwidth() // 3
        self.center_window(self.LARGEUR, self.HAUTEUR)
        
        self.Canvas = tk.Canvas(self.interface, width=self.LARGEUR, height=self.HAUTEUR, bg='black')
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
        start_button = tk.Button(self.frame, text="Jouer", command=self.start_game)
        start_button.pack(side=tk.LEFT, padx=10)

        # Menu 'option'
        menubar = tk.Menu(self.interface)
        self.interface.config(menu=menubar)

        game_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Options", menu=game_menu)
        game_menu.add_command(label="Quitter", command=self.interface.quit)

        # Lier Échap au menu pause
        self.interface.bind("<Escape>", self.afficher_menu_pause)

    def center_window(self, width, height):
        """Centre la fenêtre sur l'écran."""
        screen_width = self.interface.winfo_screenwidth()
        screen_height = self.interface.winfo_screenheight()

        x = (screen_width / 2) - (width / 2) 
        y = 0
        self.interface.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

    def start_game(self):
        """Code pour démarrer la partie."""
        self.score = 0
        self.update_score()
        
        # Réinitialisation des aliens
        for alien in self.aliens:
            self.Canvas.delete(alien.id)
        self.aliens = []  

        # Exemple simple d'initialisation (à adapter à votre classe Alien)
        for i in range(5):  # 5 colonnes
            for j in range(3):  # 3 rangées
                x = 100 + i * 50
                y = 50 + j * 50
                alien = Alien(self.Canvas, x, y, 40, 40, 0.1, self.LARGEUR) 
                self.aliens.append(alien)

        self.deplacer_aliens()

        # Initialisation joueur (à adapter à votre classe Player)
        self.joueur = Player(self.Canvas, self.LARGEUR, self.HAUTEUR, self.interface)

    def update_score(self):
        """Met à jour l'affichage du score."""
        self.score_label.config(text=f"Score: {self.score}")

    def deplacer_aliens(self):
        """Déplace tous les aliens."""
        if not self.jeu_en_pause:  # Vérifie si le jeu est en pause
            for alien in self.aliens:
                alien.deplacer_aliens(self.aliens)
        self.interface.after(16, self.deplacer_aliens)

    def afficher_menu_pause(self, event=None):
        """Affiche le menu pause."""
        self.jeu_en_pause = True  # Met le jeu en pause
        menu = tk.Toplevel(self.interface)
        menu.title("Menu Pause")
        menu.geometry("300x200")
        menu.transient(self.interface)
        menu.grab_set()

        # Ajouter des boutons
        tk.Button(menu, text="Reprendre le jeu", command=lambda: [menu.destroy(), self.reprendre_jeu()]).pack(pady=10)
        tk.Button(menu, text="Quitter", command=self.interface.quit).pack(pady=10)

    def reprendre_jeu(self):
        """Reprend le jeu après la pause."""
        self.jeu_en_pause = False

    def deplacer_torpilles(self):
        if not self.jeu_en_pause:  # Vérifie si le jeu est en pause
            for torpille in Torpille.torpilles:
                torpille.deplacer()
        self.interface.after(50, self.deplacer_torpilles)


# Lancer l'interface
interface = tk.Tk() 
game = Jeu(interface)
interface.mainloop()
