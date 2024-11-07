import tkinter as tk

class Jeu:
    def __init__(self, interface):
        self.interface = interface
        self.interface.title("Space Invider - Sanjay x Anaëlle")
        
        #canva de la page
        self.Canvas = tk.Canvas(interface, width=600, height=400, bg='black' )
        self.Canvas.pack(anchor=tk.CENTER, expand=True)

        #en-tete
        self.Canvas.create_text(
            (300,100),
            text = "Space Invider",
            fill = "yellow",
            font = 'arial'
        )

        #score / level / vies / highest score
        self.score = 0
        self.score_label = tk.Label(self.interface, text=f"Score: {self.score}", font=("Arial", 14), fg="black")
        self.score_label.pack()

        #Start / quit button
        start_button = tk.Button(self.interface, text="Démarrer", command=self.start_game)
        start_button.pack(side=tk.LEFT, padx=10)

        quit_button = tk.Button(self.interface, text="Quitter", command=self.interface.quit)
        quit_button.pack(side=tk.RIGHT, padx=10)

        #Menu 'option'
        menubar = tk.Menu(self.interface)
        self.interface.config(menu=menubar)

        game_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Options", menu=game_menu)
        game_menu.add_command(label="Recommencer", command=self.start_game)
        game_menu.add_separator()
        game_menu.add_command(label="Quitter", command=self.interface.quit)

        #Initialisation variables
        self.score = 0
        self.level = 0
        self.vies = 5


    def start_game(self):
        # Code pour démarrer la partie
        self.score = 0
        self.update_score()
        # initialisation alien, joueur etc
        self.Canvas.create_text(
            (300,150),
            text = "La partie commence !",
            fill = "white",
            font = 'arial'
        )
        pass

    def update_score(self):
        # Code pour update le score
        pass
    
         


# Lancer l'interface
interface = tk.Tk()
game = Jeu(interface)
interface.mainloop()







