import random

class NumberGuesser: 
	# define different arrays/tuples of possible replies for more variety, so it feels less repetitive -> here its important for me that the indication of the direction is at the end of the sentence, to easily get the information when playing
	high_set = ("your guess was too high", "next time, try it a bit lower", "woah hold on there, the number isn't that high!", "uhh cold, so cold up there, maybe go a bit down")
	low_set = ("your guess was too low", "And the player saw the number at the top, and they thought to go up", "the number is not what you think, it might be a bit higher", "up up up, you should go up up up")

	def __init__(self, min=0, max=100, seed=None):
		self.min = min			# set min and max values for the random number generation
		self.max = max
		random.seed(seed)		# set the random seed if one was given
		self.guess_count = 1	# counter for the number of guesses

		self.number = random.randint(self.min, self.max)	# generate the random integer in our set range -> this is the value the user has to guess
		
	# funtion to generate and validate an integer input inside the set min-max 
	def get_int_input(self):
		str_in = input(f"Please guess a number between {self.min} and {self.max}: ")	# get input from the user and store it as a string
		
		try:
			num_in = int(str_in)	# try to convert the string to an integer and return it, if it worked
			return True, num_in
		except:
			print(f"\t INVALID FORMAT please enter only a full number")	# if the integer conversion failed, inform the player and return false
			return False, 0
			
	# function to compare the user input with the number that has to be guessed
	def process_input(self):
		while True:
			valid, num_in = self.get_int_input()
			
			if(valid):
				break

		if(num_in == self.number):	
			if(self.guess_count == 1):
				print("\t UNBELIEVABLE!! YOU WON WITH A SINGLE GUESS")
			else:
				print(f"\t CONGRATULATIONS you won in {self.guess_count} guesses")

			return True
		else:
			if(num_in > self.number):
				print("\t",NumberGuesser.high_set[random.randint(0,len(NumberGuesser.high_set)-1)])
			else:
				print("\t",NumberGuesser.low_set[random.randint(0,len(NumberGuesser.low_set)-1)])

			self.guess_count += 1		# increase the guess counter by 1

			return False

	# the simple play loop of one round of playing the game
	def play(self):
		win = False
		while not win:
			win = self.process_input();



# main program
guesser = NumberGuesser()
guesser.play()