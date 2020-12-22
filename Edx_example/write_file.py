#writing files
exmp2 = 'example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n")   #write single line
    writefile.write("This is line B")   #write multiple lines

#Read file
'''with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())
'''

#sample list of text
Lines = ["This is new line A\n","This is new line B\n","This is C"]
Lines

with open('example2.txt','w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)
#verify file is written
with open('Example2.txt','r') as testwritefile:
    print(testwritefile.read())

#setting the mode to w overwrite all existing data in the file.
with open('example2.txt','w') as writefile:
    writefile.write("Overwritten\n")
with open('example2.txt','r') as testwritefile:
    print(testwritefile.read())
