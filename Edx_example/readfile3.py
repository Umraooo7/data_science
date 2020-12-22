# Iteration through the line
example1 = "textf1.txt"
with  open(example1, "r") as file1:
    i = 0;
    for line in file1:
        print("Iteration", str(i), ": ", line)
        i = i + 1

#Read all lines and save as a list
example2 = "textf2.txt"
with open(example2, "r") as file2:
    fileaslist = file2.readlines()

fileaslist[1]
