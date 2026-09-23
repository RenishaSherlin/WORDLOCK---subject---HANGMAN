import random

# ============================================================
#                    WORDLOCK
#             SUBJECT CHALLENGE HANGMAN
# ============================================================

LEADERBOARD_FILE = "leaderboard.txt"


# ============================================================
#                    LEADERBOARD
# ============================================================

def load_scores():
    scores = []

    try:
        file = open(LEADERBOARD_FILE, "r")

        for line in file:
            line = line.strip()

            if line:
                parts = line.split(",")

                if len(parts) == 3:
                    name = parts[0]
                    subject = parts[1]
                    score = int(parts[2])
                    scores.append([name, subject, score])

                elif len(parts) == 2:
                    # Supports older leaderboard entries
                    name = parts[0]
                    score = int(parts[1])
                    scores.append([name, "Unknown", score])

        file.close()

    except FileNotFoundError:
        pass

    return scores


def save_score(name, subject, score):
    file = open(LEADERBOARD_FILE, "a")

    name = name.replace(",", " ")
    subject = subject.replace(",", " ")

    file.write(name + "," + subject + "," + str(score) + "\n")

    file.close()


def show_leaderboard():
    scores = load_scores()

    scores.sort(key=lambda x: x[2], reverse=True)

    print("\n" + "-" * 60)
    print("                    🏆 LEADERBOARD")
    print("-" * 60)

    if len(scores) == 0:
        print("No scores yet!")

    else:
        for i, player in enumerate(scores[:10], start=1):
            print(
                str(i) + ". " +
                player[0] +
                " | " +
                player[1] +
                " | " +
                str(player[2])
            )

    print("=" * 60)


# ============================================================
#                    RANK SYSTEM
# ============================================================

def get_rank(score):

    if score >= 600:
        return "🏆 WORDLOCK MASTER"

    elif score >= 400:
        return "🥇 EXPERT PLAYER"

    elif score >= 200:
        return "🥈 SKILLED PLAYER"

    else:
        return "🥉 ROOKIE PLAYER"


# ============================================================
#                    HANGMAN DRAWINGS
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
      |      / \
      |
   ___|___
