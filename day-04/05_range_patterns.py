import random


# Set secret number to 12 (specified in task)
#secret_number = 12
   
# Set secret number to random nuber 1 to 20
secret_number = random.randint(1, 20)
    
# Set attempts to 0
attempts = 0
    
# Set guessed correctly to False
guessed_correctly = False
    
# WHILE guessed correctly is False
while not guessed_correctly and attempts < 5:
        
        # Get guess as text
        guess_text = input("Enter your guess: ")
        
        # IF guess is not digits only
        if not guess_text.isdigit():
            # Show number-input message
            print("Please enter numbers only.")
            
        # ELSE
        else:
            # Convert guess to a whole number
            guess = int(guess_text)
            
            # IF guess is outside 1 to 20
            if guess < 1 or guess > 20:
                # Show range message
                print("Your guess must be between 1 and 20.")
                
            # ELSE
            else:
                # Increase attempts
                attempts += 1
                
                # IF guess equals secret number
                if guess == secret_number:
                    # Show Correct and set guessed correctly to True
                    print(f"Correct! You guessed it in {attempts} attempts.")
                    guessed_correctly = True
                    
                # ELSE IF guess is below secret number
                elif guess < secret_number:
                    # Show Too low
                    print("Too low")
                    
                # ELSE: Show Too high
                else:
                    print("Too high")

print("secret number was: ", secret_number)
