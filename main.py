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
from Torpille import Torpille

class Jeu:
    def __init__(self, interface):
        # Initialisation des variables
        self.aliens = []  
        self.score = 0
        

        self.interface = interface
        self.interface.title("Space Invader - Sanjay x Anaëlle")

        # Fenêtre
        self.HAUTEUR = self.interface.winfo_screenheight() - 100  # Ajuster la hauteur pour laisser de la place en bas
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
    
    def deplacer_torpilles(self):
         """Déplacement de la torpille vers le haut."""
         Torpille.torpilles.y -=  Torpille.torpilles.vitesse  # Déplacer la torpille vers le haut
    
        # Met à jour la position de la torpille
        Torpille.torpilles.canvas.coords( Torpille.torpilles.id,  Torpille.torpilles.x - 2,  Torpille.torpilles.y - 20,
                                           Torpille.torpilles.x + 2,  Torpille.torpilles.y - 30)

        for torpille in Torpille.torpilles:
            
             # Si la torpille sort de l'écran, la supprimer
        if torpille.y < 0:
            Torpille.torpilles.canvas.delete(Torpille.torpilles.id)
            Torpille.torpilles.remove(torpille)  # Retirer la torpille de la liste
        else:
            # Relancer le déplacement de la torpille
            torpille.canvas.after(20, Torpille.torpilles.deplacer)
            alien_detecte = torpille.detecter_collision(Torpille.torpilles.aliens)
            if alien_detecte:
                Torpille.torpilles.score += 1
                Torpille.torpilles.update_score()
                Torpille.torpilles.aliens.remove(alien_detecte)
                Torpille.torpilles.Canvas.delete(alien_detecte.id)
                Torpille.torpilles.Canvas.delete(torpille.id)
                Torpille.torpilles.remove(torpille)
                break
            
            
        Torpille.torpilles.interface.after(50, Torpille.torpilles.deplacer_torpilles)  # Appelle cette méthode toutes les 50 ms


    


# Lancer l'interface
interface = tk.Tk() 
game = Jeu(interface)
interface.mainloop()