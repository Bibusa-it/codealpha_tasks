import random

def hangman():
    # Predefined list of 5 words
    words = ['python', 'programming', 'hangman', 'developer', 'internship']
    
    # Select a random word from the list
    word = random.choice(words).lower()
    
    # Game variables
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6
    word_completion = '_' * len(word)
    guessed = False
    
    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters. You have {max_incorrect} incorrect guesses allowed.")
    
    while not guessed and incorrect_guesses < max_incorrect:
        print("\nWord:", ' '.join(word_completion))
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        
        # Get player's guess
        guess = input("Please guess a letter: ").lower()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
            
        guessed_letters.append(guess)
        
        # Check if guess is in the word
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            
            # Update word completion
            new_completion = ""
            for i in range(len(word)):
                if word[i] == guess:
                    new_completion += guess
                else:
                    new_completion += word_completion[i]
            word_completion = new_completion
            
            # Check if word is complete
            if '_' not in word_completion:
                guessed = True
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1
    
    # Game result
    if guessed:
        print(f"\nCongratulations! You guessed the word: {word}")
    else:
        print(f"\nGame over! The word was: {word}")

# Run the game
if __name__ == "__main__":
    hangman()