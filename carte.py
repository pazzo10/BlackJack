class Carte:
    def __init__(self):
        self.couleur = ["carreau", "pique", "coeur", "trefle"]
        self.paquet = []
        self.generate_deck()

    def generate_deck(self):
        for couleur in  self.couleur:
            for num in range(1,14):
                self.paquet.append((num, couleur))

    
    def print_deck(self):
        for f in self.paquet:
            if f[0] == 1:
                print("as", f[1])
            elif f[0] == 11:
                print("valet",f[1])
            elif f[0] == 12:
                print("reine",f[1])
            elif f[0] == 13:
                print("roi",f[1])
            else:
                print(f)





if __name__ == "__main__":
    lesCartes = Carte()
    lesCartes.print_deck()