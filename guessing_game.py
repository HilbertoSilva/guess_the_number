import random
repeat = "y"
while repeat == "y":
	random_number = random.randint(1,10)

	guess = input("I chose a number between 1 and 10. Guess it. ")
	n=1
	while int(guess) != random_number:
		n +=1
		if int(guess) > random_number:
			print (f"{guess} is too high. Try again.")
		else:
			print (f"{guess} is too low. Try again.")
		guess = input ("New guess: ")

	print (f"Yes! {guess} is the correct number! You took {n} tries.")	
	repeat = input ("Want to play again? (y/n) ")	

print ("Thank you for playing.")	