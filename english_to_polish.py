import sys


#hui
thisdict =	{
"page":"strona",
"folder":"folder",
"keyboard":"klawiatura",
"giraffe":"żyrafa",
"beech":"buk",
"computer":"komputer",
"wall":"ściana",
"house":"dom",
"dog":"pies",
"cat":"kot"
}  	

if sys.argv[1] in thisdict.keys():
	print(thisdict[sys.argv[1]])
else: print("brak slowa w slowniku")
