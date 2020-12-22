# a+ more
with open('example2.txt','a+') as testwritefile:
    print("Intial Location: {}".format(testwritefile.tell()))

    data = testwritefile.read()
    if (not data):
        print('Read nothing')
    else:
        print(testwritefile.read())

    testwritefile.seek(0,0)

    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data):
        print('Read nothing')
    else:
        print(data)

    print("Location after read: {}".format(testwritefile.tell()))
