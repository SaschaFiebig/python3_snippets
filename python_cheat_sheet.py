


#### data types (datentypen) 
#===========================
# boolean (wahr/falsch)
b_wahrer_boolean = True
b_falscher_boolean = False

# integer (ganze nummer)
i_ganze_nummer = 42

# float   (kommerzahl)
f_kommer_zahl = 3.1415

# string  (wort, satz ect)
s_bacon = 'Bacon ist unser freund'

# list (sammlung von datentypen)
l_meine_liste = [1, True, 3.1415, 'Hello']

# tuple (sammlung von datentypen, ohne index)
t_meine_tuple = (1, False, 3.1415, 'Bye');

# dictionary (sammlung von datentypen mit schlüssel/wert paaren)
d_mein_dictionary = {
    'serie': 'Mr. Robot',
    'film': 'Star Wars',
    'buch': 'Herr der Ringe',
    'song': 'The best is yet to come'
}


#### control flow (fluss kontrolle/steuerung)
#============================================
# if/else (wenn/dann)
if 5 > 3:
    print('Fünf ist größer als drei')
elif 3 > 5:
    print('Drei ist größer als fünf')
else:
    print('Nichts von beiden trifft zu')


#### loops (schleifen)
#========================
# while loops 
while i_ganze_nummer > 30:
    if i_ganze_nummer == 40:
        i_ganze_nummer -= 1
        continue  # überspringe wenn 40
    print(i_ganze_nummer)
    i_ganze_nummer -= 1 
    if i_ganze_nummer == 33:
        break  # beende loop wenn 33

# for loops
for item in l_meine_liste:
    print(item) 

for number in range(5):
    print('bacon')

#### functions (funktionen)
#==========================
# math 
# 


#### classes and objects (klassen und objekte)
#=============================================


# virtual environments (virtuelle umgebungen)
#============================================

#### packages & modules (packete und module) 
#===========================================
# pip 
# anaconda 

#### INPUT/OUTPUT (eingabe/ausgabe)
#==================================
# user I/O (nutzer)
# file I/O (datai)

#### error handling (fehler behandlung)
#======================================

