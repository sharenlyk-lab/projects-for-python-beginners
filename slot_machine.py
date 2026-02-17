#Python Slot Machine 
import random

def spin_row():
    symbols = ["🍎", "🍊", "🍋",]
    results = []
    for symbol in range (3): 
        results.append(random.choice(symbols))
    return results

def print_row(row): 
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍎":
            return bet * 30
        elif row[0] == "🍊":
            return bet * 40
        elif row[0] == "🍋":
            return bet * 50
        else:
            return 0
    return 0

def main():
    balance = 100.0
    
    print("Welcome to the Python Slot Machine!")
    print("----------------------------------------")
    print(f"Current Balance: ${balance}")

    while balance > 0: 
        print(f"Current Balance: ${balance}")
        bet = input("Enter your bet amount: ")
        
        if not bet.isdigit():
            print("Invalid bet amount!")
            continue
        
        bet = int(bet)
        if bet > balance:
            print("Insufficient balance!")
            continue

        if bet <= 0:
            print("Bet must be greater than zero!")
            continue
        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0: 
            print(f"Congratulations! You won ${payout}!")
            balance += payout
        else:
            print("Sorry, you lost this round.")

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            break
    print("----------------------------------------")
    print(f"Game Over!Current Balance: ${balance}")
    print("----------------------------------------")

if __name__ == "__main__":
    main()



