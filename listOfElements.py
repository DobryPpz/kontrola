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

def removeEveryThird(listOfElements):
    newListOfElements = []
    for x in range(len(listOfElements)):
        if x%3 == 2:
            continue
        newListOfElements.append(listOfElements[x])
    return newListOfElements
    
listOfNames = ['cyprian','eryk','adam','damian','bartosz','tomasz','maciej','krzysztof','marcin','michal','piotr','pawel','dawid','lukasz','mariusz','igor','wiktor','jerzy','waldemar','stanislaw','filip','konrad','mateusz','jaroslaw','slawomir','zbigniew', 'radosław','sebastian', 'szymon', 'karol','artur','arkadiusz','przemysław','robert','andrzej']

listOfElements = []
for x in listOfNames:
    listOfElements.append(Element(x))
    
    
print(sortAscending(listOfElements))
listOfElements = removeEveryThird(sortAscending(listOfElements))
print(listOfElements)

listOfNames2 = ['janusz','marek','zofia','zuzanna','ada','katarzyna','barbara','kinga','karolina','erytrytol']
for x in listOfNames2:
    listOfElements.append(Element(x))
    
print(sortAscending(listOfElements))