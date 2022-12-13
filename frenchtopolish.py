import sys


#hui
thisdict =	{
"côté":"strona",
"dossier":"folder",
"clavier":"klawiatura",
"girafe":"żyrafa",
"hêtre":"buk",
"l'ordinateur":"komputer",
"mur":"ściana",
"loger":"dom",
"chien":"pies",
"chat":"kot",
"arbre":"drzewo",
"cheval": "koń",
"électronique":"elektronika",
"Retour en arrière":"wspomnienie",
"sentir": "zapach",
"couche": "warstwa",
"terminal": "terminal",
"avion": "samolot",
"sec":"suchy",
"humide":"mokry",
"angle": "kąt",
"équipe": "zespół",
"ours": "niedźwiedź",
"livres": "książki",
"décerner": "nagroda",
"Goulache": "gulasz",
"les dents": "zęby",
"Commerce": "handel",
"invité": "gość",
"zoo": "zoo",
"auto": "samochód",
"machine": "maszyna",
"câble": "kabel",
"piano": "fortepian",
"violoncelle": "wiolonczela",
"violon": "skrzypce",
"guitare": "gitara",
"couple": "para",
"gecko": "gekon",
"moniteur": "waran"
}  	

if sys.argv[1] in thisdict.keys():
	print(thisdict[sys.argv[1]])
else: print("brak slowa w slowniku")