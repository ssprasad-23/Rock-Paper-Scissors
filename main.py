
from random import randint

t = ["rock", "paper", "scissors"]
computer = t[randint(0, 2)]

player = False

while not player:
	player = input("\nInput: rock, paper, or scissors:\n")
	if player == computer:
		print("It is a TIE!!!!")

	elif player == "rock":
		if computer == "paper":
			print("Sorry you lost, paper beats rock")
		else:
			print("Yee boy, you won!!! rock beats paper")

	elif player == "paper":
		if computer == "scissors":
			print("Sorry you lost, scissors beats paper")
		else:
			print("Yee boy, you won!!! scissors beats paper")

	elif player == "scissors":
		if computer == "rock":
			print("Sorry you lost, rock beats scissors")
		else:
			print("Yee boy, you won!!! scissors beats rock")

	print(f"computer was: {computer}")
	player = False
	computer = t[randint(0, 2)]

