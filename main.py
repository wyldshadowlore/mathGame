"""
Main game file
"""
#import essential files
import os
from rich import print


def main():
	os.system('cls')
	menu()

def menu():
	print(f"""
		[red]This game will help you with math.[/] 
		
		[green]Please choose:[/]
		[blue](A)ddition
		(S)ubtraction
		(M)ultiplication
		(D)ivion[/]
		""")

	mathChoice = input("Choose up to 4: ")
	gamesChoice = input("How many problems would you like? (1 - 30)")


if __name__ == "__main__":
	main()