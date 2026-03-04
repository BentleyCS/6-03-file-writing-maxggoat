import random

#You need to create your own test file for this assignment.
#Because we are dealing with both reading and writing to files. Your test file will be more complicated than it has been.

def writeFile(inputList, fileName):
    #Creates a file of the given name and adds each value from the list to said file with each line being
    # an index from the list.
    with open(fileName, 'w') as file:
        for i in inputList:
            file.write(str(i)+'\n')

writeFile([10,20,"apple"], "apple2.txt")
test_data = [1, 2, 3]
file_name = "test.txt"
writeFile(test_data, file_name)
with open(file_name, 'r') as file:
    contents = file.read()
    print("xxx")
print(contents)
print("zzz")
assert contents == "1\n2\n3\n"

def sortNames(fileName, targetFile):
    with open(fileName, 'r') as file:
        out1 = file.readlines()
    out1.sort()
    print(out1)
    writeFile(out1, targetFile)

    #Modify the below function such that it takes in source file and a target file.
    #Sort all of the values from the source file and write them to the target file
    #I recommend using .sort() for this. You do not need to write the sorting algorithm yourself.


sortNames("apple.txt","sampleA.txt")



def highScore( newScore: int):
    #Modify the function such that it adds a new score to the file scores.txt
    #Then return the average score from all of the scores in scores.txt
    with open("scores.txt",'a') as file:
        file.write(str(newScore)+'\n')


highScore(random.randint(1,100))

