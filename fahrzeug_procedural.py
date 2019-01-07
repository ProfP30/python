#!/usr/bin/env python3
anz_autos = 0
anz_fahrraeder = 0
anz_fahrzeuge = 0

def add_fahrzeug(typ, marke, raeder):
    global anz_fahrzeuge
    anz_fahrzeuge += 1
    if typ == "Fahrrad":
        global anz_fahrraeder
        anz_fahrraeder += 1
    if typ == "Auto":
        global anz_autos
        anz_autos += 1
    fahrzeug={'Typ': typ, 
         'Marke': marke, 
         'Räder': raeder}    
    return fahrzeug

def nenne_raeder(fahrzeug):        
    trace(f"Das {fahrzeug['Typ']} hat {fahrzeug['Räder']} Räder.")
        
def nenne_marke(fahrzeug):      
    trace(f"Die Marke des {fahrzeug['Typ']}s: {fahrzeug['Marke']}")
    
def trace(message):
    print(message)

### main ###
paulsFahrrad = add_fahrzeug("Fahrrad", "Cube", 2)
paulsAuto = add_fahrzeug("Auto", "Golf", 4)
karinsFahrrad = add_fahrzeug("Fahrrad", "Specialized", 2)
karinsAuto = add_fahrzeug("Auto", "Mini", 4)

print("--")
nenne_marke(karinsFahrrad)
nenne_raeder(karinsFahrrad)
nenne_marke(karinsAuto)
nenne_raeder(karinsAuto)
print("--")
nenne_marke(paulsFahrrad)
nenne_raeder(paulsFahrrad)
nenne_marke(paulsAuto)
nenne_raeder(paulsAuto)
print("--")
print("Anzahl der Autos: " + str(anz_autos))
print("Anzahl der Fahrräder: " + str(anz_fahrraeder))
print("Anzahl der Fahrzeuge: " + str(anz_fahrzeuge))
print("==")
