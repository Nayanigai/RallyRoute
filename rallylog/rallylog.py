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
elif choice == 2:
    print("Exiting RallyLog")
else:
    print("Invalid choice")
