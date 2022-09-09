import random

minimum = 1
maximum = 1000




answer = random.randint(minimum, maximum)
guessed = False

while not guessed:
    write = input("devin un nombre entre 1 et 1000")
    write = int(write)
    if answer == write:
        print("vous avez raison")
        guessed = True
    if answer < write:
        print("votre reponse est plus grande que la bonne")
    if answer > write:
        print("votre reponse est plus petite que la bonne")












.00000