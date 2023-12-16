from random import *

žest = ["kivi", "käärid", "paber"]

player1 = input("Sisesta esimese mängija nimi: ")
player2 = input("Sisesta teise mängija nimi: ")

print("kivi... käärid... paber... üks... kaks... kolm!")

scores = {player1: 0, player2: 0}
rounds = 3

for _ in range(rounds):
    print(f"\nRound {_ + 1} algab!")

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

    if (žest1 == "paber" and žest2 == "kivi") or (žest1 == "kivi" and žest2 == "käärid") or (žest1 == "käärid" and žest2 == "paber"):
        print(f"{player1} võidab! {žest1} mähib {žest2} ümber.")
        scores[player1] += 1
    elif (žest2 == "paber" and žest1 == "kivi") or (žest2 == "kivi" and žest1 == "käärid") or (žest2 == "käärid" and žest1 == "paber"):
        print(f"{player2} võidab! {žest2} mähib {žest1} ümber.")
        scores[player2] += 1
    else:
        print("Viik! Mäng mängitakse uuesti.")

    print(f"Aktuaalne skoor: {player1} {scores[player1]} - {scores[player2]} {player2}")

print("\nLõplik skoor:")
print(f"{player1}: {scores[player1]} punkti")
print(f"{player2}: {scores[player2]} punkti")











