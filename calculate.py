"""
Calculations
"""
import random


def nextProblem(mathChoice, validChoices):
	getOperation = random.choices(list(mathChoice))  ## Need to change this back to string
#	getOperation = ''.join(getOperation)
	if getOperation == validChoices[0] :
		augend = random.randrange(10)
		addend = random.randrange(10)
		print(augend, "+", addend, "=")
		getAnswer = int(input())
		if (augend + addend) == getAnswer:
			pass
		else:
			pass


def problemSet(mathChoice, gamesChoice, validChoices):
	counter = 0
	counthigh = gamesChoice
	while counter < counthigh:
		nextProblem(mathChoice, validChoices)
		counter += 1

