import csv
from sys import argv

def main(argv):

    # correct command line errors
    if len(argv) != 3:
        print("Usage ./ argument count")

    # open file of people's dna
    with open(argv[1], "r") as file:
        people = csv.reader(file)
        #f.read() ??
        agatCount = people[0]
        for row in fbi:
            name = row[0] # name is first item in dict
            people[name]+= 1 # move to next name
        # for name in people:


    # open file of fbi dna
    fbi = open(argv[2], "r")


    # iterate through each letter and search for str
    # s[i : j] = substring
    for i = letter, j = letter + 4, j < len(string) - 4

    for letter in fbi:
        i = letter
        j = 0
        if j < len(fbi) - 4:
            j = letter + 4
        # else
        # compare substring w headers in people file
        for fbi[i : j] in fbi:
            if fbi[i : j] ==
                count += 1
                if count > max

            elif letter == "A":
                if letter + 1 == "A":
                    if letter + 2 == "T":
                        if letter + 3 == "G":
                            aatgCount += 1
            elif letter == "T":
                if letter + 1 == "A":
                    if letter + 2 == "T":
                        if letter + 3 == "C":
                            tatcCount += 1
            # else:

    #find str counts of people

    #find max of each str in fbi
    max = 0
    for letter in fbi:
        if agatCount > max:
            max = letter

    #Compare str counts of people w str counts of fbi
    for i in range (4):
        if agatCount == people[i]:
            # if aatgCount == people[]:
                # if
            print("yes")
        else:
            print("no match")
    fbi.close()

main()
