class Element:
    
    def __init__(self,name):
        self.name = name
    
    def __str__(self):
        return self.name+" "
        
    def __repr__(self):
        return self.__str__()
    

listOfElements = []
for x in ['cyprian','eryk','adam','damian','bartosz']:
    listOfElements.append(Element(x))
    
print(listOfElements)