import random
secret_number = random.randint(0,10)
guess_count = 0
guess_limit = 3
print("""                 
      
                                         * "WELCOME TO GUESSING GAME *
                                   Game Objective: Guess the secret number !
    
      Game Rules: 
      1) A Random secret number will be set in every round
      2) You will have three chances to guess the number
      3) You can only use single digit integers to answer in every chance
      4) If you guess the wrong number in all three chances then you loose
      5) If you guess the right number then you win the game!
      
      """)
while guess_count <= 2:
    guess = int(input("Guess  : "))
    guess_count  += 1
    if guess == secret_number:
        print("""         Congratulations !! 
              You won !""")
        break
else:
    print(" You lost ! Try again")

