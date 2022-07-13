#Auteur: Mohamad Jaber
choix=" "
p_dict={}
p_ID=[]
boeuf=0.0
viande=0.0
croquettes=0.0
poulet=0.0
saumon=0.0
poisson=0.0
quantité=0
nom=""
IDnbr=[]
total=0.0
reponse=""
prix=0.0
TPS=0.05
TVQ=0.10

from random import*


class eatbot3(object):
    
    
    
    def commanderAvecOnlineEatbot(p_dict:dict)->dict:
        p_dict={}
        choix=" "
        reponse = input("Bienvenue, l'assistant virtuel est la pour vouz aider:")
        reponse=reponse.lower()
        reponse=reponse.capitalize()
        while reponse!="au revoir":
            for key, value in dict.items():
                for elem in reponse.split():
                    if elem in key :
                        p_dict[key]=reponse
                        reponse= input( value)
                        if elem=="menu":
                            print(eatbot3.menu())
                            reponse= input( value)
                        elif elem=="iD":
                            print(selection_ID.Id(p_ID))
                            reponse= input( value)
                        elif elem=="prix":
                            print(eatbot3.menu())
                            reponse= input( value)
                        for elem_reponse in reponse.split():
                            if elem_reponse=="menu":
                                print(eatbot3.menu())
                                reponse= input( value)
                            elif elem_reponse=="iD":
                                print(selection_ID.Id(p_ID))
                                reponse= input( value)
                            elif elem_reponse=="prix":
                                print(eatbot3.menu())
                                reponse= input( value)
                    if "boeuf" == elem or (elem in value):
                       choix="boeuf" or "viande"
                       p_dict[key]=choix
                    elif "croquettes" == elem or (elem in value):
                        choix="croquettes" or "poulet"
                        p_dict[key]=choix
                    elif "saumon"== elem or (elem in value):
                        choix = "saumon" or "poisson"
                        p_dict[key]=choix
                   
            return choix
    
    
    def menu()->str:
        print("\t[boeuf] 15$")
        print("\t[croquettes] 10$")
        print("\t[saumon] 20$")


class selection_ID(object):
    
    
    def Id(p_ID:list)->list:
        if True:
            p_ID=[]
            IDnbr=[]
            nom= input("Quel est votre nom?:")
            p_ID.append(nom)
            p_ID.append(quantité)
            p_ID.append(prix)
            p_ID.append(total)
            Id=randint(0, 10000)
            IDnbr+=[Id]
            p_ID.append(IDnbr)
            p_ID.append(choix)
                
        return p_ID
        


#Main function
dict = {"Bonjour!": "Bonjour, comment puis-je vous aider? :", "Allo!":  "Allo, comment puis-je vous aider? :", "Je veux manger.":  "Oui, veuillez saisir le mot «Menu». :", "Est-il possible de commander?": "Oui, veuillez saisir le mot «Menu». :", "le menu svp?": "Veuillez saisir le mot «Menu». :", " J'aimerai savoir si ma commande est prete SVP." : "Oui, puis-je vous demander votre ID de commande"}
while True:
    choix=eatbot3.commanderAvecOnlineEatbot(dict)
    if choix == ("boeuf" or "viande"):
        boeuf=15.00
        quantité=int(input("saisir les quantités:"))
        prix=boeuf*quantité
        total=prix + (prix*(TPS+TVQ))
        print(selection_ID.Id(p_ID))
    elif choix==("croquettes" or "poulet"):
        croquettes=10.00
        quantité=int(input("saisir les quantités:"))
        prix=croquettes*quantité
        total=prix + (prix*(TPS+TVQ))
        print(selection_ID.Id(p_ID))
    elif choix==("saumon" or "poisson"):
        saumon=20.00
        quantité=int(input("saisir les quantités:"))
        prix=saumon*quantité
        total=prix + (prix*(TPS+TVQ))
        print(selection_ID.Id(p_ID))
    elif choix=="ID":
        print(selection_ID.Id(p_ID))
    else:
        break
        
print("Merci d'avoir commander avec le eatbot. Au revoir.")
