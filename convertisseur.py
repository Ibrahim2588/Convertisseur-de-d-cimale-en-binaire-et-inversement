#coding:utf-8

#coding:utf-8
#!/bin/python3

#--------------------------------------------------------

"""
FONCTION DE CALCULE
"""

#CONVERTION DU DECIMALE AU BINAIRE
def du_decimale_au_binaire(x):
	resultat = ""
	x = int(x)
	for i in range(15):	
		h = str(x%2)
		if x == 1 or x == 0:
			resultat = h + resultat
			break
		x = int(x/2)
		resultat = h + resultat
	return resultat

#CONVERTION DU BINAIRE AU DECIMALE
def du_binaire_au_decimale(x):
	x = int(x)
	x = str(x)
	dcount = len(x)
	count = len(x)
	resultat = 0
	i = 0
	while i < dcount:
		valeur = x[i]
		valeur = int(valeur)
		resultat += (valeur * puissance(2, count-1))
		count -= 1
		i += 1
	return resultat

#CALCULE LA PUISSANCE D'UN NOMBRE
def puissance(nombres, puissancex):
	i = 0
	if puissancex == 0:
		return 1
	if puissancex == 1:
		return nombres
	while i < (puissancex-1):
		nombres += nombres
		i += 1
	return nombres
  
#--------------------------------------------------------


from tkinter import *

#fonction de recuperation de variables
def get_decimal(*args):
	resultat_binaire.set(du_decimale_au_binaire(var_entrer_decimale.get()))
def get_binary(*args):
	resultat_decimal.set(du_binaire_au_decimale(var_entrer_binaire.get()))

#initialisation de la fenetre
window = Tk()
window.minsize(310, 130)
window.maxsize(300, 130)
window.title("Convertion binaire")

cadre = Frame(window, background="gray")

#Widget label de fenetre
binaire1 = Label(cadre, text="BINAIRE :", background="gray")
binaire2 = Label(cadre, text="BINAIRE :", background="gray")

decimal1 = Label(cadre, text="Decimale :", background="gray")
decimal2 = Label(cadre, text="Decimale :", background="gray")

binaire = Label(cadre, text="Convertire en binaire", background="gray")
decimal = Label(cadre, text="Convertire en decimal", background="gray")

#variable entrer par l'utilisateur
var_entrer_binaire = IntVar()
var_entrer_decimale = IntVar()

#variable resultats
resultat_binaire = IntVar()
resultat_decimal = IntVar()

#Capture des entrer utilisateur
var_entrer_decimale.trace("w", get_decimal)
var_entrer_binaire.trace("w",get_binary)

#Widget de variable enter par utilisateur
entrer_decimal = Entry(cadre, textvariable=var_entrer_decimale, background="gray")
entrer_binaire = Entry(cadre, textvariable=var_entrer_binaire, background="gray")

#Widget de sortie des résultats
sotie_binaire = Label(cadre, textvariable=resultat_binaire, background="gray")
sotie_decimal = Label(cadre, textvariable=resultat_decimal, background="gray")

#Affichage des widget
binaire.grid(row=0, column=0)
decimal1.grid(row=1, column=0)
binaire1.grid(row=2, column=0)

decimal.grid(row=4, column=0)
binaire2.grid(row=5, column=0)
decimal2.grid(row=6, column=0)

entrer_decimal.grid(row=1, column=1)
entrer_binaire.grid(row=5, column=1)

sotie_binaire.grid(row=2, column=1)
sotie_decimal.grid(row=6, column=1)

cadre.grid()

window.mainloop()
