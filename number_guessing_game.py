import random
import time
import os

def get_difficulty():
    print("🎮 Choose Difficulty Level:")
    print("1. Easy (1-20, 10 attempts)")
    print("2. Medium (1-50, 7 attempts)")
    print("3. Hard (1-100, 5 attempts)")

    
    choice = input("Enter 1 / 2 / 3: ")

    if choice == '1':
        return 1, 20, 10
    elif choice == '2':
        return 1, 50, 7
    elif choice == '3':
        return 1, 100, 5
    else:
        print("⚠️ Invalid choice. Defaulting to Medium.")
        return 1, 50, 7

def load_highscore():
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as file:
            try:
                return int(file.read())
            except:
                return None
    return None

def save_highscore(score):
    with open("highscore.txt", "w") as file:
        file.write(str(score))

def play_game():
    low, high, max_attempts = get_difficulty()
    secret_number = random.randint(low, high)
    attempts = 0
    highscore = load_highscore()

    print(f"\n🔢 I have chosen a number between {low} and {high}.")
    print(f"🧠 You have {max_attempts} attempts to guess it!")

    while attempts < max_attempts:
        try:
            guess = int(input(f"\n👉 Attempt {attempts+1}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("❌ Invalid input! Enter a number.")
            continue

        if guess < low or guess > high:
            print(f"⚠️ Out of range! Please guess between {low} and {high}.")
            continue

        attempts += 1

        if guess < secret_number:
            print(random.choice(["📉 Too low!", "🔽 Not quite. Go higher!", "⬆️ Try a bigger number."]))
        elif guess > secret_number:
            print(random.choice(["📈 Too high!", "🔼 Overshot it. Go lower!", "⬇️ Try a smaller number."]))
        else:
            print(f"\n🎉 Correct! You guessed it in {attempts} attempts.")
            if highscore is None or attempts < highscore:
                print("🏆 New High Score! Well done.")
                save_highscore(attempts)
            else:
                print(f"📊 High Score: {highscore} attempts")
            break
    else:
        print(f"\n😢 You've used all {max_attempts} attempts.")
        print(f"The correct number was: {secret_number}")

def main():
    while True:
        print("\n🌟 Welcome to Aditya's Number Guessing Game 🌟")
        play_game()

        again = input("\n🔁 Do you want to play again? (y/n): ").lower()
        if again != 'y':
            print("👋 Thanks for playing! See you next time.")
            break
        print("\n🔄 Restarting...\n")
        time.sleep(1)

if __name__ == "__main__":
    main()
