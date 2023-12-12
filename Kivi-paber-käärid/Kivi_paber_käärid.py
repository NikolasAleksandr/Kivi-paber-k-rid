import random
import time

def mängi_raund(mängija1, mängija2):
    märgid = ["kivi", "käärid", "paber"]

    print("kivi... käärid... paber... üks... kaks... kolm!")

    märk1 = input(f"{mängija1}, vali märk (kivi/käärid/paber): ").lower()
    while märk1 not in märgid:
        print("Viga: Vali kehtiv märk!")
        märk1 = input(f"{mängija1}, vali märk (kivi/käärid/paber): ").lower()

    märk2 = input(f"{mängija2}, vali märk (kivi/käärid/paber): ").lower()
    while märk2 not in märgid:
        print("Viga: Vali kehtiv märk!")
        märk2 = input(f"{mängija2}, vali märk (kivi/käärid/paber): ").lower()

    print(f"{mängija1} näitas {märk1}")
    print(f"{mängija2} näitas {märk2}")

    if märk1 == märk2:
        return "Viik"
    elif (märk1 == "kivi" and märk2 == "käärid") or \
         (märk1 == "käärid" and märk2 == "paber") or \
         (märk1 == "paber" and märk2 == "kivi"):
        return f"{mängija1} võidab!"
    else:
        return f"{mängija2} võidab!"

def main():
    mängija1 = input("Sisesta esimese mängija nimi: ")
    mängija2 = input("Sisesta teise mängija nimi (või sisesta 'robot' jaoks): ")

    skoor = {mängija1: 0, mängija2: 0}
    raundid = 3

    for _ in range(raundid):
        tulemus = mängi_raund(mängija1, mängija2)
        print(tulemus)

        if "võidab" in tulemus:
            võitja = tulemus.split()[0]
            skoor[võitja] += 1

        print(f"Aktuaalne skoor: {mängija1} {skoor[mängija1]} - {skoor[mängija2]} {mängija2}")
        time.sleep(1)

    print("\nLõplik skoor:")
    print(f"{mängija1}: {skoor[mängija1]} punkti")
    print(f"{mängija2}: {skoor[mängija2]} punkti")

if __name__ == "__main__":
    main()



