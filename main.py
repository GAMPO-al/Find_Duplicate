def Find_Duplicate(liste):
    new_liste = []
    result = {}
    for item in liste:
        if item in new_liste:
            result[item] = 1
        else:
            new_liste.append(item)
    return "The Duplicate numbers are " + str(result.keys())[9:]
x = [1, 5, 7, 44, 76, 5, 7, 45, 22, 121, 44, 5]
print(Find_Duplicate(x))
