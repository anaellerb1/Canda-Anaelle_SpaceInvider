import tkinter as tk
import random

# Configurer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Space Invaders")
fenetre.resizable(False, False)

# Dimensions de la fenêtre de jeu
LARGEUR = 600
HAUTEUR = 400

# Canvas pour dessiner les éléments du jeu
canvas = tk.Canvas(fenetre, width=LARGEUR, height=HAUTEUR, bg="black")
canvas.pack()

# Variables de joueur
joueur_x = LARGEUR // 2
joueur_y = HAUTEUR - 30
joueur_vitesse = 20
joueur = canvas.create_rectangle(joueur_x - 15, joueur_y - 10, joueur_x + 15, joueur_y + 10, fill="blue")

# Liste des projectiles du joueur 
projectiles = []
projectile_vitesse = 10

# Variables des ennemis
ennemis = []
ennemi_vitesse = 2
ennemi_direction = 1

# Fonction pour créer des ennemis
def creer_ennemis():
    for i in range(5):
        ennemi_x = 50 + i * 100
        ennemi_y = 50
        ennemi = canvas.create_rectangle(ennemi_x - 15, ennemi_y - 15, ennemi_x + 15, ennemi_y + 15, fill="red")
        ennemis.append(ennemi)

# Déplacement du joueur
def deplacer_joueur(event):
    global joueur_x
    if event.keysym == "Left" and joueur_x > 0:
        joueur_x -= joueur_vitesse
    elif event.keysym == "Right" and joueur_x < LARGEUR:
        joueur_x += joueur_vitesse
    canvas.coords(joueur, joueur_x - 15, joueur_y - 10, joueur_x + 15, joueur_y + 10)

# Tir de projectile
def tirer_projectile(event):
    projectile = canvas.create_oval(joueur_x - 5, joueur_y - 20, joueur_x + 5, joueur_y - 10, fill="yellow")
    projectiles.append(projectile)

# Déplacement des projectiles
def deplacer_projectiles():
    for projectile in projectiles[:]:
        canvas.move(projectile, 0, -projectile_vitesse)
        if canvas.coords(projectile)[1] < 0:
            canvas.delete(projectile)
            projectiles.remove(projectile)

# Déplacement des ennemis
def deplacer_ennemis():
    global ennemi_direction
    bord_atteint = False
    for ennemi in ennemis:
        x1, y1, x2, y2 = canvas.coords(ennemi)
        if x2 >= LARGEUR or x1 <= 0:
            ennemi_direction *= -1
            bord_atteint = True
            break
    for ennemi in ennemis:
        canvas.move(ennemi, ennemi_vitesse * ennemi_direction, 0)
        if bord_atteint:
            canvas.move(ennemi, 0, 20)

# Vérification des collisions
def verifier_collisions():
    for projectile in projectiles[:]:
        px1, py1, px2, py2 = canvas.coords(projectile)
        for ennemi in ennemis[:]:
            ex1, ey1, ex2, ey2 = canvas.coords(ennemi)
            # Vérifie si un projectile touche un ennemi
            if px1 < ex2 and px2 > ex1 and py1 < ey2 and py2 > ey1:
                canvas.delete(projectile)
                projectiles.remove(projectile)
                canvas.delete(ennemi)
                ennemis.remove(ennemi)
                break

# Boucle principale du jeu
def boucle_jeu():
    deplacer_projectiles()
    deplacer_ennemis()
    verifier_collisions()
    fenetre.after(50, boucle_jeu)

# Initialiser le jeu
creer_ennemis()
fenetre.bind("<Left>", deplacer_joueur)
fenetre.bind("<Right>", deplacer_joueur)
fenetre.bind("<space>", tirer_projectile)
boucle_jeu()

# Lancer la fenêtre Tkinter
fenetre.mainloop()
