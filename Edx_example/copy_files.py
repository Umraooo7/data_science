#copying a Files
#copy file to another
with open('example2.txt','r') as readfile:
    with open('example3.txt','w') as writefile:
        for line in readfile:
            writefile.write(line)

#verify if the copy is done
with open('example3.txt','r') as testwritefile:
    print(testwritefile.read())
