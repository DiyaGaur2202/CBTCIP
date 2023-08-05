import random
print("-----------------> WELCOME <-----------------")
print()
print(""" Winning Rules Are :-
      1- Paper Vs Rock --> Paper \n
      2- Rock Vs Scissors --> Rock \n
      3- Scissors Vs Paper --> Scissors \n""")
print()
name=input("Enter your name : -")
	
while True:
	print("""choice are :-
		1- Rock
		2- Paper
		3- Scissors
		""")
	choice =int( input("Enter your choice: "))
	print()
	if choice ==1:
		user_choice ="Rock"
	elif choice ==2:
		user_choice ="Paper"
	else:
		user_choice = "Scissors"
		
	print(" Yours choice is : ", user_choice)
	print()
	print("Now it's computer's turn ....")
	print()

	computer = random.randint(1,3)

	if computer == 1:
		computer_choice = "Rock"
	elif computer == 2:
		computer_choice = "Paper"
	else:
		computer_choice = "Scissors"
		
	print(" Computer choice is : ", computer_choice)
	print()

	if (user_choice =="Paper" and computer_choice =="Rock") or(user_choice =="Rock" and computer_choice =="Paper"):
		print(" Paper Wins!")
		result = "Paper"
	elif(user_choice == "Rock" and computer_choice =="Scissors") or (user_choice=="Scissors" and computer_choice=="Rock"):
		print("Rock Wins!")
		result =" Rock"

		
	elif(user_choice== computer_choice):
		print("Aha! It's a Tie")
		result = "Tie"
		
	else:
		print("Scissors Wins!")
		result = "Scissors"
	print()
		
	if result== "Tie":
		print("Better luck for next time")
		

	elif result == user_choice:
		print( " user Wins!")
		
		
	else:
		print("Computer Wins!")
	

	Again = input("Do you want play again? ")
	if Again == "no":
		break
print("Game Over!")
			