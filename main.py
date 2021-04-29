"""
Main game file
"""
#import essential files
import os
from rich import print
import calculate

validChoices = ['a', 's', 'd', 'm']

def main():
	menu()

def menu():
	menuLoop = True
	while menuLoop:
		os.system('cls')
		print(f"""
			[red]This game will help you with math.[/] 
			
			[green]Please choose:[/]
			[blue](A)ddition
			(S)ubtraction
			(M)ultiplication
			(D)ivion[/]
			""")


		while True:
			mathChoice = (input("Choose up to 4: (ASMD) "))
			mathChoice = mathChoice.lower()
			if any(elem not in validChoices for elem in list(mathChoice)):
				print("Invalid choice.")
			else:
				break

		while True:
			try:
				gamesChoice = int(input("How many problems would you like? (1 - 30)"))
				break
			except:
				print("Invalid choice, please choose between 1 and 30.")
		if gamesChoice >= 1 and gamesChoice <= 30:
			calculate.problemSet(mathChoice, gamesChoice)
		else:
			pass



if __name__ == "__main__":
	main()