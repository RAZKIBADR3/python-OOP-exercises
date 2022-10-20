from datetime import date

class Article():
    def __init__(self,num="0",prixHT=0,qtStock=0,qtMini=0):
        self.num = num
        self.prixHT = prixHT
        self.qtStock = qtStock
        self.qtMini = qtMini

    def str(self):
        print("le numero de serie est:" , self.num)
        print("le prix hors taxe est:" , self.prixHT)
        print("le quantite en stock est:" , self.qtStock)
        print("le quantite minimale est:" , self.qtMini)

    def achat(self,qte):
        self.qte = qte
        if (self.qte <= self.qtStock - self.qtMini):
            self.qtStock = self.qtStock - self.qte
            print("Achat terminé")
        else:
            print("Achat n'a pas terminé ,la quantité qui reste est inférieure à la quantité minimale")

class Habit(Article):
    def __init__(self,num="0",prixHT=0,qtStock=0,qtMini=0,taille="XL",couleur="rouge"):
        self.num = num
        self.prixHT = prixHT
        self.qtStock = qtStock
        self.qtMini = qtMini
        self.taille = taille
        self.couleur = couleur

    def str(self):
        print("le numero de serie est:" , self.num)
        print("le prix hors taxe est:" , self.prixHT)
        print("le quantite en stock est:" , self.qtStock)
        print("le quantite minimale est:" , self.qtMini)
        print("la taille de habit est: " , self.taille)
        print("la couleur de habit est: " , self.couleur)

class Electromenager(Article):
    def __init__(self,num="0",prixHT=0,qtStock=0,qtMini=0,poid="1kg",garantie=1):
        self.num = num
        self.prixHT = prixHT
        self.qtStock = qtStock
        self.qtMini = qtMini
        self.poid = poid
        self.garantie = garantie

    def datefinGarantie(self):
        month = 5 + self.garantie
        D = date(2022,month,11)
        datefinGarantie = str(D.year) + "\\" + str(D.month) + "\\" + str(D.day)
        return datefinGarantie

    def str(self):
        print("le numero de serie est:" , self.num)
        print("le prix hors taxe est:" , self.prixHT)
        print("le quantite en stock est:" , self.qtStock)
        print("le quantite minimale est:" , self.qtMini)
        print("la poid de electromenager est: " , self.poid)
        x = self.datefinGarantie()
        print("la date de fin de garantie est: " , x)


habit = Habit("1",200,20,4,"XL","rouge")
habit.str()
electromenager = Electromenager("2",150,20,3,"5kg",3)
electromenager.achat(10)
x = electromenager.datefinGarantie()
print("la date de fin de garantie est: " , x)
electromenager.str()