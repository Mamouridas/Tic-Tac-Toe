positions = [0] * 9 #This will hold information about who has the position (P1(1),P2(2),no one(0))
visiblePositions = [" "] * 9
row = ["a","b","c"]
column = ["1","2","3"]

def translator(inp): #Translates user's input in list position for the board
	if (inp[0].lower() == "a"):
		return(int(inp[1])-1)
	elif(inp[0].lower() == "b"):
		return(int(inp[1])+2)
	else:
		return(int(inp[1])+5)

def isInputValid(inp):
	if (len(inp) != 2):
		print("Invalid input")
		return False
	elif (inp[0].lower() not in row):
		print("Invalid input but right number of letters")
		return False
	elif (inp[1] not in column):
		print("Invalid input but right first letter")
		return False
	elif (positions[translator(inp)] != 0):
		print("position is not empty")
		return False
	else:
		return True

def printBoard():
	marks = 0
	k = "B"
	print("  1 2 3") #For the first line of the board
	print("A ", end = "") 
	for i in visiblePositions:
		if (marks == 3):
			print("\n",k," ",i," ",sep = "", end = "")
			k = "C"
			marks = 1
		else:
			print(i," ", sep = "", end = "")
			marks += 1

def playerTurn(player):
	tempInp = input("\nPlayer "+str(player)+" please enter the position you want to play to:").strip()
	while (not isInputValid(tempInp)):
		tempInp = input("\nPlayer "+str(player)+" please enter the position you want to play to:").strip()
	position = translator(tempInp) #This is the second time I do the same translation, I should check that
	positions[position] = player
	if (player == 1):
		visiblePositions[position] = "X"
	else:
		visiblePositions[position] = "O"
	return position

def ThreeInRow(player, position): #TODO! Find a better way to do this
	if (position == 0): #Top-Left
		if(positions[1] == player and positions[2] == player):
			WeHaveAWinner(player)
		elif(positions[3] == player and positions[6] == player):
			WeHaveAWinner(player)
		elif(positions[4] == player and positions[8] == player):
			WeHaveAWinner(player)
	elif (position == 1): #Top-Mid
		if(positions[0] == player and positions[2] == player):
			WeHaveAWinner(player)
		elif(positions[4] == player and positions[7] == player):
			WeHaveAWinner(player)
	elif (position == 2): #Top-Right
		if(positions[0] == player and positions[1] == player):
			WeHaveAWinner(player)
		elif(positions[5] == player and positions[8] == player):
			WeHaveAWinner(player)
		elif(positions[4] == player and positions[6] == player):
			WeHaveAWinner(player)
	elif (position == 3): #Mid-Left
		if(positions[4] == player and positions[5] == player):
			WeHaveAWinner(player)
		elif(positions[0] == player and positions[6] == player):
			WeHaveAWinner(player)
	elif (position == 4): #Center
		if(positions[0] == player and positions[8] == player):
			WeHaveAWinner(player)
		elif(positions[2] == player and positions[6] == player):
			WeHaveAWinner(player)
		elif(positions[1] == player and positions[7] == player):
			WeHaveAWinner(player)
		elif(positions[3] == player and positions[5] == player):
			WeHaveAWinner(player)
	elif (position == 5): #Mid - Right
		if(positions[2] == player and positions[8] == player):
			WeHaveAWinner(player)
		elif(positions[3] == player and positions[4] == player):
			WeHaveAWinner(player)
	elif (position == 6): #Bot - Left
		if(positions[3] == player and positions[0] == player):
			WeHaveAWinner(player)
		elif(positions[7] == player and positions[8] == player):
			WeHaveAWinner(player)
		elif(positions[4] == player and positions[2] == player):
			WeHaveAWinner(player)
	elif (position == 7): #Bot - Mid
		if(positions[4] == player and positions[1] == player):
			WeHaveAWinner(player)
		elif(positions[6] == player and positions[8] == player):
			WeHaveAWinner(player)
	else: #Bot - Right
		if(positions[7] == player and positions[6] == player):
			WeHaveAWinner(player)
		elif(positions[5] == player and positions[2] == player):
			WeHaveAWinner(player)
		elif(positions[4] == player and positions[0] == player):
			WeHaveAWinner(player)

def WeHaveAWinner(winner):
	print("\nCongratulations player", winner, "won this round")
	exit(0)


def main():
	player = 1
	rounds = 1
	printBoard()
	while(rounds <= 9):
		position = playerTurn(player)
		printBoard()
		if (rounds >= 5):
			ThreeInRow(player, position)
		if(player == 1):
			player = 2
		else:
			player = 1
		rounds += 1
	print("\nRound Draw!")
	exit(0)

main()


#TODO!
#Create a bot that never lose 