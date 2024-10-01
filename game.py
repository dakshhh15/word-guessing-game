import random

title = "wordle jr"
word_bank = []

with open("words.txt") as words:
    for line in words:
        word_bank.append(line.rstrip().lower())

guess_the_word = random.choice(word_bank)

misspelled_letters = []
wrong_letters = []
max_turns = 5
current_turns = 0

print("Welcome to", title, "!!")
print("You have to guess a", len(guess_the_word), "letter word.")
print("You have", max_turns, "turns to guess the letter.")

while current_turns < max_turns:
    word = input("Guess a word: ")

    if len(word) != guess_the_word or not word.isaplha():
        print("Enter a 5 letter word")
        continue

    index = 0
    for c in word:
        if c == word[index]:
            print(c, end="")
            if c in misspelled_letters:
                misspelled_letters.remove(c)
        
        elif c in word:
            if c not in misspelled_letters:
                misspelled_letters.append(c)

        else:
            if c not in wrong_letters:
                wrong_letters.append(c)
            print("_", end=" ")
            index += 1
