#
# Name: Julian Lankstead
# Student Number: 101043448
#
# References: Gaddis, T (2015). "Starting Out With Python"

print ("Answer the following questions and let the program guess your arrow!")
PointDown = raw_input("Does your arrow point down?   ")
PointUp = raw_input("Does your arrow point up?     ")
PointLeft = raw_input("Does your arrow point left?   ")
PointRight = raw_input("Does your arrow point right?  ")
BranchArmC = raw_input("Does your arrow have a curved branching arm? ")
BranchArm = raw_input("Does your arrow have a elbow branching arm? ")
TwoLines = raw_input("Does your arrow have two lines underneath it? ")
MultiArrows = raw_input ("Does your arrow(s) have more then one arrow? ")
LineToRight = raw_input("Does your arrow have one bold line to the left of it? ")
ThreeLineLeft = raw_input("Does your arrow have three bold lines to the right of it? ")
LineUnder = raw_input("Does your arrow have a bold line underneath it? ")

if PointDown == "yes" and BranchArm == "yes" and not MultiArrows == "yes":
	print("Your arrow is in position 1,1")

elif PointLeft == "yes" and PointDown == "yes" and not MultiArrows == "yes":
	print("Your arrow is in postion 1,2")

elif PointRight == "yes" and BranchArmC == "yes":
	print("Your arrow is in position 1,3")

elif PointRight == "yes" and LineToRight == "yes":
	print("Your arrow is in poition 1,4")

elif PointRight == "yes" and PointLeft == "yes" and PointDown == "yes" and PointUp == "yes" and MultiArrows == "yes":
	print("Your arrow is in position 1,5")

elif PointLeft == "yes" and ThreeLineLeft == "yes":
	print("Your arrow is in position 2,1")

elif PointUp == "yes" and LineUnder == "yes":
	print ("Your arrow is in position 2,2")

elif PointUp == "yes" and not MultiArrows == "yes":
	print("Your arrow is in position 2,3")

elif PointUp == "yes" and BranchArmC == "yes":
	print("Your arrow is in position 2,4")

elif PointDown == "yes" and TwoLines == "yes":
	print ("Your arrow in in position 2,5")

else:
	print("Error: Please check your picture and answers and try again.")
