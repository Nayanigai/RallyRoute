import csv
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
    rally_history = []

    while True:
        print("Who won Rally", rally, "?")
        print("1.", player1)
        print("2.", player2)

        winner = int(input("Enter your choice: "))

        if winner == 1:
            score1 = score1 + 1
            rally_history.append(player1)

        elif winner == 2:
            score2 = score2 + 1
            rally_history.append(player2)

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
    print("\n========== RALLY HISTORY ==========")
    for i in range(len(rally_history)):
        print("Rally", i + 1, ":", rally_history[i])
    print("Total Rallies:", len(rally_history))
    with open("match_results.csv", "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            player1,
            player2,
            score1,
            score2,
            player1 if score1 > score2 else player2,
            len(rally_history)
        ])
    print("Match result saved successfully!")
    
    with open("rally_history.csv", "a", newline="") as file:
        writer = csv.writer(file)

        for i in range(len(rally_history)):
            writer.writerow([
                player1,
                player2,
                i + 1,
                rally_history[i]
            ])

    print("Rally history saved successfully!")
    
    print("\n========== MATCH STATISTICS ==========")

    total_rallies = len(rally_history)

    player1_points = rally_history.count(player1)
    player2_points = rally_history.count(player2)

    player1_percentage = (player1_points / total_rallies) * 100
    player2_percentage = (player2_points / total_rallies) * 100

    print("Total Rallies:", total_rallies)

    print(player1, "Points:", player1_points)
    print(player2, "Points:", player2_points)

    print(player1, "Scoring Percentage:", round(player1_percentage, 2), "%")
    print(player2, "Scoring Percentage:", round(player2_percentage, 2), "%")

    streak1 = 0
    streak2 = 0
    longest1 = 0
    longest2 = 0

    for winner_name in rally_history:
        if winner_name == player1:
             streak1 = streak1 + 1
             streak2 = 0
             if streak1 > longest1:
                longest1 = streak1
        else:
            streak2 = streak2 + 1
            streak1 = 0
            if streak2 > longest2:
                longest2 = streak2
    print(player1, "Longest Winning Streak:", longest1)
    print(player2, "Longest Winning Streak:", longest2)
    
elif choice == 2:
    print("Exiting RallyLog")

else:
    print("Invalid choice")
