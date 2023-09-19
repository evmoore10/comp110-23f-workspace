"""One Shot Wordle!"""

__author__ = "730670009"

secret_word: str = "python"
guess: str = input(f"What is your {len(secret_word)} letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
# check if guess is right length
while len(guess) > len(secret_word) or len(guess) < len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")
# check if guess is right guess
if str(guess) == str(secret_word):
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
# wordle block emojis
index_var: int = 0
store_var: str = ""
while index_var < len(secret_word):
    if guess[index_var] == secret_word[index_var]:
        store_var += (GREEN_BOX)
    else:
        is_yellow: bool = False
        alt_indicies: int = 0
        while (alt_indicies < len(secret_word)):
            if guess[index_var] == secret_word[alt_indicies]:
                is_yellow = True
                store_var += YELLOW_BOX
            alt_indicies += 1
        if (is_yellow is False):
            store_var += (WHITE_BOX)
    index_var += 1
print(store_var)