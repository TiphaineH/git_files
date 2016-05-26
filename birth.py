# -*- coding: utf-8 -*-
"""
Created on August 2013
@author: Benoit MAILLOT
@author: Tiphaine HUET
"""


class OurFamily():
    def mother (self, mfn, mln):
        self.mfn = 'Tiphaine'
        self.mln = 'HUET'
        listMother = [mfn, mln]
        return (" ".join(listMother) + " is fine")
            
    def father (self, ffn, fln):
        self.ffn  = 'Benoit'
        self.fln = 'MAILLOT'
        listFather = [ffn, fln]
        #nobody care but
        return (" ".join(listFather) + " is fine too")
                 
    def daughter (self, dfn, dln, age):
        self.dfn = 'Hyaline Gwenaelle Alvinella'
        self.dln = 'MAILLOT'
        self.age = 6 #year old
        listDaugther = [dfn, dln]
        return (" ".join(listDaugther) + " is happy!")
    
    def newborn_name (self, sfn1, sfn2, sfn3, sln):
        # type(object) = boy
        self.sfn1 = 'Ewald'
        property(sfn1, doc='reciprocal space')
        self.sfn2 = 'Ulysse'
        property(sfn2, doc='homeric odysseus')
        self.sfn3 = 'Asterias'
        property(sfn3, doc='starfish echinoderm')
        self.sln = 'MAILLOT'
        listSon = [sfn1, sfn2, sfn3, sln]
        return (" ".join(listSon) + " is born and he's fine")
    
    def newborn_status(self, h, k, l):
        self.h = 'XX'
        self.k = 'YY'
        self.l = 'CHU'
        date = 'DD/MM/YYYY'
        listhkl = [h, k, l]
        listUnit = ['cm', 'kg', ' Montpellier']
        for hkl, Unit in zip(listhkl, listUnit):
            print (hkl + Unit)
            print (date)

# message end
# écrire les lignes suivantes pour faire tourner les fonctions

mother = (mother,'Tiphaine', 'HUET')
father = (father,'Benoit', 'MAILLOT')
daughter = (daughter,'Hyaline Gwenaelle Alvinella', 'MAILLOT',6)
newborn_name = (newborn_name,'Ewald','Ulysse','Asterias','MAILLOT')
newborn_status = (newborn_status,'XX','YY','CHU')


