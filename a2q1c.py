#
# Name: Julian Lankstead
# Student Number: 101043448
#
# References: Gaddis, T (2015). "Starting Out With Python"

X = raw_input("Does your character have a beard? ")

if X == "yes":
	print("I have 5 characters with a beard!")
	X = raw_input("Does your character have a wig? ")

	if  X == "yes":
		print("Your character is in position 1,3" )
