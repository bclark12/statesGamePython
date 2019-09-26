from capitals import states
import random
print("Welcome to your States and Capitals exam")
print("Please type in the correct captial for each State that you are presented, Do this for all 50 States:")
y = 1
i = 0
array = []
for state in states:
    j = 0
    h = 0
    i += 1  
    state_name = states[i]["name"]
    state_capital = states[i]["capital"]
    array.append({'state':state_name,'captial':state_capital,'correctcount':j,'incorrectcount':h})
    if i == 49:
        break
# print(array)
random.shuffle(array)
missed_count = 0
wins = 0
loser = 0
total_guesses = 0
while y == 1:
    user = input("What is the capital of {}? ".format(states[0]["name"]))
    print(user)

    if user == states[0]["capital"]:
        wins += 1
        print("You are correct!")
        y = 0
        total_guesses += 1
        print("Your total correct guesses are: " + wins + " Your total incorrect guesses are:" + losers)
    else:
        loser += 1
        print("You are incorrect!")
        count = states[t]["count"]
        total_guesses += 1
        print("Your total correct guesses are: " + wins + " Your total incorrect guesses are:" + losers)

    print(states[0])




#print(states[0]["name"])



# stateKey = dict.keys(states[0])
# stateValue = dict.get(name, default = None)

# print(stateKey)



# def function(input)