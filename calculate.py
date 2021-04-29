"""
Calculations
"""
import random


def nextProblem(mathChoice):
	getOperation = random.choices(list(mathChoice))  ## Need to change this back to string
	getOperation = ''.join(getOperation)
	if getOperation == 'a' :
		augend = random.randrange(10)
		addend = random.randrange(10)
		print(augend, "+", addend, "=")
		getAnswer = int(input())
		if (augend + addend) == getAnswer:
			pass
		else:
			pass


def problemSet(mathChoice, gamesChoice):
	counter = 0
	counthigh = gamesChoice
	while counter < counthigh:
		nextProblem(mathChoice)
		counter += 1

