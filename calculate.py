"""
Calculations
"""
import random


def nextProblem(mathChoice, validChoices):
	getOperation = random.choices(mathChoice)  ## grab a random choice
	getOperation = ''.join(getOperation)  ## is there a cleaner way to get rand choice witout normalizing to str?
	x0 = random.randrange(11)
	x1 = random.randrange(11)

	if getOperation == validChoices[0] : #addition -- seems legit
		print(x0, "+", x1, "=")
		getAnswer = int(input())
		if (x0 + x1) == getAnswer:
			pass
		else:
			pass

	elif getOperation == validChoices[1] : #subtraction -- needs to be cleaned up to ensure no negative integers
		print(x0, "-", x1, "=")
		getAnswer = int(input())
		if (x0 - x1) == getAnswer:
			pass
		else:
			pass

	elif getOperation == validChoices[2] : # division -- needs to be cleaned up to ensure no irrationals, etc.
		print(x0, "/", x1, "=")
		getAnswer = int(input())
		if (x0 / x1) == getAnswer:
			pass
		else:
			pass

	elif getOperation == validChoices[3] : # multiplication -- seems legit
		print(x0, "x", x1, "=")
		getAnswer = int(input())
		if (x0 * x1) == getAnswer:
			pass
		else:
			pass

	else:
		pass

def problemSet(mathChoice, gamesChoice, validChoices):
	counter = 0
	counthigh = gamesChoice
	while counter < counthigh:
		nextProblem(mathChoice, validChoices)
		counter += 1

