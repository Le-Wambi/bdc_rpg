from Personnage import Personnage
# Exemple d'utilisation de joueur de la classe Personnage
jour1 = Personnage("Aragorn", "Guerrier", 10, 100, 15, 5)
jour2 = Personnage("Gandalf", "Magicien", 10, 80, 5, 15)

jour1.afficher_info()
jour2.afficher_info()

jour1.attaquer(jour2)
jour2.afficher_info()