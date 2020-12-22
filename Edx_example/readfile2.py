#using with method
example1 = "textf1.txt"
with open(example1, "r") as file1:
    filecontent = file1.read()
    print(filecontent)

#file1.name
#file1.mode
file1.close
print(filecontent)
#printing in groups

example2 = "textf2.txt"
with open(example2, "r") as file2:
    print(file2.read(4))
    print(file2.read(4))
    print(file2.read(7))
    print(file2.read(13))
    print("first line: " + file2.readline())    #first line

example = "textf1.txt"
with open(example, "r") as file1:
    print("it is readline: " + file1.readline(20))
    print("just 20 words: " + file1.read(20))
