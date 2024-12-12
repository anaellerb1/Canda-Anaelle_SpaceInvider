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
        self.torpilles = [] 
        self.score = 0
        self.pause = False
        self.pause_text = []
        self.win = False
        self.win_text = []
        self.loose = False
        self.loose_text = []
    
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
            (self.LARGEUR / 2, self.HAUTEUR / 6),
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



    def setBinds(self):
        """Définit les touches du jeu."""
        interface.bind("<Left>", self.joueur.deplacer_gauche)
        interface.bind("<Right>", self.joueur.deplacer_droite)
        interface.bind("<KeyRelease-Left>", self.joueur.arreter_deplacement)
        interface.bind("<KeyRelease-Right>", self.joueur.arreter_deplacement)
        interface.bind("<space>", lambda event: Torpille.tirer(self.joueur.canvas, int(self.joueur.x), int(self.joueur.y), self.torpilles))
        interface.bind("<Escape>", self.pause_game)

    def center_window(self, width, height):
        """Centre la fenêtre sur l'écran."""
        screen_width = self.interface.winfo_screenwidth()
        x = (screen_width // 2) - (width // 2) 
        y = 0
        self.interface.geometry(f'{width}x{height}+{x}+{y}')

    def initialiser_jeu(self):
        """Initialise les variables du jeu."""
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
                alien = Alien(self.Canvas, int(x), int(y), self.LARGEUR)
                self.aliens.append(alien)

        self.joueur = Player(self.Canvas, self.LARGEUR, self.HAUTEUR, self.interface)
        self.setBinds()
        self.update_game()

    def pause_game(self, event=None):
        """Code pour mettre en pause la partie."""
        self.pause = not self.pause
        if self.pause:
            self.pause_text = self.affichagetexte()
            self.resume_button = tk.Button(self.interface, text="Reprendre", command=self.pause_game)
            self.Canvas.create_window(self.LARGEUR / 2, self.HAUTEUR / 2 + 10, window=self.resume_button)
            self.quit_button = tk.Button(self.interface, text="Quitter", command=self.interface.quit)
            self.Canvas.create_window(self.LARGEUR / 2, self.HAUTEUR / 2 + 50, window=self.quit_button)
        else:
            for item in self.pause_text:
                self.Canvas.delete(item)
            self.resume_button.destroy()
            self.quit_button.destroy()
            self.update_game()
            self.setBinds()

    def affichagetexte(self):
        """Affichage des textes du jeu."""
        if self.pause: #texte de pause
            pause_text = [
                self.Canvas.create_rectangle(0, self.HAUTEUR, self.LARGEUR, 0, fill="black", stipple="gray50"),
                self.Canvas.create_text(
                    (self.LARGEUR / 2, self.HAUTEUR / 3),
                    text="Pause",
                    fill="red",
                    font=('arial', 24, "bold")
                ),
                self.Canvas.create_text(
                    (self.LARGEUR / 2, self.HAUTEUR / 3 + 40),
                    text=f"Score: {self.score}",
                    fill="white",
                    font=('arial', 13, "italic")
            )]
            return pause_text
        if self.win:
            win_text = [
                self.Canvas.create_text(
                    (self.LARGEUR / 2, self.HAUTEUR / 2),
                    text="Victoire !",
                    fill="green",
                    font=('arial', 24, "bold")
                ),
                self.Canvas.create_text(
                    (self.LARGEUR / 2, self.HAUTEUR / 2 + 30),
                    text=f"Score: {self.score}",
                    fill="green",
                    font=('arial', 24, "bold")
                ),
                self.Canvas.create_text(
                    (self.LARGEUR / 2, self.HAUTEUR / 2 + 60),
                    text="Appuyez sur 'Démarrer' pour rejouer",
                    fill="green",
                    font=('arial', 24, "bold")
                )]
            return win_text
        if self.loose:
            loose_text = [
                self.Canvas.create_text(
                    (self.LARGEUR / 2, self.HAUTEUR / 2),
                    text="Game Over",
                    fill="red",
                    font=('arial', 24, "bold")
                ),
                self.Canvas.create_text(
                    (self.LARGEUR / 2, self.HAUTEUR / 2 + 30),
                    text=f"Score: {self.score}",
                    fill="red",
                    font=('arial', 24, "bold")
                ),
                self.Canvas.create_text(
                    (self.LARGEUR / 2, self.HAUTEUR / 2 + 60),
                    text="Appuyez sur 'Démarrer' pour rejouer",
                    fill="red",
                    font=('arial', 24, "bold")
                )]
            return loose_text

    def update_score(self):
        """Met à jour l'affichage du score."""
        self.score_label.config(text=f"Score: {self.score}")

    def deplacer_aliens(self):
        """Déplace tous les aliens à chaque intervalle."""
        if self.aliens:
            self.aliens[0].deplacer_aliens(self.aliens)
        
    def is_collision(self):
        """Vérifie les collisions entre les torpilles et les aliens."""
        for torpille in list(self.torpilles): 
            torpille_coords = self.Canvas.coords(torpille.id) 
            if not torpille_coords:
                continue  
            if self.aliens == []:
                self.gamewin()
                break
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
                    self.torpilles.remove(torpille)
                    
                    # Mettre à jour le score
                    self.score += 1
                    self.update_score()
                    break

                # Vérifier si les aliens atteignent le bas de l'écran // MARCHE PAS !!!!!!!!
                if alien_coords[3] >= (self.HAUTEUR-20):
                    self.gameover()
                    break

    def update_game(self):
        """Mise à jour de l'état du jeu."""
        # Déplacer les aliens
        self.deplacer_aliens()
            
        # Déplacer les torpilles
        for torpille in list(self.torpilles): 
            torpille.deplacer(self.torpilles)
        
        # Vérifier les collisions
        self.is_collision()

        if not self.pause:
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
        self.affichagetexte()

    def gamewin(self):
        """Affiche page de victoire."""
        self.win = True
        self.affichagetexte()



# Lancer l'interface
interface = tk.Tk() 
game = Jeu(interface)
interface.mainloop()