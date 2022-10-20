class voiture():
    x = 0
    i = 0
    T = []
    def __init__(self,a="x-a-b",b="BMW",c="commerce"):
        self.matricule = a
        self.marque = b
        self.type = c

    def afficher(self):
        while(voiture().i<=len(voiture().T)):
            print("la matricule est" , voiture().T[voiture().i])
            voiture().i+=1
            print("la marque est" , voiture().T[voiture().i] )
            voiture().i+=1
            print("le type est" , voiture().T[voiture().i] )
            voiture().i+=1
        print("le nombre de voitures cree est" , voiture.x)

    def creeVoiture(self):
        voiture.x+=1
        print("cree le voiture nombre" , voiture.x)
        self.matricule = input("entrer le matricule\n")
        self.marque = input("entrer la marque\n")
        self.type = input("entrer le type : tourisme ou comerce\n")
        voiture().T.append(self.matricule)
        voiture().T.append(self.marque)
        voiture().T.append(self.type)


v1 = voiture()
v1.creeVoiture()
v1.creeVoiture()
voiture().afficher()