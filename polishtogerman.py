import sys


#hui
thisdict =	{
"strona":"seite",
"folder":"mappe",
"klawiatura":"klaviatur",
"żyrafa":"giraffe",
"buk":"buche",
"komputer":"computer",
"ściana":"mauer",
"dom":"haus",
"pies":"hund",
"kot":"katze",
"drzewo":"baum",
"koń": "pferd",
"elektronika":"elektronik",
"wspomnienie":"Rückblende",
"zapach": "geruch",
"warstwa": "schicht",
"terminal": "terminal",
"samolot": "Flugzeug",
"suchy":"trocken",
"mokry":"nass",
"kąt": "winkel",
"zespół": "Mannschaft",
"niedźwiedź": "tragen",
"książki": "Bücher",
"nagroda": "vergeben",
"gulasz": "gulasch",
"zęby": "Zähne",
"handel": "handeln",
"gość": "gast",
"zoo": "zoo"
}  	

if sys.argv[1] in thisdict.keys():
	print(thisdict[sys.argv[1]])
else: print("brak slowa w slowniku")