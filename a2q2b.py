#
# Name: Julian Lankstead
# Student Number: 101043448
#
# References: Gaddis, T (2015). "Starting Out With Python"

StatementOne = raw_input("Does your arrow only face down? ")

if StatementOne == "yes":
	StatementTwo = raw_input("Are there two lines below the arrow? ")

	if StatementTwo == "yes":
		print("Your arrow is in position 2,5")

	if StatementTwo == "no":
		print("Your arrow is in position 1,1")

if StatementOne == "no":
	StatementTwo = raw_input("Does your arrow only face up? ")

	if StatementTwo == "yes":
		StatementThree = raw_input("Is there a line under the arrow? ")

		if StatementThree == "yes":
			print("Your arrow is in position 2,2")

		if StatementThree == "no":
			StatementFour = raw_input("Does your arrow have a curved stem? ")

			if StatementFour == "yes":
				print("Your arrow is in position 2,4")

			if StatementFour == "no":
				print("Your arrow is in position 2,3")

	if StatementTwo == "no":
		StatementFive = raw_input("Does your arrow only face right? ")

		if StatementFive == "yes":
			StatementSix = raw_input("Does your arrow have a curved stem? ")

			if StatementSix == "yes":
				print("Your arrow is in position 1,3")

			if StatementSix == ("no"):
				print("Your arrow is in position 1,4")

		if StatementFive == "no":
			StatementSeven = raw_input("Does your arrow only face left? ")

			if StatementSeven == "yes":
				print("Your arrow is in position 2,1")

			if StatementSeven == "no":
				StatementEight = raw_input("Does your arrow face in all directions? ")

				if StatementEight == "yes":
					print("Your arrow is in position 1,5")

				if StatementEight == "no":
					print("Your arrow is in position 1,2")
