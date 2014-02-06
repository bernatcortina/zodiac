# -*- coding: utf-8 -*-

import random
from models import *


def my_view(request):
    return {'project':'zodiac'}

def zodiac_view(request):
    return { "projecte":"Signes del zodiac",
		"imatges": ["Capricorn.png","Aquarius.png","Pisces.png","Aries.png","Taurus.png","Gemini.png","Cancer.png",
    	"Leo.png","Virgo.png","Libra.png","Scorpio.png","Sagittarius.png"]
    }

def entra_dades_view(request):
	if request.method=="POST":
		nom = request.POST.get("nom")
		dia_naix = request.POST.get("dia_naix")
		mes_naix = request.POST.get("mes_naix")


		missatge = ["El fracàs és part de la vida; si no fracasses, no aprens i si no aprens, no canvies.",
			"L'èxit és aprendre a anar de fracàs en fracàs sense perdre l'entusiasme.",
			"El que és impossible només triga una mica més.",
			"Si lluites pots perdre, si no lluites estàs perdut. L'única lluita que es perd és la que s'abandona.",
			"Mai deixis que un mal dia  et faci sentir com si tinguessis una mala vida.",
			"Vols alguna cosa? Llavors ves i fes que passi. Perquè l'únic que cau del cel és la pluja.",
			"Per assolir una cosa que mai has tingut, hauràs de fer alguna cosa que mai has fet.",
			"Caure està permès. Aixecar-se és obligatori!"]

		imatges = ["Capricorn.png","Aquarius.png","Pisces.png","Aries.png","Taurus.png","Gemini.png","Cancer.png",
    	    "Leo.png","Virgo.png","Libra.png","Scorpio.png","Sagittarius.png"]

		num = random.randint(0,7)

		signe = ("Capricorn","Aquari","Peixos","Àries","Taure","Bessons","Càncer","Lleó","Verge","Balança","Escorpí","Sagitari")
		data = (20,18,20,20,21,21,22,23,23,23,22,21)

		mes_naix = int(mes_naix)
		dia_naix = int(dia_naix)
		mes_naix = mes_naix-1

		if dia_naix > data[mes_naix]:
			mes_naix=mes_naix+1
		if mes_naix==12:
			mes_naix=0

		return { "projecte": "Signes del zodiac",
			"nom": nom,
			"signe": signe[mes_naix].decode('utf-8'),
			"missatge": missatge[num].decode('utf-8'),
			"imatge": imatges[mes_naix]

		}
	return { "projecte": "Signes del zodiac" }

def guess_book_view(request):
	
	return { "projecte": "LLibre de visites" }






