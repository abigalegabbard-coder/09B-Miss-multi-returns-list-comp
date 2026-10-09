# In python, a function can return multiple values using a single return statement
# When the interpreter encounters a return statement in function, control is set back to the calling code

# returning multiple values:
def getPlayerStats():
    name = "Isaac"
    score = 95
    level = 3

    return name, score, level

# recieveing multiple values:
playerName, playerScore, playerLevel = getPlayerStats()
# variables above recieve recieve the values in the same order they were returned

print(playerName)
print(playerScore)
print(playerLevel)

# recieve the values as a tuple:
player = getPlayerStats()
print(player)
print(player[0])

# you can ignore values you don't want
pname, _, plevel = getPlayerStats() #note: the _ is just a python convention
print(pname)
print(_)