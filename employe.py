class Employe:

    def __init__(self,nom="",prenom="",salaire=2828.71):
        self.__nom = nom
        self.__prenom = prenom
        self.__salaire = salaire

    def setNom(self,nouveaunom):
        self.__nom=nouveaunom

    def setPrenom(self,nouveauprenom):
        self.__prenom=nouveauprenom

    def setSalaire(self,nouveausalaire):
        if (self.__salaire < nouveausalaire):
            self.__salaire = nouveausalaire

    def __str__(self):
        print("je m'appele" ,  self.__nom , self.__prenom , "je travaile en tant que employe")

    def comparerSalaire(self):
        self.S1 = int(input("entrer le premiere salaire"))
        self.S2 = int(input("entrer le douxieme salaire"))
        if (self.S1 > self.S2):
            print(self.S1 , 'est le grande salaire')
        elif (self.S1 < self.S2) :
            print(self.S2 , 'est le grande salaire')
        else :
            print("le deux salaire est equivalent")
    
    def creeEmploye(self):
        print("entrer les information de employe")
        self.__nom = input("entre le nom")
        self.__prenom = input("entre le prenom")
        self.__salaire = input("entre le salaire")
        if (self.__salaire == ""):
            self.__salaire = 2828.71

    def afficherEmploye(self):
        print("les information de employe")
        print("le nom : " , self.__nom)
        print("le prenom : " , self.__prenom)
        print("le salaire : " , self.__salaire)

e1=Employe()
e1.creeEmploye()
e2=Employe()
e2.creeEmploye()
e1.afficherEmploye()
e2.afficherEmploye()