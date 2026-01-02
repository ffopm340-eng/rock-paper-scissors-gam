import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

def main():
    user_score = 0
    computer_score = 0
    print("Selamat datang di Rock Paper Scissors!")
    print("Ketik 'rock', 'paper', atau 'scissors'. Ketik 'quit' untuk keluar.")
    
    while True:
        user_choice = input("Pilihan Anda: ").lower()
        if user_choice == "quit":
            print(f"Skor Akhir: Anda {user_score} - Komputer {computer_score}")
            break
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Pilihan tidak valid! Coba lagi.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Komputer memilih: {computer_choice}")
        
        winner = determine_winner(user_choice, computer_choice)
        if winner == "user":
            user_score += 1
            print("Anda menang!")
        elif winner == "computer":
            computer_score += 1
            print("Komputer menang!")
        else:
            print("Seri!")
        
        print(f"Skor: Anda {user_score} - Komputer {computer_score}")

if __name__ == "__main__":
    main()