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
        self.torpilles_joueur = [] 
        self.torpilles_alien = []
        self.player_life = 3
        self.vie_label = None
        self.score = 0
        self.score_label = None

        self.jeu = False
        self.pause = False
        self.pause_interface = []
        self.win = False
        self.win_interface = []
        self.loose = False
        self.loose_interface = []
    
        self.interface = interface
        self.interface.title("Space Invader - Sanjay x Anaëlle")

        # Fenêtre
        self.HAUTEUR = self.interface.winfo_screenheight() 
        self.LARGEUR = self.interface.winfo_screenwidth() // 3
        self.center_window(self.LARGEUR, self.HAUTEUR)
        
        self.Canvas = tk.Canvas(self.interface, width=self.LARGEUR, height=self.HAUTEUR -100, bg='black')
        self.Canvas.pack(anchor=tk.CENTER, expand=True)

        self.frame = tk.Frame(self.interface)
        self.frame.pack()

        # En-tête
        self.Canvas.create_text(
            (self.LARGEUR / 2, self.HAUTEUR / 6),
            text="Space Invader",
            fill="yellow",
            font=('arial', 24, "bold")
        )

        # Start button
        self.start_button = tk.Button(self.frame, text="Démarrer", command=self.start_game, state="active")
        self.start_button.pack(side=tk.LEFT, padx=10)

        # Menu 'option'
        menubar = tk.Menu(self.interface)
        self.interface.config(menu=menubar)

        game_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Options", menu=game_menu)
        game_menu.add_command(label="Quitter", command=self.interface.quit)

    def setBinds(self):
        """Définit les touches du jeu."""
        self.interface.bind("<KeyPress-Left>", self.joueur.deplacer_gauche)
        self.interface.bind("<KeyPress-Right>", self.joueur.deplacer_droite)
        self.interface.bind("<KeyRelease-Left>", self.joueur.arreter_deplacement)
        self.interface.bind("<KeyRelease-Right>", self.joueur.arreter_deplacement)
        self.interface.bind("<space>", lambda event: Torpille.tirer(self.joueur.canvas, int(self.joueur.x), int(self.joueur.y), self.torpilles_joueur))
        self.interface.bind("<Escape>", self.pause_game)

    def center_window(self, width, height):
        """Centre la fenêtre sur l'écran."""
        screen_width = self.interface.winfo_screenwidth()
        x = (screen_width // 2) - (width // 2) 
        y = 0
        self.interface.geometry(f'{width}x{height}+{x}+{y}')

    def initialiser_jeu(self):
        """Initialise les variables du jeu."""
        self.score = 0
        self.player_life = 3
        self.update_score_life()
        self.Canvas.delete("all")
        self.aliens = []
        self.torpilles_joueur = []
        self.torpilles_alien = []
        self.jeu = True
        self.start_button.config(state="disabled")
        self.vie_label = self.Canvas.create_text(
            (self.LARGEUR-50, 30),
            text=f"Life: {self.player_life}",
            fill="white",
            font=('arial', 13, "italic")
        )
        self.score_label = self.Canvas.create_text(
            (50, 30),
            text=f"Score: {self.score}",
            fill="white",
            font=('arial', 13, "italic")
        )

    def start_game(self):
        """Code pour démarrer la partie."""
        self.initialiser_jeu()
        for i in range(5):
            for j in range(3):
                x = 100 + i * 50
                y = 50 + j * 50
                alien = Alien(self.Canvas, int(x), int(y), self.LARGEUR)
                self.aliens.append(alien)

        self.joueur = Player(self.Canvas, self.LARGEUR, self.HAUTEUR, self.interface)
        self.setBinds()
        self.update_game()

    def pause_game(self, event=None):
        """Code pour mettre en pause la partie."""
        self.pause = not self.pause
        if self.pause:
            self.jeu = False
            self.pause_interface = self.affichagetexte()
            self.resume_button = tk.Button(self.interface, text="Reprendre", command=self.pause_game)
            self.Canvas.create_window(self.LARGEUR / 2, self.HAUTEUR / 2 + 10, window=self.resume_button)
            self.quit_button = tk.Button(self.interface, text="Quitter", command=self.interface.quit)
            self.Canvas.create_window(self.LARGEUR / 2, self.HAUTEUR / 2 + 50, window=self.quit_button)
        else:
            for item in self.pause_interface:
                self.Canvas.delete(item)
            self.resume_button.destroy()
            self.quit_button.destroy()
            self.jeu = True
            self.update_game()
            self.setBinds()

    def affichagetexte(self):
        """Affichage des textes du jeu."""
        rectangle_flou = self.Canvas.create_rectangle(0, self.HAUTEUR, self.LARGEUR, 0, fill="black", stipple="gray50")
        score_text = self.Canvas.create_text(
            (self.LARGEUR / 2, self.HAUTEUR / 3 + 40),
            text=f"Score: {self.score}",
            fill="white",
            font=('arial', 13, "italic")
        )
        life_text = self.Canvas.create_text(
            (self.LARGEUR / 2, self.HAUTEUR / 3 + 60),
            text=f"Life: {self.player_life}",
            fill="white",
            font=('arial', 13, "italic")
        )

        if self.pause:  # texte de pause
            pause_interface = [
                rectangle_flou,
                self.Canvas.create_text(
                    (self.LARGEUR / 2, self.HAUTEUR / 3),
                    text="Pause",
                    fill="red",
                    font=('arial', 24, "bold")
                ),
                score_text,
                life_text
            ]
            return pause_interface
        if self.win:
            win_interface = [
                rectangle_flou,
                self.Canvas.create_text(
                    (self.LARGEUR / 2, self.HAUTEUR / 3),
                    text="Victoire !",
                    fill="green",
                    font=('arial', 24, "bold")
                ),
                score_text,
                life_text,
                self.Canvas.create_text(
                    (self.LARGEUR / 2, self.HAUTEUR / 3 + 80),
                    text="Appuyez sur 'Démarrer' pour rejouer",
                    fill="green",
                    font=('arial', 13, "bold")
                )
            ]
            return win_interface
        if self.loose:
            loose_interface = [
                rectangle_flou,
                self.Canvas.create_text(
                    (self.LARGEUR / 2, self.HAUTEUR / 3),
                    text="Game Over",
                    fill="red",
                    font=('arial', 24, "bold")
                ),
                score_text,
                life_text,
                self.Canvas.create_text(
                    (self.LARGEUR / 2, self.HAUTEUR / 3 + 80),
                    text="Appuyez sur 'Démarrer' pour rejouer",
                    fill="red",
                    font=('arial', 13, "bold")
                )
            ]
            return loose_interface
            
    def update_score_life(self):
        """Met à jour l'affichage du score et de la vie."""
        self.Canvas.itemconfig(self.score_label, text=f"Score: {self.score}") 
        self.Canvas.itemconfig(self.vie_label, text=f"Life: {self.player_life}")   

    def deplacer_aliens(self):
        """Déplace tous les aliens à chaque intervalle."""
        if self.aliens:
            self.aliens[0].deplacer_aliens(self.aliens)
            
            Torpille.tire_alien(self.aliens, self.torpilles_alien)
              
    def is_collision(self):
        """Vérifie les collisions entre les torpilles et les aliens."""
        joueur_coords = self.Canvas.coords(self.joueur.id)

        if self.aliens == []:
            self.gamewin()
        
        for alien in list(self.aliens):
            alien_coords = self.Canvas.coords(alien.id)  
            if not alien_coords:
                continue
            
            #Colisions avec torpilles
            for torpille in list(self.torpilles_joueur):
                torpille_coords = self.Canvas.coords(torpille.id)
                if not torpille_coords:
                    continue  # Si la torpille n'existe pas, passer à la suivante

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
                    self.torpilles_joueur.remove(torpille)
                    
                    # Mettre à jour le score
                    self.score += 1
                    self.update_score_life()
                    break
            
            for torpille in list(self.torpilles_alien):
                torpille_coords = self.Canvas.coords(torpille.id)
                if not torpille_coords:
                    continue
                if (
                    torpille_coords[0] < joueur_coords[2] and
                    torpille_coords[2] > joueur_coords[0] and
                    torpille_coords[1] < joueur_coords[3] and
                    torpille_coords[3] > joueur_coords[1]
                ):
                    self.player_life -= 1
                    self.Canvas.delete(torpille.id)
                    self.update_score_life()
                    break
            
            #Colisions alien avec le joueur 
            if (
                joueur_coords[0] < alien_coords[2] and
                joueur_coords[2] > alien_coords[0] and
                joueur_coords[1] < alien_coords[3] and
                joueur_coords[3] > alien_coords[1]
            ):
                self.gameover()
                break
            
    def update_game(self):
        """Mise à jour de l'état du jeu."""
        
        if self.player_life < 1:
            self.gameover()

        # Déplacer les aliens
        self.deplacer_aliens()

        # Déplacer les torpilles
        for torpille in list(self.torpilles_joueur): 
            torpille.deplacer(self.torpilles_joueur)
        for torpille in list(self.torpilles_alien):
            torpille.deplacer(self.torpilles_alien)
        
        # Vérifier les collisions
        self.is_collision()

        if self.jeu:
            # Relancer l'update après un délai
            self.interface.after(32, self.update_game)       
        else:
            # disable les touches de mouvement du joueur
            self.interface.unbind("<Left>")
            self.interface.unbind("<Right>")
            self.interface.unbind("<KeyRelease-Left>")
            self.interface.unbind("<KeyRelease-Right>")
            self.interface.unbind("<space>")

    def gameover(self):
        """Affiche page de fin de partie."""
        self.loose = True
        self.jeu = False
        self.start_button.config(state="active")
        self.affichagetexte()

    def gamewin(self):
        """Affiche page de victoire."""
        self.win = True
        self.jeu = False
        self.start_button.config(state="active")
        self.affichagetexte()



# Lancer l'interface
interface = tk.Tk() 
game = Jeu(interface)
interface.mainloop()