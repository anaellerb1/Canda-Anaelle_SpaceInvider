import tkinter as tk
import Player
import Alien_1
import Alien_2
import Alien_3

LARGEUR = 600
HAUTEUR = 400

class Jeu:
    def __init__(self, interface):
        self.interface = interface
        self.interface.title("Space Invider - Sanjay x Anaëlle")
        
        #canva de la page
        self.Canvas = tk.Canvas(interface, width=LARGEUR, height=HAUTEUR, bg='black' )
        self.Canvas.pack(anchor=tk.CENTER, expand=True)

        #Frame options
        self.frame = tk.Frame(self.interface)
        self.frame.pack()

        #en-tete
        self.Canvas.create_text(
            (300,100),
            text = "Space Invider",
            fill = "yellow",
            font = ('arial',24,"bold")
        )
        
        #score / level / vies / highest score
        self.score = 0
        self.score_label = tk.Label(self.interface, text=f"Score: {self.score}", font=("Arial", 14), fg="black")
        self.score_label.pack()

        #Start / quit button
        start_button = tk.Button(self.frame, text="Démarrer", command=self.start_game)
        start_button.pack(side=tk.LEFT, padx=10)

        """quit_button = tk.Button(self.interface, text="Quitter", command=self.interface.quit, )
        quit_button.pack(side=tk.RIGHT, padx=10)"""

        #Menu 'option'
        menubar = tk.Menu(self.interface)
        self.interface.config(menu=menubar)

        game_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Options", menu=game_menu)
        """game_menu.add_command(label="Recommencer", command=self.start_game)
        game_menu.add_separator()"""
        game_menu.add_command(label="Quitter", command=self.interface.quit)

        #Initialisation variables
        self.score = 0
        self.level = 0
        self.vies = 5

        # Bind les touches pour le déplacement du joueur
        self.interface.bind("<Left>", lambda event: self.player.deplacement(-1))
        self.interface.bind("<Right>", lambda event: self.player.deplacement(1))

    def start_game(self):
        # Code pour démarrer la partie
        self.score = 0
        self.update_score()
        
        # Initialiser le joueur
        self.player = Player(self.Canvas)
        
        # Initialiser un alien comme exemple
        self.alien = Alien_1(self.Canvas, 100, 50)
        
        # Commencer le mouvement de l'alien
        self.move_aliens()
        pass

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")
        pass


# Lancer l'interface
interface = tk.Tk()
game = Jeu(interface)
interface.mainloop()







