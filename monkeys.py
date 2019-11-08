import random, string
#Open the passage.txt and store the entire text in the passage variable
f = open("passage.txt", "r")
passage = f.read()

#Obtain list of all possible characters in the passage
allCharacters = []
for character in passage:
    if character not in allCharacters:
        allCharacters += character

#Generate random string
def randomString(stringLength): 
    return ''.join(random.choice(allCharacters) for i in range(stringLength))

#Prompt user for string length
stringLength = input("Length of randomly generated search query: ")

#Begin generating random strings
attemptNumber = 1
guess = ""
while True:
    print("Attempt " + str(attemptNumber) + ": ", end = "")
    guess = randomString(int(stringLength))
    print(guess)
    attemptNumber += 1

    #When string is found in passage
    if guess in passage:
        break
print("\nThe string " + '"' + guess + '"' + " was found on attempt " + str(attemptNumber) + " in the following location:\n")
print("..." + passage[passage.find(guess)-100:passage.find(guess)+100] + "...") #Print the section of passage where the random string was found
