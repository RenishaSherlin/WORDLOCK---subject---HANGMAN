import random

LEADERBOARD_FILE = "leaderboard.txt"


def load_scores():
    scores = []

    try:
        file = open(LEADERBOARD_FILE, "r")

        for line in file:
            line = line.strip()

            if line:
                name, score = line.split(",")
                scores.append([name, int(score)])

        file.close()

    except FileNotFoundError:
        pass

    return scores


def save_score(name, score):
    file = open(LEADERBOARD_FILE, "a")
    file.write(name + "," + str(score) + "\n")
    file.close()


def show_leaderboard():
    scores = load_scores()

    scores.sort(key=lambda x: x[1], reverse=True)

    print("\n" + "=" * 40)
    print("          🏆 LEADERBOARD")
    print("=" * 40)

    if len(scores) == 0:
        print("No scores yet!")

    else:
        for i, player in enumerate(scores[:5], start=1):
            print(i, ".", player[0], "-", player[1])

    print("=" * 40)

# ============================================================
#                 WORDLOCK - SUBJECT HANGMAN
# ============================================================
print( )
print("💀" * 22)
print( )
print("              🔐 WORDLOCK")
print("        SUBJECT CHALLENGE HANGMAN")
print( )
print("💀" * 22)

print("\nWelcome to WORDLOCK!")
print("Choose a subject and test your knowledge.")
print("Answer the question, use the clue, and guess the hidden word!")

# ============================================================
#                     QUESTION DATA
# ============================================================

subjects = {

    "1": {
        "name": "Computer Science",
        "words": [
            {
                "word": "python",
                "question": "Which programming language is commonly used for this project?",
                "hint": "It is named after a type of snake."
            },
            {
                "word": "algorithm",
                "question": "What do we call a step-by-step procedure for solving a problem?",
                "hint": "It is commonly used in computer science."
            },
            {
                "word": "variable",
                "question": "What stores a value that can change during program execution?",
                "hint": "It has a name and stores data."
            },
            {
                "word": "function",
                "question": "What is a reusable block of code that performs a specific task?",
                "hint": "In Python, it can be created using 'def'."
            },
            {
                "word": "computer",
                "question": "What electronic device processes data and executes programs?",
                "hint": "You are probably using one right now."
            },
            {
                "word": "database",
                "question": "What is an organized collection of data called?",
                "hint": "Websites often use one to store user information."
            }
        ]
    },

    "2": {
        "name": "Biology",
        "words": [
            {
                "word": "mitochondria",
                "question": "Which organelle is commonly called the powerhouse of the cell?",
                "hint": "It produces much of the cell's usable energy."
            },
            {
                "word": "photosynthesis",
                "question": "What process allows plants to make food using light?",
                "hint": "It occurs mainly in chloroplasts."
            },
            {
                "word": "chromosome",
                "question": "Where is genetic information packaged inside a cell?",
                "hint": "Humans normally have 46 of them."
            },
            {
                "word": "neuron",
                "question": "What specialized cell transmits nerve signals?",
                "hint": "It is part of the nervous system."
            },
            {
                "word": "protein",
                "question": "What biological molecule is made from amino acids?",
                "hint": "It performs many structural and functional roles."
            },
            {
                "word": "osmosis",
                "question": "What is the movement of water through a selectively permeable membrane?",
                "hint": "It involves movement of water toward higher solute concentration."
            }
        ]
    },

    "3": {
        "name": "Chemistry",
        "words": [
            {
                "word": "molecule",
                "question": "What is formed when two or more atoms chemically bond?",
                "hint": "Water is an example."
            },
            {
                "word": "element",
                "question": "What substance contains only one type of atom?",
                "hint": "Oxygen and gold are examples."
            },
            {
                "word": "reaction",
                "question": "What process changes reactants into products?",
                "hint": "It can produce new substances."
            },
            {
                "word": "catalyst",
                "question": "What speeds up a chemical reaction without being consumed?",
                "hint": "It lowers the activation energy."
            },
            {
                "word": "atom",
                "question": "What is the basic unit of an element?",
                "hint": "It contains protons, neutrons and electrons."
            },
            {
                "word": "compound",
                "question": "What substance contains two or more different elements chemically bonded?",
                "hint": "Water is a common example."
            }
        ]
    },

    "4": {
        "name": "Mathematics",
        "words": [
            {
                "word": "algebra",
                "question": "Which branch of mathematics uses symbols and letters to represent values?",
                "hint": "You may solve for x in this topic."
            },
            {
                "word": "calculus",
                "question": "Which branch studies derivatives and integrals?",
                "hint": "It includes differentiation and integration."
            },
            {
                "word": "matrix",
                "question": "What rectangular arrangement of numbers is used in linear algebra?",
                "hint": "It has rows and columns."
            },
            {
                "word": "geometry",
                "question": "Which branch studies shapes, sizes and properties of space?",
                "hint": "Triangles and circles are important here."
            },
            {
                "word": "integer",
                "question": "What do we call whole numbers including positive, negative and zero?",
                "hint": "Examples include -3, 0 and 7."
            },
            {
                "word": "equation",
                "question": "What mathematical statement shows that two expressions are equal?",
                "hint": "It normally contains an equals sign."
            }
        ]
    },

    "5": {
        "name": "General Science",
        "words": [
            {
                "word": "gravity",
                "question": "What force attracts objects toward one another?",
                "hint": "It keeps us on Earth's surface."
            },
            {
                "word": "planet",
                "question": "What type of celestial body orbits a star?",
                "hint": "Earth is one."
            },
            {
                "word": "energy",
                "question": "What is the capacity to do work?",
                "hint": "It exists in many forms such as kinetic and potential."
            },
            {
                "word": "radiation",
                "question": "How can energy travel through space as electromagnetic waves or particles?",
                "hint": "Sunlight reaches Earth this way."
            },
            {
                "word": "magnet",
                "question": "What object produces a magnetic field and attracts certain metals?",
                "hint": "It has north and south poles."
            },
            {
                "word": "electricity",
                "question": "What phenomenon involves the movement or presence of electric charge?",
                "hint": "It powers many electronic devices."
            }
        ]
    }
}


