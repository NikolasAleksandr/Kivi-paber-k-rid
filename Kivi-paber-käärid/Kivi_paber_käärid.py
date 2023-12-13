import random
import time

def play_round(player1, player2):
    žest = ["kivi", "käärid", "paber"]

    print("kivi... käärid... paber... üks... kaks... kolm!")

    žest1 = input(f"{player1}, loe 'kolm' ja näita žesti (kivi/käärid/paber): ").lower()
    while žest1 not in žest:
        print("Viga: Vali kehtiv žest!")
        žest1 = input(f"{player1}, loe 'kolm' ja näita žesti (kivi/käärid/paber): ").lower()

    žest2 = input(f"{player2}, loe 'kolm' ja näita žesti (kivi/käärid/paber): ").lower()
    while žest2 not in žest:
        print("Viga: Vali kehtiv žest!")
        žest2 = input(f"{player2}, loe 'kolm' ja näita žesti (kivi/käärid/paber): ").lower()

    print(f"{player1} näitas {žest1}")
    print(f"{player2} näitas {žest2}")

    if (žest1 == "paber" and žest2 == "kivi"):
        return f"{player1} võidab! Paber mähib kivi ümber."
    elif (žest1 == "kivi" and žest2 == "käärid"):
        return f"{player1} võidab! Kivi tuhmib või purustab käärid."
    elif (žest1 == "käärid" and žest2 == "paber"):
        return f"{player1} võidab! Käärid lõikavad paberit."
    elif (žest2 == "paber" and žest1 == "kivi"):
        return f"{player2} võidab! Paber mähib kivi ümber."
    elif (žest2 == "kivi" and žest1 == "käärid"):
        return f"{player2} võidab! Kivi tuhmib või purustab käärid."
    elif (žest2 == "käärid" and žest1 == "paber"):
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








