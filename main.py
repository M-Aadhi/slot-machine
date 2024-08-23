MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100



def deposit():
	while True:
		amout=input("how much  u have?")
		if amout.isdigit():
			amout = int(amout)
			if amout > 0:
				break
			else:
				print("u have that much onlyyyy")
		else:
			print("Money will represent in number dummyy")

	return amout

def get_number_of_lines():
	while True:
		line=input("whre u wanna but ur money F (1 - "+str (MAX_LINES) +")? ")
		if line.isdigit():
			line = int(line)
			if 1<=  line  <= MAX_LINES:
				print(f"do u think u will win in {line}")
				break
			else:
				print("enter the valid gambel ")
		else:
			print("gample all so  represent in number dummyy")

	return line
def get_bet():
	while True:
		amout=input("how much do u wanna bet in ur money?")
		if amout.isdigit():
			amout = int(amout)
			if MIN_BET <= amout <= MAX_BET:
				break
			else:
				print(f"do u tihnk u have that much ")
		else:
			print("Money will represent in number dummyy")

	return amout

def main():
	balance = deposit()
	lines = get_number_of_lines()
	bet = get_bet()
	print(f"u have {balance} and u bet {bet} on {lines} lines")
	


main()