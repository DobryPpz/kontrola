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
"kot": "gata"
}  	

if sys.argv[1] in thisdict.keys():
	print(thisdict[sys.argv[1]])
else: print("brak slowa w slowniku")
