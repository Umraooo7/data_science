#Appending Files

#write a new line to text file
with open('example2.txt','a') as testwritefile:
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")
    testwritefile.write("This is line F\n")

with open('example2.txt','r') as testwritefile:
    print(testwritefile.read())

#additonal modes
#r+ : reading and writing. cannot turncate the file.
#w+ : writing and reading. turncates the file.
#a+ : appending and reading

#trying out the a+
