#!/usr/bin/env python3
# coding = utf-8
class Fahrzeug:    
    Instanzen = 0   
    _Instanzen = 0
    
    def __init__(self, raeder):
        self.Raeder = raeder 
        Fahrzeug._Instanzen += 1 
        type(self).Instanzen += 1
        
    def __del__(self):        
        Fahrzeug._Instanzen -= 1 
        type(self).Instanzen -= 1

    def nenne_raeder(self):        
        trace(f"Das {self.class_name()} hat {self.Raeder} Räder.")
        
    def nenne_marke(self):                
        trace(f"Die Marke des {self.class_name()}s: {self.Marke}")
        
    @classmethod    
    def class_name(cls):
      return str(cls.__name__)        

    
class Fahrrad(Fahrzeug):
    def __init__(self, marke):
        Fahrzeug.__init__(self, 2)
        self.Marke=marke


class Auto(Fahrzeug):
    def __init__(self, marke):
        Fahrzeug.__init__(self, 4)
        self.Marke=marke

                
def trace(message):
    print(message)

### main ###
paulsFahrrad = Fahrrad("Cube")
paulsAuto = Auto("Golf")
karinsFahrrad = Fahrrad("Specialized")
karinsAuto = Auto("Mini")

print("--")
karinsFahrrad.nenne_marke()
karinsFahrrad.nenne_raeder()
karinsAuto.nenne_marke()
karinsAuto.nenne_raeder()
print("--")
paulsFahrrad.nenne_marke()
paulsFahrrad.nenne_raeder()
paulsAuto.nenne_marke()
paulsAuto.nenne_raeder()
print("--")
print("Anzahl der Autos: " + str(Auto.Instanzen))
print("Anzahl der Fahrräder: " + str(Fahrrad.Instanzen))
print("Anzahl der Fahrzeuge: " + str(Fahrzeug._Instanzen))
print("==")
