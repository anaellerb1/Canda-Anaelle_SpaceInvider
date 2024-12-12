"""
Anaëlle ROBIN  & Sanjay CANDA 3ETI
02/12/2024
Fichier de lancement du jeu
"""

from main import Jeu 
import tkinter as tk

# Lancer l'interface
interface = tk.Tk() 
game = Jeu(interface)
interface.mainloop()