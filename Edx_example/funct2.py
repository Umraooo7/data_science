#custom functions, setting up default argument values
def GoodRating(rating = 4):
    if (rating < 7):
        print("This album sucks it's rating: ", rating)
    else:
        print("This album is terrific: ",rating)
print(GoodRating(7))

#global variable example
artist = 'Michael Jackson'
def printer1(artist):
    intrnal_variable = artist
    print(artist,"is an artist.")
printer1(artist)

#Collections and Functions,
def PrintAll(*args):
    print("Number of arguments: ",len(args))
    for arguments in args:
        print(arguments)
PrintAll('HorseFeather','Adonis','Bone',54,True)
