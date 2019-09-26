from capitals import states
import random

print("Welcome to your States and Capitals exam")
print("Please type in the correct captial for each State that you are presented, Do this for all 50 States:")

i = 0
array = []

for state in states:
    i += 1  
    state_name = states[i]["name"]
    state_capital = states[i]["capital"]
    array.append({'name': state_name, 'capital': state_capital, 'correctcount': 0,'incorrectcount':0})
    if i == 49:
        break

random.shuffle(array)

y = 1
j = 0

while y == 1:
    j += 1
    user = input("What is the capital of {}? ".format(array[j]["name"]))
    print(user)
    if user == array[j]["capital"]:
        print("You are correct!")
        array[j]["correctcount"] += 1
        print("Your total correct guesses are: {0}. Your total incorrect guesses are:{1}"
        .format(array[j]['correctcount'], array[j]['incorrectcount']))
    else:
        print("You are incorrect!")
        array[j]["incorrectcount"] += 1
        print("Your total correct guesses are: {0}. Your total incorrect guesses are:{1}"
        .format(array[j]['correctcount'], array[j]['incorrectcount']))
    k = 1
    if j == 10:   
        while k == 1:        
            j = 0
            userEndGame = input("Would You Like to Play Again? Type yes or no (case sensitive) ")
            if userEndGame == "no":
                y = 0
                k = 0
            elif userEndGame =="yes":
                k = 0