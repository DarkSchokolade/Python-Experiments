import random

intro = r"""
#######################################
WELCOME TO HANGMAN       
+---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
            --MADE BY: SUHAS K SHETTY
#######################################  
  
GUESS THE WORD BELOW:

"""
print(intro)

f = open("WordList.txt", "r", encoding="utf-8")
txt = f.read()
lines = txt.split("\n")
word = random.choice(lines)
arr = list(word)  # splits the word
result = []  # stores the result after each guess
randLetter = random.randrange(len(word))

# random letter hint and blanks
for i in range(len(word)):
    if arr[i] != arr[randLetter]:
        result.append("_")
    else:
        result.append(arr[randLetter])

print(result)

# lives logic
def main():
    lives = 5
    while True:
        if lives >= 1:
            wordGuess = input("\n Enter a letter:  ")
            # check if the letter is present
            # get the position and then reset it in result
            for i in range(len(arr)):
                if wordGuess == arr[i]:
                    result[i] = wordGuess
            if wordGuess not in arr:
                lives = lives - 1
                print(":( --> wrong guess   lives:" + str(lives))
            print(result)

        if lives == 0:
            print(
                """
            ***************************************
            --GAME OVER, BETTER LUCK NEXT TIME-- (✖╭╮✖)
            ***************************************
            """
            )
            print("THE CORRECT ANSWER IS: " + word.upper() + "\n")
            break
        if result == arr:
            print(
                """
            ***************************************
            --THAT'S THE RIGHT ANSWER-- (▀̿Ĺ̯▀̿ ̿)
            ***************************************
            """
            )
            break


main()
