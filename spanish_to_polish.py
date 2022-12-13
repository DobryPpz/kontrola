import sys
 #44


thisdict =	{
"strona": "lado",
"folder": "carpeta",
"klawiatura": "teclado",
"żyrafa" : "jirafa",
"buk": "haya",
"komputer" : "computadora",
"ściana" : "pared",
"dom" : "Casa",
"pies": "perro",
"kot": "gata",
"drzewo": "árbol",
"koń": "caballo",
"elektronika": "electrónica",
"wspomnienie": "Escena retrospectiva",
"zapach": "oler",
"warstwa": "capa",
"terminal": "Terminal",
"samolot": "plano",
"suchy": "seco",
"mokry": "mojado"
"lotnisko": "aeropuerto",
"łopata": "pala",
"krok": "paso",
"czołg": "tanque",
"ślad": "rastro
"bogactwo": "riqueza",
"dzwon": "campana",
"ptak": "pájaro",
"prąd": "electricidad",
"olej": "Aceite"
}

if sys.argv[1] in thisdict.keys():
	print(thisdict[sys.argv[1]])
else: print("brak slowa w slowniku")


