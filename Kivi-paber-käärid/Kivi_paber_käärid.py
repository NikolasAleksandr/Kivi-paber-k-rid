import random
import time

def play_round(player1, player2):
    gestures = ["kivi", "käärid", "paber"]

    print("kivi... käärid... paber... üks... kaks... kolm!")

    gesture1 = input(f"{player1}, loe 'kolm' ja näita žesti (kivi/käärid/paber): ").lower()
    while gesture1 not in gestures:
        print("Viga: Vali kehtiv žest!")
        gesture1 = input(f"{player1}, loe 'kolm' ja näita žesti (kivi/käärid/paber): ").lower()

    gesture2 = input(f"{player2}, loe 'kolm' ja näita žesti (kivi/käärid/paber): ").lower()
    while gesture2 not in gestures:
        print("Viga: Vali kehtiv žest!")
        gesture2 = input(f"{player2}, loe 'kolm' ja näita žesti (kivi/käärid/paber): ").lower()

    print(f"{player1} näitas {gesture1}")
    print(f"{player2} näitas {gesture2}")

    if (gesture1 == "paber" and gesture2 == "kivi"):
        return f"{player1} võidab! Paber mähib kivi ümber."
    elif (gesture1 == "kivi" and gesture2 == "käärid"):
        return f"{player1} võidab! Kivi tuhmib või purustab käärid."
    elif (gesture1 == "käärid" and gesture2 == "paber"):
        return f"{player1} võidab! Käärid lõikavad paberit."
    elif (gesture2 == "paber" and gesture1 == "kivi"):
        return f"{player2} võidab! Paber mähib kivi ümber."
    elif (gesture2 == "kivi" and gesture1 == "käärid"):
        return f"{player2} võidab! Kivi tuhmib või purustab käärid."
    elif (gesture2 == "käärid" and gesture1 == "paber"):
        return f"{player2} võidab! Käärid lõikavad paberit."
    else:
        return "Viik"
    
def main():
    player1 = input("Sisesta esimese mängija nimi: ")
    player2 = input("Sisesta teise mängija nimi: ")

    scores = {player1: 0, player2: 0}
    rounds = 3

    for _ in range(rounds):
        result = play_round(player1, player2)
        print(result)

        if "võidab" in result:
            winner = result.split()[0]
            scores[winner] += 1

        print(f"Aktuaalne skoor: {player1} {scores[player1]} - {scores[player2]} {player2}")
        time.sleep(1)

    print("\nLõplik skoor:")
    print(f"{player1}: {scores[player1]} punkti")
    print(f"{player2}: {scores[player2]} punkti")

if __name__ == "__main__":
    main()








