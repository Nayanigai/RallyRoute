print("========== RALLYLOG ==========")
print("1. Start New Match")
print("2. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Starting a new match")

    player1 = input("Enter Player 1 name: ")
    player2 = input("Enter Player 2 name: ")

    print("Match started!")
    print(player1, "0 - 0", player2)

    score1 = 0
    score2 = 0
    rally = 1

    while True:
        print("Who won Rally", rally, "?")
        print("1.", player1)
        print("2.", player2)

        winner = int(input("Enter your choice: "))

        if winner == 1:
            score1 = score1 + 1
        elif winner == 2:
            score2 = score2 + 1
        else:
            print("Invalid choice")
            continue

        print(player1, score1, "-", score2, player2)
        rally = rally + 1
        if score1 == 30 or score2 == 30:
            break

        if score1 >= 21 or score2 >= 21:
            if abs(score1 - score2) >= 2:
                break
    if score1 > score2:
        print("Game Winner:", player1)
    else:
        print("Game Winner:", player2)

    print("Final Score:", score1, "-", score2)    
elif choice == 2:
    print("Exiting RallyLog")

else:
    print("Invalid choice")