"""
]


# ============================================================
#                    SUBJECT DATA
# ============================================================

subjects = {

    "1": {
        "name": "Computer Science",

        "words": [

            {
                "word": "python",
                "difficulty": "Easy",
                "question": "Which keyword is used to define a function in Python?",
                "options": ["A) function", "B) def", "C) func", "D) define"],
                "answer": "B"
            },

            {
                "word": "variable",
                "difficulty": "Easy",
                "question": "Which symbol is commonly used to assign a value to a variable in Python?",
                "options": ["A) =", "B) ==", "C) ->", "D) :="],
                "answer": "A"
            },

            {
                "word": "algorithm",
                "difficulty": "Medium",
                "question": "What is an algorithm?",
                "options": [
                    "A) A computer virus",
                    "B) A programming language",
                    "C) A step-by-step method for solving a problem",
                    "D) A type of hardware"
                ],
                "answer": "C"
            },

            {
                "word": "database",
                "difficulty": "Medium",
                "question": "What is a database mainly used for?",
                "options": [
                    "A) Storing and organizing data",
                    "B) Drawing pictures",
                    "C) Playing music",
                    "D) Increasing screen brightness"
                ],
                "answer": "A"
            },

            {
                "word": "recursion",
                "difficulty": "Hard",
                "question": "What happens in recursion?",
                "options": [
                    "A) A function calls itself",
                    "B) A program deletes itself",
                    "C) A loop stops immediately",
                    "D) A variable becomes constant"
                ],
                "answer": "A"
            },

            {
                "word": "encryption",
                "difficulty": "Hard",
                "question": "What is encryption mainly used for?",
                "options": [
                    "A) Compressing images",
                    "B) Protecting information by converting it into coded form",
                    "C) Increasing processor speed",
                    "D) Creating computer games"
                ],
                "answer": "B"
            }
        ]
    },


    "2": {
        "name": "Biology",

        "words": [

            {
                "word": "cell",
                "difficulty": "Easy",
                "question": "What is generally considered the basic unit of life?",
                "options": [
                    "A) Tissue",
                    "B) Organ",
                    "C) Cell",
                    "D) Organ system"
                ],
                "answer": "C"
            },

            {
                "word": "protein",
                "difficulty": "Easy",
                "question": "Proteins are made from which smaller units?",
                "options": [
                    "A) Fatty acids",
                    "B) Amino acids",
                    "C) Glucose",
                    "D) Nucleotides"
                ],
                "answer": "B"
            },

            {
                "word": "photosynthesis",
                "difficulty": "Medium",
                "question": "Which gas is taken in by plants during photosynthesis?",
                "options": [
                    "A) Oxygen",
                    "B) Nitrogen",
                    "C) Carbon dioxide",
                    "D) Hydrogen"
                ],
                "answer": "C"
            },

            {
                "word": "mitochondria",
                "difficulty": "Medium",
                "question": "Which molecule is commonly described as the main energy currency of cells?",
                "options": [
                    "A) ATP",
                    "B) DNA",
                    "C) RNA",
                    "D) Glucose"
                ],
                "answer": "A"
            },

            {
                "word": "chromosome",
                "difficulty": "Hard",
                "question": "What molecule carries most hereditary information in human chromosomes?",
                "options": [
                    "A) Protein",
                    "B) DNA",
                    "C) Lipid",
                    "D) ATP"
                ],
                "answer": "B"
            },

            {
                "word": "homeostasis",
                "difficulty": "Hard",
                "question": "What does homeostasis refer to?",
                "options": [
                    "A) Cell division",
                    "B) Maintaining relatively stable internal conditions",
                    "C) Production of hormones",
                    "D) Movement of blood"
                ],
                "answer": "B"
            }
        ]
    },


    "3": {
        "name": "Chemistry",

        "words": [

            {
                "word": "atom",
                "difficulty": "Easy",
                "question": "Which particle has a negative electric charge?",
                "options": [
                    "A) Proton",
                    "B) Neutron",
                    "C) Electron",
                    "D) Nucleus"
                ],
                "answer": "C"
            },

            {
                "word": "element",
                "difficulty": "Easy",
                "question": "What does an element contain?",
                "options": [
                    "A) Only one type of atom",
                    "B) Only molecules",
                    "C) Two different compounds",
                    "D) Only ions"
                ],
                "answer": "A"
            },

            {
                "word": "molecule",
                "difficulty": "Medium",
                "question": "What is formed when two or more atoms chemically bond?",
                "options": [
                    "A) Molecule",
                    "B) Electron",
                    "C) Proton",
                    "D) Neutron"
                ],
                "answer": "A"
            },

            {
                "word": "catalyst",
                "difficulty": "Medium",
                "question": "What does a catalyst generally do?",
                "options": [
                    "A) Stops every reaction",
                    "B) Increases activation energy",
                    "C) Speeds up a reaction without being consumed",
                    "D) Turns solids into gases"
                ],
                "answer": "C"
            },

            {
                "word": "oxidation",
                "difficulty": "Hard",
                "question": "Which process is commonly associated with loss of electrons?",
                "options": [
                    "A) Reduction",
                    "B) Oxidation",
                    "C) Neutralization",
                    "D) Condensation"
                ],
                "answer": "B"
            },

            {
                "word": "equilibrium",
                "difficulty": "Hard",
                "question": "In chemical equilibrium, what is equal?",
                "options": [
                    "A) Reactant and product concentrations always",
                    "B) Forward and reverse reaction rates",
                    "C) Number of atoms and molecules",
                    "D) Mass and volume"
                ],
                "answer": "B"
            }
        ]
    },


    "4": {
        "name": "Mathematics",

        "words": [

            {
                "word": "integer",
                "difficulty": "Easy",
                "question": "Which of these is an integer?",
                "options": [
                    "A) 3.5",
                    "B) 1/2",
                    "C) -7",
                    "D) √2"
                ],
                "answer": "C"
            },

            {
                "word": "algebra",
                "difficulty": "Easy",
                "question": "What is x if x + 5 = 12?",
                "options": [
                    "A) 5",
                    "B) 6",
                    "C) 7",
                    "D) 8"
                ],
                "answer": "C"
            },

            {
                "word": "matrix",
                "difficulty": "Medium",
                "question": "A matrix is mainly arranged using what?",
                "options": [
                    "A) Rows and columns",
                    "B) Circles and lines",
                    "C) Angles only",
                    "D) Fractions only"
                ],
                "answer": "A"
            },

            {
                "word": "derivative",
                "difficulty": "Medium",
                "question": "What is the derivative of x²?",
                "options": [
                    "A) x",
                    "B) 2x",
                    "C) x²",
                    "D) 2"
                ],
                "answer": "B"
            },

            {
                "word": "probability",
                "difficulty": "Hard",
                "question": "What is the probability of getting heads when a fair coin is tossed?",
                "options": [
                    "A) 0",
                    "B) 1/4",
                    "C) 1/2",
                    "D) 1"
                ],
                "answer": "C"
            },

            {
                "word": "differential",
                "difficulty": "Hard",
                "question": "Which operation is the reverse of differentiation?",
                "options": [
                    "A) Integration",
                    "B) Multiplication",
                    "C) Division",
                    "D) Factorization"
                ],
                "answer": "A"
            }
        ]
    },


    "5": {
        "name": "General Science",

        "words": [

            {
                "word": "gravity",
                "difficulty": "Easy",
                "question": "What is the SI unit of force?",
                "options": [
                    "A) Joule",
                    "B) Watt",
                    "C) Newton",
                    "D) Pascal"
                ],
                "answer": "C"
            },

            {
                "word": "planet",
                "difficulty": "Easy",
                "question": "What does the Earth orbit?",
                "options": [
                    "A) The Moon",
                    "B) The Sun",
                    "C) Mars",
                    "D) Jupiter"
                ],
                "answer": "B"
            },

            {
                "word": "energy",
                "difficulty": "Medium",
                "question": "Which type of energy is associated with motion?",
                "options": [
                    "A) Kinetic energy",
                    "B) Chemical energy",
                    "C) Nuclear energy",
                    "D) Sound energy"
                ],
                "answer": "A"
            },

            {
                "word": "radiation",
                "difficulty": "Medium",
                "question": "Which type of radiation helps plants perform photosynthesis?",
                "options": [
                    "A) Visible light",
                    "B) Radio waves",
                    "C) Microwaves",
                    "D) X-rays"
                ],
                "answer": "A"
            },

            {
                "word": "ecosystem",
                "difficulty": "Hard",
                "question": "What does an ecosystem include?",
                "options": [
                    "A) Only animals",
                    "B) Only plants",
                    "C) Living organisms and their physical environment",
                    "D) Only microorganisms"
                ],
                "answer": "C"
            },

            {
                "word": "atmosphere",
                "difficulty": "Hard",
                "question": "Which gas makes up the largest portion of Earth's atmosphere?",
                "options": [
                    "A) Oxygen",
                    "B) Nitrogen",
                    "C) Carbon dioxide",
                    "D) Hydrogen"
                ],
                "answer": "B"
            }
        ]
    }
}


# ============================================================
#                    HELPER FUNCTIONS
# ============================================================

def display_word(word, guessed_letters):
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter.upper() + " "
        else:
            display += "_ "

    return display


def reveal_letter(word, guessed_letters):
    unguessed = []

    for letter in word:
        if letter not in guessed_letters:
            unguessed.append(letter)

    if len(unguessed) == 0:
        return None

    letter = random.choice(unguessed)
    guessed_letters.append(letter)

    return letter


def choose_subject():
    print("\n" + "=" * 60)
    print("                    📚 SUBJECTS")
    print("=" * 60)

    print("1. 💻 Computer Science")
    print("2. 🧬 Biology")
    print("3. 🧪 Chemistry")
    print("4. 📐 Mathematics")
    print("5. 🌌 General Science")
    print("6. 🎲 Random Subject")

    while True:
        choice = input("\nChoose your favourite subject (1-6): ").strip()

        if choice in subjects:
            return choice

        elif choice == "6":
            return random.choice(list(subjects.keys()))

        else:
            print("❌ Please enter a number from 1 to 6.")


def choose_difficulty():
    print("\n" + "=" * 60)
    print("                  🎚️ DIFFICULTY")
    print("=" * 60)

    print("1. 🟢 Easy")
    print("2. 🟡 Medium")
    print("3. 🔴 Hard")
    print("4. 🎲 Mixed")

    while True:
        choice = input("\nChoose difficulty (1-4): ").strip()

        if choice == "1":
            return "Easy"

        elif choice == "2":
            return "Medium"

        elif choice == "3":
            return "Hard"

        elif choice == "4":
            return "Mixed"

        else:
            print("❌ Please enter 1, 2, 3 or 4.")


def choose_question(word_data):
    print("\n" + "=" * 60)
    print("                    🧠 BONUS QUESTION")
    print("=" * 60)

    print("\n" + word_data["question"])

    for option in word_data["options"]:
        print(option)

    while True:

        answer = input("\nYour answer (A/B/C/D): ").upper().strip()

        if answer in ["A", "B", "C", "D"]:
            break

        print("❌ Please enter only A, B, C or D.")

    if answer == word_data["answer"]:

        print("\n✅ Correct!")
        print("🎁 You earned a FREE HINT!")

        return True

    else:

        print("\n❌ Incorrect.")
        print("No hint bonus this time.")

        return False


# ============================================================
#                     WELCOME
# ============================================================

print("=" * 60)
print("                    🔐 WORDLOCK")
print("              SUBJECT CHALLENGE HANGMAN")
print("=" * 60)

print("\nWelcome to WORDLOCK! 🎮")
print("Choose a subject, answer questions and solve hidden words.")
print("You have 5 ❤️ hearts in every round.")

player_name = input("\nEnter your name: ").strip()

if player_name == "":
    player_name = "Player"


# ============================================================
#                     CHOOSE SUBJECT
# ============================================================

subject_choice = choose_subject()

subject_name = subjects[subject_choice]["name"]

print("\n✅ Selected Subject:", subject_name)


# ============================================================
#                    CHOOSE DIFFICULTY
# ============================================================

difficulty = choose_difficulty()

print("✅ Difficulty:", difficulty)


# ============================================================
#                    GAME VARIABLES
# ============================================================

score = 0
round_number = 0
words_won = 0
words_lost = 0

used_words = []


# ============================================================
#                    MAIN GAME LOOP
# ============================================================

while True:

    # Create available word list
    available_words = []

    for item in subjects[subject_choice]["words"]:

        if item["word"] not in used_words:

            if difficulty == "Mixed":

                available_words.append(item)

            elif item["difficulty"] == difficulty:

                available_words.append(item)

    # If all words of chosen difficulty are finished
    if len(available_words) == 0:

        print("\n🎉 There are no more words in this difficulty!")

        if difficulty != "Mixed":

            print("You can continue with Mixed difficulty.")

            change = input(
                "\nSwitch to Mixed difficulty? (y/n): "
            ).lower().strip()

            if change == "y":
                difficulty = "Mixed"
                continue

        break


    # Choose random word
    selected = random.choice(available_words)

    word = selected["word"]

    used_words.append(word)

    guessed_letters = []

    wrong_guesses = 0

    max_wrong = 5

    hint_used = False

    round_number += 1


    # ========================================================
    #                    ROUND START
    # ========================================================

    print("\n")
    print("=" * 60)
    print("                    🔐 ROUND", round_number)
    print("=" * 60)

    print("Subject   :", subject_name)
    print("Difficulty:", selected["difficulty"])


    # ========================================================
    #                    BONUS QUESTION
    # ========================================================

    free_hint = choose_question(selected)

    if free_hint:

        revealed = reveal_letter(word, guessed_letters)

        if revealed is not None:
            print("💡 A letter has been revealed:", revealed.upper())


    # ========================================================
    #                     HANGMAN LOOP
    # ========================================================

    while wrong_guesses < max_wrong:

        print("\n" + "=" * 60)

        hearts = "❤️ " * (max_wrong - wrong_guesses)
        empty_hearts = "🖤 " * wrong_guesses

        print("HEARTS:", hearts + empty_hearts)

        print(hangman[wrong_guesses])

        print("WORD:", display_word(word, guessed_letters))


        if len(guessed_letters) > 0:

            print(
                "Guessed:",
                " ".join(guessed_letters).upper()
            )


        # ====================================================
        #                    WIN CHECK
        # ====================================================

        complete = True

        for letter in word:

            if letter not in guessed_letters:
                complete = False
                break


        if complete:

            print("\n🎉🎉 YOU WON! 🎉🎉")
            print("The word was:", word.upper())

            bonus = 50

            if wrong_guesses == 0:
                bonus += 30

                print("🔥 Perfect round bonus: +30")

            score += bonus
            words_won += 1

            print("⭐ Round bonus:", bonus)
            print("🏆 Current score:", score)

            break


        # ====================================================
        #                    ACTION MENU
        # ====================================================

        print("\nChoose an action:")

        print("1. 🔤 Guess a letter")
        print("2. 💡 Use hint")
        print("3. 🎯 Guess the whole word")
        print("4. 🚪 Quit game")


        action = input("\nEnter choice: ").strip()


        # ====================================================
        #                    LETTER GUESS
        # ====================================================

        if action == "1":

            guess = input(
                "\nEnter one letter: "
            ).lower().strip()


            if len(guess) != 1:

                print("❌ Enter exactly ONE letter.")
                continue


            if not guess.isalpha():

                print("❌ Letters only.")
                continue


            if guess in guessed_letters:

                print("⚠️ You already guessed that letter.")
                continue


            guessed_letters.append(guess)


            if guess in word:

                print("✅ Correct!")

                score += 10

                print("⭐ +10 points")

            else:

                wrong_guesses += 1

                print("❌ Wrong guess!")

                print("You lost one ❤️ heart.")


        # ====================================================
        #                       HINT
        # ====================================================

        elif action == "2":

            if hint_used:

                print("⚠️ You already used your hint!")

            else:

                hint_used = True

                revealed = reveal_letter(
                    word,
                    guessed_letters
                )

                if revealed is not None:

                    print("\n💡 HINT!")
                    print(
                        "The letter",
                        revealed.upper(),
                        "has been revealed."
                    )

                    score -= 10

                    if score < 0:
                        score = 0

                    print("⚠️ Hint cost: 10 points")


        # ====================================================
        #                  WHOLE WORD GUESS
        # ====================================================

        elif action == "3":

            full_guess = input(
                "\nEnter the complete word: "
            ).lower().strip()


            if full_guess == word:

                print("\n🎉 AMAZING!")
                print("You guessed the complete word!")

                score += 60

                words_won += 1

                print("⭐ +60 points")

                break

            else:

                print("❌ Wrong word!")

                wrong_guesses += 1

                print("You lost one ❤️ heart.")


        # ====================================================
        #                       QUIT
        # ====================================================

        elif action == "4":

            print("\n👋 Thanks for playing WORDLOCK!")

            print("Your current score:", score)

            save_score(
                player_name,
                subject_name,
                score
            )

            print("✅ Score saved!")

            show_leaderboard()

            exit()


        # ====================================================
        #                    INVALID ACTION
        # ====================================================

        else:

            print("❌ Choose 1, 2, 3 or 4.")


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

    again = input("\nEnter choice: ").strip()

    if again != "1":
        break


# ============================================================
#                    FINAL RESULTS
# ============================================================

print("\n")
print("-" * 60)
print("                 🏆 FINAL RESULTS")
print("-" * 60)

print("\nPlayer          :", player_name)
print("Subject         :", subject_name)
print("Difficulty      :", difficulty)
print("Rounds played   :", round_number)
print("Words solved    :", words_won)
print("Words missed    :", words_lost)
print("Final Score     :", score)

rank = get_rank(score)

print("Rank            :", rank)


# ============================================================
#                    SAVE SCORE
# ============================================================

save_score(
    player_name,
    subject_name,
    score
)

print("\n✅ Your score has been saved to the leaderboard!")


# ============================================================
#                    SHOW LEADERBOARD
# ============================================================

show_leaderboard()


print("\n" + "-" * 60)
print("             🔐 THANK YOU FOR PLAYING")
print("                    WORDLOCK")
print("-" * 60)
