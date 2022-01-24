#!python3

'''
Ask the user to enter in a list of 5 words.
Convert the word to a string literal JSON object
Write the contents to a file called 'task3.txt'

Example:
Enter a word: frog
Enter a word: french
Enter a word: puppy
Enter a word: escalate
Enter a word: ice

task3.txt contents:
["frog","french","puppy","escalate","ice"]

'''
import json
f = open("task3.txt", "w")
count = 0
z = []
while True:
    x = input('Enter a word:')
    z.append(x)
    count = count + 1
    if count == 5:
        outputData = json.dumps(z)
        f.write(outputData)
        break
    