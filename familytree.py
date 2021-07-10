#!/usr/bin/env python3

testData = (
    # Dictionaries were stored in list instead of set as Python doesn't allow dictionaries in sets
    [
        {"Name": 'Alice', "Father": "Arlo", "Mother": "Madeline", "Children": []},
        {"Name": 'Bob', "Father": "Charlie", "Mother": "Eve", "Children": []},
        {"Name": 'Eve', "Father": "Oliver", "Mother": "Aurora", "Children": ['Bob']},
        {"Name": 'Charlie', "Father": "Jack", "Mother": "Luna", "Children": ['Bob']},
        {"Name": 'Madeline', "Father": "Jack", "Mother": "Aurora", "Children": ['Alice']},
        {"Name": 'Arlo', "Father": "Oscar", "Mother": "Isla", "Children": ['Alice']},
        {"Name": 'Oliver', "Father": "Hugo", "Mother": "Rose", "Children": ['Eve']},
        {"Name": 'Luna', "Father": "Oscar", "Mother": "Isla", "Children": ['Charlie']},
        {"Name": 'Aurora', "Father": "Hugo", "Mother": "Rose", "Children": ['Eve', 'Madeline']},
        {"Name": 'Jack', "Father": "Oscar", "Mother": "Rose", "Children": ['Charlie', 'Madeline']},
        {"Name": 'Hugo', "Father": "Unknown", "Mother": "Unknown", "Children": ['Oliver', 'Aurora']},
        {"Name": 'Rose', "Father": "Unknown", "Mother": "Unknown", "Children": ['Oliver', 'Aurora', 'Jack']},
        {"Name": 'Isla', "Father": "Unknown", "Mother": "Unknown", "Children": ['Luna', 'Arlo']},
        {"Name": 'Oscar', "Father": "Unknown", "Mother": "Unknown", "Children": ['Luna', 'Jack', 'Arlo']}
    ],
    "Bob"
)

# Helper function to format card data to be usable
def formatCardData(testData):
    useableData = {}
    useableData = set()

    for card in testData[0]:
        for key, value in card.items():
            if (value != "Unknown"):
                if (key == "Mother" or key == "Father"):
                    useableData.add((card['Name'], value))

    # Data will be formated like ({('Bob', 'Charlie'), ('Bob', 'Eve'),...}, 'Bob')
    formattedData = (useableData, testData[1])

    return formattedData;

# vertices connected by an edge from S.
def NS_out(V, E, S):
    return { v for v in V for u in S if (u,v) in E }

# vertices connected by an edge to u
def N_in(V, E, u):
   return { v for v in V if (v,u) in E }

# get a single element of a set. Don't care which
def arbitraryElement(S):
    return next(iter(S))

def distanceClassesP(V, E, u):
    V0 = V              # V_0 = V
    D = [ {u} ]         # D[0] = D_0 = {u}
    parent = { u: False }
    return distanceClassesPR(V0, E, D, parent)

def distanceClassesPR(V, E, D, parent):
    Vnew = V - D[-1]                          # V_{j} = V_{j-1} / D_{j-1}
    if len(Vnew) == 0: 
        return D, parent                      # All done?
    Dnew = D + [ NS_out(Vnew, E, D[-1]) ]     # D_{j} = N_{V_j}(D_{j-1})
    if len(Dnew[-1]) == 0: return D, parent   # No more neighbours, graph is disconnected
    for v in Dnew[-1]:
      parent[v] = arbitraryElement(N_in(D[-1], E, v))
    return distanceClassesPR(Vnew, E, Dnew, parent)

def solve(instance):
    (L, s) = instance
    V = { u for (u,v) in L } | { v for (u,v) in L }
    E = L | { (v,u) for (u,v) in L }
    newCards = []

    D = distanceClassesP(V, E, testData[1])

    for person in V:
        personCard = getCard(person)
        for key, value in D[1].items():
            if key == personCard['Name']:
                # If person your searching for is the key, update value card
                if value != False:
                    cardToChange = getCard(value)
                    newCard = addStarTo(cardToChange, key)
                    if newCard not in newCards:
                        newCards.append(newCard)
            elif value == personCard['Name']:
                # If person your searching for is value, update the key card
                cardToChange = getCard(key)
                newCard = addStarTo(cardToChange, value)
                if newCard not in newCards:
                    newCards.append(newCard)
    return newCards

# Helper function that gets dictionary of a person
def getCard(name):
    for card in testData[0]:
        if(card['Name'] == name):
            return card

# Helper function that returns card with star
def addStarTo(card, name):
    resultCard = card
    if (name in card.values()):
        # Name to be changed must be Father or Mother
        for key, value in card.items():
            if (value == name and name != testData[1]):
                resultCard[key] = "*" + name
    else:
        # If not in cards.values(), Name to be changed must be in Children array
        newChildArray = card.get('Children')
        if newChildArray:
            for i in range(len(newChildArray)):
                if (newChildArray[i] == name):
                    newChildArray[i] = "*" + name
            resultCard['Children'] = newChildArray
    return resultCard
    
def printSolution(solution):
    newCards = solution
    print("Updated Family Tree Cards:")
    print("--------------------")
    for card in newCards:
        for key, value in card.items():
            if key == "Children":
                print(f"{key}: ", end="")
                print(*value)
            else:
                print (f"{key}: {value}")
        print("--------------------------")
        
printSolution(solve(formatCardData(testData)))
