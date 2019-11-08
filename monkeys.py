import random, string
#Open the passage.txt and store the entire text in the "passage" variable
f = open("passage.txt", "r")
passage = f.read()

#Obtain list of all possible characters in the passage and store it in the "allCharacters" variable
allCharacters = []
for character in passage:
    if character not in allCharacters:
        allCharacters += character
        
total = ""
guess = ""
stringLength = input("Desired length of search query: ")

#Begin generating random strings
while True:
    temp = random.choice(allCharacters)
    total += temp
    print(temp, end = '')
    guess = total[-int(stringLength):]

    #When string is found in passage
    if guess in passage and len(guess) >= int(stringLength):
        break
print("\n\nThe string " + '"' + guess + '"' + " was found in the following location:\n")
print("..." + passage[passage.find(guess)-100:passage.find(guess)+100] + "...") #Print the section of passage where the random string was found.
