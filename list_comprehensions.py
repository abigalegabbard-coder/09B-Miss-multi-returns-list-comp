# List comprehensions provide a concise, readable and effiecient way to create new lists

# General Format:
# [expression for item in iterable if condition]
# iterable is something like a list, tuple, or dictionary
# expression: what you want to do with each item (eg. x * 2)
# for item in iterable: the loop that goes through each value(eg. for x in ranger(1,11))
# if condition: (optional): A filter that decides which items to include

#example (traditional method - without list comprehension):
doubles = []

for x in range(1, 11):  # range(1, 11) gives numbers 1–10
    doubles.append(x * 2)

print(doubles) 

# simplify the above, and do it in one line!
doubles_lc = [x*2 for x in range(1,11)]
print(doubles_lc)

# note we can unpack lists by prepending a * to them
mykytas_query = [*[x*2 for x in range(1,11)], 99]
print(mykytas_query)

mykytas_query+=[*[x*2 for x in range(1,11)], 99]
print(mykytas_query)

# let's say we only want multiples of 5
# do it without a step function on range
multiples_of_5= [x for x in range(0,51) if x % 5 == 0]
print(multiples_of_5)

games = ["call of duty", "fortnite", "mindustry", "no man sky"]
# use list comprehension to create a list of these titles in title case
game_titles = [game.title() for game in games]
print(game_titles)

# update the above to only give back titles with more than one word and still in title case
game_titles = [game.title() for game in games if " " in game.strip()]
print(game_titles)

students = [("Zach", 54), ("Christian", 0), ("Evan", 1), ("K-luh", 106), ("Blake", 80), ("Allyn", 90)]
# use list comprehension to create a list of students who have a score of over 70 or above
# also make a list of failing students
students_passing = [x for x in students if x[1]>= 70]
students_failing = [x for x in students if x[1]< 70]
print(students_passing)
print(students_failing)