class Element:
    
    def __init__(self,name):
        self.name = name
    
    def __str__(self):
        return self.name
        
    def __repr__(self):
        return self.__str__()
        

def sortAscending(listOfElements):
    for i in range(len(listOfElements)):
        for j in range(len(listOfElements)-1):
            if listOfElements[j].name > listOfElements[j+1].name:
                temp = listOfElements[j] 
                listOfElements[j] = listOfElements[j+1] 
                listOfElements[j+1] = temp 
                
    return listOfElements
    
def sortDescending(listOfElements):
    for i in range(len(listOfElements)):
        for j in range(len(listOfElements)-1):
            if listOfElements[j].name < listOfElements[j+1].name:
                temp = listOfElements[j] 
                listOfElements[j] = listOfElements[j+1] 
                listOfElements[j+1] = temp 
                
    return listOfElements

listOfNames = ['cyprian','eryk','adam','damian','bartosz','tomasz','maciej','krzysztof','marcin','michal','piotr','pawel','dawid','lukasz','mariusz','igor','wiktor','jerzy','waldemar','stanislaw','filip','konrad','mateusz','jaroslaw','slawomir']

listOfElements = []
for x in listOfNames:
    listOfElements.append(Element(x))
    
    
    
print(sortDescending(listOfElements))