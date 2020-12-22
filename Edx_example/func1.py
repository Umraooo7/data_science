def mult(a, b):
    c = a*b
    print("This is not printed")
    return(c)

result = mult(12,2)
print(result)

#using if/else statement and loops in functions.
def type_of_album(artist, album, year_rel):
    print(artist, album, year_rel)
    if year_rel > 1980:
        return'Modern'
    else:
        return'Oldie'

x = type_of_album("Michael Jackson","Thriller",1985)
print(x)

#Printing elements from list
def Printlist(the_list):
    for element in the_list:
        print(element)
Printlist([1,1,58,"Earth","an ABC"])
