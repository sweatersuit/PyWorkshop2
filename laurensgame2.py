print()
print("What is your name?")

# store input in 'name'

name = input("> ")

# use input in a print statement

print("Hello %s, welcome to the forest!" % (name))
print("Do you want to climb a tree 1 or tree 2?")

tree = input("> ")

if tree == "1":
	print("There is a mean squirrel at the top of the tree.")
	print("What do you do?")
	print("1. Ignore it and keep climbing")
	print("2. Jump down and run")

	squirrel = input(">")

	if squirrel == "1":
		print("You're really brave, aren't you?")
	elif squirrel == "2":
		print("Uh oh. The squirrel is now pelting you with acorns.")
	else:
		print("Um, that wasn't an option...")

if tree == "2":
	print("Congratulations! You've chosen the best tree in this forest.")
	print("How high do you want to climb?")
	print("1. All the way to the top")
	print("2. To the most sturdy limb")

	limb = input(">")

	if limb == "1":
		print("That's pretty ambitious")
	elif limb == "2":
		print("That seems like a safe choice")
	else:
		print("Error! Does not compute")

print("Ok, %s, what do you want to do next?" % (name))
print("1. Swim in the lake")
print("2. Climb a mountain")

