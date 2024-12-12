# TP4-_-spaceinvider

Règle du jeu 

    Le but du jeu Space Invaders est de détruire des vagues d'aliens envahisseurs qui descendent progressivement vers le bas de l'écran, tout en évitant que ces aliens n'atteignent le bas de l'écran ou que le joueur ne soit touché par leurs projectiles. Le joueur contrôle un vaisseau spatial qui se déplace horizontalement en bas de l'écran et peut tirer des projectiles pour éliminer les aliens.

    - Commande :
        tirer -> espace
        ce déplacer -> flèche de droite/gauche
        pause -> échap


Le jeu est en programmation Orienté Objet, il fait donc appelé à plusieurs Classe :
    * Player permettant de : - Gérer l'affichage graphique du joueur
                             - Gérer les déplacement du joueur
                             - Gérer la mise à jour de la position du joueur en fonction de ces déplacements
    * Alien permettante de : - Représenter graphiquement les aliens
                             - Gérer le comportement collectif des aliens (déplacements)
                             - Gérer le changement de direction du groupe d'aliens une fois le bord atteind
    * Torpille permettant de : - Créer l'affichage graphique des tropilles
                               - Définir le mouvement des torpilles 
                               - Gérer les tirs du joueurs et des aliens
    * Jeu permettante de : - Créer l'environnement du jeu (fenêtre, inteface graphique)
                           - Démarrer et initialiser le jeu
                           - Gérer les déplacement et les interractions du joueur avec les aliens
                           - Gérer les collisions avec les torpilles 
                           - Mettre en pause et reprendre/quitter le jeu
                           - Afficher les information (nombre de vie, score et message)


Adresse du répertoire GIT : https://github.com/anaellerb1/Canda-Anaelle_SpaceInvider.git

Implémentation : 
 * Liste : 
    - Dans self.aliens : Liste qui contient tous les aliens du jeu.
    - Dans self.torpilles_joueur : Liste des torpilles tirées par le joueur.
    - Dans self.torpilles_alien : Liste des torpilles tirées par les aliens.
    - Dans self.ilots : Liste des îlots dans le jeu.
    - Dans affichagetexte() et pause_game() : Liste permettant de modifier les infomartion texte (score et vie)
* Pile :
    - Dans self.torpilles_joueur : Les torpilles sont retirés de la liste après avoir été déplacés ou lorsqu'elles touchent un objet
* File :
    - Dans self.torpilles_alien: Les premières torpilles créées sont les premières à disparaître lorsque l'écran est nettoyé ou lorsqu'elles sortent du cadre.
    - Dans is_collision : vérifie les collisions pour chaque objet dans les listes (aliens, torpilles, îlots) où chaque élément est traité dans l’ordre d’ajout.

