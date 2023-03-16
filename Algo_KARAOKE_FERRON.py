class Joueur:
    
    def __init__(self,pseudo,score,):

        self.nomJoueur = pseudo
        self.scoreJoueur = score
        


    def choixPseudo(self,pseudo):
        print("Bienvenue dans ce Karaoké.")
        pseudo = int(input("Quel est ton pseudo ?"))

    def choixChanson(self,chanson):
        
        self.chanson = chanson
        
        print("Choissisez une chanson à chanter")
        if self.chanson == 1 :
            print("Vous avez choisi la chanson 1")
        elif self.chanson == 2 :
            print("Vous avez choisit la 2ème chanson")
        elif self.chanson == 3 :
            print("Vous avez choisit la 3ème chanson")
        elif self.chanson == 4 :
            print("Vous avez choisit la 4ème chanson")
        elif self.chanson == 5 :
            print("Vous avez choisit la 5ème chanson")
    





class Karaoké:
    
    def __init__(self,musique,player):
        self.musique = musique
            

