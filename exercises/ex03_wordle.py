"""Lets play Wordle!"""

__author__ = "730670009"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(any_len: str, single_char: str) -> bool:
    """Searches for a character at any index of another string of characters and then returns a boolean statement."""
    assert len(single_char) == 1
    index: int = 0
    while (index < len(any_len)):
        if (any_len[index] == single_char):
            return True
        else:
            index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Check if guess letters match secret word by using a string of different colored emojis."""
    assert len(guess) == len(secret)
    index: int = 0
    store: str = ""
    while (index < len(secret)):
        if (secret[index] == guess[index]):
            store += GREEN_BOX
        else:
            if contains_char(secret, guess[index]) is True:
                store += YELLOW_BOX
            else:
                store += WHITE_BOX
        index += 1
    return store


def input_guess(expected_length: int) -> str:
    """Check if guess is the proper length of secret word according to user entry and then return the entry."""
    guess: str = input(f"Enter a {str(expected_length)} character word: ")
    while len(guess) > expected_length or len(guess) < expected_length:
        guess = input(f"That wasn't {str(expected_length)} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    goal_length: int = 5
    correct: bool = False 
    while turns < 7 and correct is False:
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(goal_length)
        print(emojified(guess, "codes"))
        if emojified(guess, "codes") == GREEN_BOX * goal_length:
            print(f"You won in {str(turns)}/6 turns!")
            correct = True
        turns += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()