# ============================================================
#                     HANGMAN DRAWINGS
# ============================================================

hangman = [

"""
       _______
      |       |
      |
      |
      |
      |
   ___|___
""",

"""
       _______
      |       |
      |       O
      |
      |
      |
   ___|___
""",

"""
       _______
      |       |
      |       O
      |       |
      |
      |
   ___|___
""",

"""
       _______
      |       |
      |       O
      |      /|
      |
      |
   ___|___
""",

"""
       _______
      |       |
      |       O
      |      /|\\
      |
      |
   ___|___
""",

"""
       _______
      |       |
      |       O
      |      /|\\
      |      /
      |
   ___|___
"""
]


# ============================================================
#                     SUBJECT SELECTION
# ============================================================

print("\n📚 AVAILABLE SUBJECTS")
print("-" * 40)
print("1. 💻 Computer Science")
print("2. 🧬 Biology")
print("3. 🧪 Chemistry")
print("4. 📐 Mathematics")
print("5. 🌌 General Science")

while True:

    subject_choice = input("\nChoose your favourite subject (1-5): ")

    if subject_choice in subjects:
        break

    print("❌ Invalid choice. Please enter a number from 1 to 5.")


subject = subjects[subject_choice]

print("\n✅ Subject selected:", subject["name"])


# ============================================================
#                     GAME SETTINGS
# ============================================================

score = 0
round_number = 0
words_won = 0
words_lost = 0

used_words = []


# ============================================================
#                     MAIN GAME
# ============================================================

