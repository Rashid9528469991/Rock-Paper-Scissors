import random
l=["rock", "scissor", "paper"]
'''
roc vs paper-> paper win
rock vs scissor-> raock wins
paper vs scissor-> scissor wins
'''
while  True:
	computercount=0
	usercount=0
	uc = int(input('''
game start...
1 Yes
2 No | Exit

		'''))
	if uc ==1:
		for a in range(1,6):
			userInput=int(input('''
1 Rock
2 Scissor
3 Paper
				'''))
			if userInput==1:
				userchoice="rock"
			elif userInput==2:
				userchoice="scissor"

			elif userInput==3:
				userchoice="paper"

			computerchoice=random.choice(l)
			print(userchoice)
			print(computerchoice)

			if computerchoice==userchoice:
				print("computer value",computerchoice)
				print("user value", userchoice)
				print("Game Draw")
				usercount=usercount+1
				computercount=computercount+1

			elif (userchoice=="rock" and computerchoice=="scissor") or (userchoice=="paper" and computerchoice=="rock") or (userchoice=="scissor" and computerchoice=="paper"):
				print("computer value",computerchoice)
				print("user value", userchoice)
				print("You Win")
				usercount=usercount+1
			else:
				print("computer value",computerchoice)
				print("user value", userchoice)
				print("Compuetr Win")
				
				computercount=computercount+1

			if usercount==computercount:
				print("Final Game Draw ...")
				print("User score", usercount)
				print("computer Score", computercount)
			elif usercount>computercount:
				print("Final You win Game ...")
				print("User score", usercount)
				print("computer Score", computercount)


			else:
				print("Final computer win Game ...")
				print("User score", usercount)
				print("computer Score", computercount)

		else:
			break;






