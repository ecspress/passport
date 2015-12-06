from charIO import _Getch
import os

def promptForServiceAddition():
	print("promptForServiceAddition")

def promptForServiceDeletion():
	print("promptForServiceDeletion")

def promptForServiceModification():
	print("promptForServiceModification")

def promptToDisplayService():
	print("promptToDisplayService")

def listAllServices():
	print("listAllServices")

def promptToAddUserToAService():
	print("promptToAddUserToAService")

def promptToDeleteUserOfAService():
	print("promptToDeleteUserOfAService")

def promptToModifyUserOfAService():
	print("promptToModifyUserOfAService")

def promptToDisplayUserOfAService():
	print("promptToDisplayUserOfAService")

def listAllUsers():
	print("listAllUsers")

def processServiceMenuChoice(input):
	if input == 'a':
		promptForServiceAddition()
	elif input == 'd':
		promptForServiceDeletion()
	elif input == 'm':
		promptForServiceModification()
	elif input == 'v':
		promptToDisplayService()
	elif input == 'l':
		listAllServices()
	elif input == 'b':
		pass
	else:
		displayWrongInputAlert(input)

def processUserMenuChoice(input):
	if input == 'a':
		promptToAddUserToAService()
	elif input == 'd':
		promptToDeleteUserOfAService()
	elif input == 'm':
		promptToModifyUserOfAService()
	elif input == 'v':
		promptToDisplayUserOfAService()
	elif input == 'l':
		listAllUsers()
	elif input == 'b':
		pass
	else:
		displayWrongInputAlert(input)

def displayUsereMenu():
	print("Please choose from the following options.")
	print("\t(a) to add user to a service")
	print("\t(d) to delete user from a service")
	print("\t(m) to modify user of a service")
	print("\t(v) to view user of a service")
	print("\t(l) to list all users")
	print("\t(b) to return")

def displayServiceMenu():
	print("Please choose from the following options.")
	print("\t(a) to add service")
	print("\t(d) to delete service")
	print("\t(m) to modify service")
	print("\t(v) to view service")
	print("\t(l) to list all services")
	print("\t(b) to return")

def userMain(getch, input):
	while input != 'b':
		displayUsereMenu()
		input = getch()
		clearScreen()
		processUserMenuChoice(input)

def serviceMain(getch, input):
	while input != 'b':
		displayServiceMenu()
		input = getch()
		clearScreen()
		processServiceMenuChoice(input)

def displayInitialMenu():
	print("Please choose from the following options.")
	print("\t(s) to view service menu")
	print("\t(u) to view user menu")
	print("\t(q) to quit")

def processInitialMenuChoice(getch, input):
	if input == 's':
		serviceMain(getch, input)
	elif input == 'u':
		userMain(getch, input)
	elif input == 'q':
		pass
	else:
		displayWrongInputAlert(input)

def initialMain(getch, input):
	while input != 'q':
		displayInitialMenu()
		input = getch()
		clearScreen()
		processInitialMenuChoice(getch, input)

def displayWrongInputAlert(input):
	print("invalid option ({}) selected.".format(input))

def showWelcomeScreen():
	print("Welcome to digital airport. Please choose from the following options.")
	print("\t(e) if you already have a passport file")
	print("\t(n) to create a new passport file")
	print("\t(q) to quit")

def processWelcomeScreenInput(getch, char):
	fileName = None
	if char == 'e':
		print("Please enter the file path")
		fileName = input()
		print("opened file at {}".format(fileName))
	elif char == 'n':
		print("Please enter the file path")
		fileName = input()
		print("created file at {}".format(fileName))
	elif char == 'q':
		pass
	else:
		displayWrongInputAlert(char)

	return fileName

def clearScreen():
	os.system('clear')
	#os.system('cls')

def main(getch):
	clearScreen()
	input = ''
	fileName = None
	while input != 'q':
		showWelcomeScreen()
		input = getch()
		clearScreen()
		fileName = processWelcomeScreenInput(getch, input)
		if(fileName):
			break
	if(fileName):
		initialMain(getch, input)

if __name__ == "__main__":
	getch = _Getch()
	main(getch)
