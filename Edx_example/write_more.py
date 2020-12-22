#r+ more
with open('example2.txt','r+') as testwritefile:
    data = testwritefile.readlines()
    testwritefile.seek(0,0)     #write at beginning of file

    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("finished\n")

    testwritefile.truncate()    #clear the file then write on file
    testwritefile.seek(0,0)
    print(testwritefile.read())
