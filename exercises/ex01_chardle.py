"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730670009"

word: str = input("Enter a 5-character word: ")
if len(word) > 5 or len(word) < 5:
    print("Error: Word must contain 5 chracters ")
    exit()
letter: str = input("Enter a single character: ")
if len(letter) > 1 or len(letter) < 1:
    print("Error: Character must be a single character ")
    exit()
print("Searching for " + letter + " in " + word)
instance: int = 0
if word[0] == letter:
    print(letter + " found at index 0")
    instance += 1
if word[1] == letter:
    print(letter + " found at index 1")
    instance += 1
if word[2] == letter:
    print(letter + " found at index 2")
    instance += 1
if word[3] == letter:
    print(letter + " found at index 3")
    instance += 1
if word[4] == letter:
    print(letter + " found at index 4")
    instance += 1
if instance == 1:
    print("1 instance of " + letter + " found in " + word)
if instance == 0:
    print("No instances of " + letter + " found in " + word)
else: 
    print(str(instance) + " instances of " + letter + " found in " + word)