while True:

    # Stop if all words have been used
    available_words = []

    for item in subject["words"]:
        if item["word"] not in used_words:
            available_words.append(item)

    if len(available_words) == 0:
        print("\n🎉 You have completed all available words!")
        break

    round_number += 1

    # Select random word
    selected = random.choice(available_words)

    word = selected["word"]
    question = selected["question"]
    hint = selected["hint"]

    used_words.append(word)

    guessed_letters = []

    wrong_guesses = 0
    max_wrong = 5

    hint_used = False

    # ========================================================
    #                    ROUND START
    # ========================================================

    print("\n")
    print("=" * 60)
    print("                 🔐 ROUND", round_number)
    print("=" * 60)

    print("\n📚 Subject:", subject["name"])

    print("\n🧠 QUESTION")
    print("-" * 60)
    print(question)

    input("\nPress ENTER when you are ready to start guessing...")

    # ========================================================
    #                    WORD GAME
    # ========================================================

    while wrong_guesses < max_wrong:

        print("\n" + "=" * 60)

        # Hearts
        hearts = "❤️ " * (max_wrong - wrong_guesses)
        empty_hearts = "🖤 " * wrong_guesses

        print("HEARTS:", hearts + empty_hearts)

        # Hangman
        print(hangman[wrong_guesses])

        # Display hidden word
        display = ""

        for letter in word:

            if letter in guessed_letters:
                display += letter.upper() + " "

            else:
                display += "_ "

        print("\nWORD:", display)

        # Show guessed letters
        if len(guessed_letters) > 0:
            print("Guessed letters:", " ".join(
                guessed_letters).upper())

        # ----------------------------------------------------
        # Check whether the word has been completed
        # ----------------------------------------------------

        complete = True

        for letter in word:

            if letter not in guessed_letters:
                complete = False

        if complete:

            print("\n🎉🎉 YOU SOLVED IT! 🎉🎉")
            print("The word was:", word.upper())

            # Score
            round_score = 100 - (wrong_guesses * 10)

            if not hint_used:
                round_score += 25

            if round_score < 0:
                round_score = 0

            score += round_score
            words_won += 1

            print("⭐ Round Score:", round_score)
            print("🏆 Total Score:", score)

            break

        # ----------------------------------------------------
        # Game options
        # ----------------------------------------------------

        print("\nChoose an action:")
        print("1. 🔤 Guess a letter")
        print("2. 💡 Use hint")
        print("3. 🎯 Guess the whole word")
        print("4. 🚪 Quit game")

        action = input("\nEnter choice: ")

        # ====================================================
        # GUESS LETTER
        # ====================================================

        if action == "1":

            guess = input("\nEnter one letter: ").lower().strip()

            # Validation
            if len(guess) != 1:

                print("❌ Please enter exactly ONE letter.")
                continue

            if not guess.isalpha():

                print("❌ Please enter a letter only.")
                continue

            if guess in guessed_letters:

                print("⚠️ You already guessed that letter.")
                continue

            guessed_letters.append(guess)

            # Correct
            if guess in word:

                print("✅ Correct guess!")

                # Bonus
                score += 10

            # Wrong
            else:

                wrong_guesses += 1

                print("❌ Wrong guess!")
                print("You lost one ❤️ heart.")

        # ====================================================
        # USE HINT
        # ====================================================

        elif action == "2":

            if hint_used:

                print("⚠️ You already used your hint!")

            else:

                hint_used = True

                print("\n💡 HINT")
                print("-" * 40)
                print(hint)

                print("\n⚠️ Hint penalty: -20 points")

                score -= 20

                if score < 0:
                    score = 0

        # ====================================================
        # GUESS WHOLE WORD
        # ====================================================

        elif action == "3":

            full_guess = input(
                "\nEnter your guess for the whole word: "
            ).lower().strip()

            if full_guess == word:

                print("\n🎉 AMAZING! You guessed the entire word!")

                round_score = 150

                if hint_used:
                    round_score -= 20

                score += round_score
                words_won += 1

                print("⭐ Round Score:", round_score)
                print("🏆 Total Score:", score)

                break

            else:

                print("❌ Wrong answer!")

                wrong_guesses += 1

        # ====================================================
        # QUIT
        # ====================================================

        elif action == "4":

            print("\n👋 Thanks for playing WORDLOCK!")

            print("\nFinal Score:", score)

            exit()

        # ====================================================
        # INVALID OPTION
        # ====================================================

        else:

            print("❌ Invalid option. Choose 1, 2, 3 or 4.")

    # ========================================================
    #                    GAME OVER
    # ========================================================

    if wrong_guesses >= max_wrong:

        print("\n" + "=" * 60)

        print(hangman[5])

        print("💀 GAME OVER!")

        print("The correct word was:", word.upper())

        words_lost += 1

    # ========================================================
    #                    NEXT ROUND
    # ========================================================

    print("\n" + "-" * 60)

    print("Would you like to play another round?")

    print("1. ▶️ Yes")
    print("2. 🚪 No")

    again = input("\nEnter choice: ")

    if again != "1":
        break


# ============================================================
#                     FINAL RESULTS
# ============================================================

print("\n")
print("=" * 60)
print("                 🏆 FINAL RESULTS")
print("=" * 60)

print("\n📚 Subject:", subject["name"])
print("🎯 Rounds played:", round_number)
print("✅ Words solved:", words_won)
print("❌ Words missed:", words_lost)
print("⭐ Final Score:", score)

player_name = input("\nEnter your name for the leaderboard: ")

save_score(player_name, score)

print("✅ Score saved successfully!")

show_leaderboard()

# Rank system
if score >= 600:
    rank = "🏆 WORDLOCK MASTER"

elif score >= 400:
    rank = "🥇 EXPERT PLAYER"

elif score >= 200:
    rank = "🥈 SKILLED PLAYER"

else:
    rank = "🥉 ROOKIE PLAYER"

print("\nYour Rank:", rank)

print("\n" + "-" * 60)
print("          🔐 THANK YOU FOR PLAYING")
print("               WORDLOCK")
print("-" * 60)
