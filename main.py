def Findme(liste):
    new_liste = []
    result = {}
    for i in range(len(liste)):
        if liste[i] in new_liste:
            result[liste[i]] = 1
        else:
            new_liste.append(liste[i])
    return "The Duplicate numbers are "+ str(result.keys())[9:]
x = [1,5,7,44,76,5,7,45,22,121,44,5]
print(Findme(x))