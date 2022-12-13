import sys
 #44


thisdict =	{
"strona": "side",
"folder": "folder",
"klawiatura": "keyboard",
"żyrafa" : "giraffe",
"buk": "beech",
"komputer" : "computer",
"ściana" : "wall",
"dom" : "House",
"pies": "dog",
"kot": "cat",
"drzewo": "tree",
"koń": "horse",
"elektronika": "electronics",
"wspomnienie": "flashback",
"zapach": "smell",
"warstwa": "layer",
"terminal": "Terminal",
"samolot": "plane",
"suchy": "dry",
"mokry": "wet",
"kąt": "angle",
"zespół": "team",
"Niedźwiedź": "Bear",
"książki": "books",
"nagroda": "award",
"gulasz": "Goulash",
"zęby": "teeth",
"handel": "trade",
"gość": "guest",
"zoo": "zoo"


}  	


if sys.argv[1] in thisdict.keys():
	print(thisdict[sys.argv[1]])
else: print("brak slowa w slowniku")

