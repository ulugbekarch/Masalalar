# a = float(input("Kvadratning tomonini kiriting: "))
# p = 4 * a
# print(f"Kvadratning perimetri: {int(p)}")

# a = float(input(" Kvadratning tomoni: "))
# S = a * a
# print(f"Kvadratning yuzasi: {int(S)} ")

# a = float(input("To'g'ri to'rtburchakning a tomoni: "))
# b = float(input("To'g'ri to'rtburchakning b tomoni: "))
# p = 2 * (a+b)
# S = a * b
# print(f"To'g'ri to'rtburchakning perimetri: {int(p)}")
# print(f"To'g'ri to'rtburchakning yuzasi: {int(S)}")


while True:
    try:
      a = float(input("aylananing diametirini kiriting: "))
      L = 3.14 * a
      print(f"aylana uzunligi: {int(L)}")
      break
    except ValueError:
      print("raqam kiritng")

hisob = 0
while hisob < 10:
    try:
        a = float(input("aylananing diametirini kiriting: "))
        L = 3.14 * a
        print(f"aylana uzunligi: {int(L)}")
        hisob += 1

        if hisob == 5:
            print("diqqat 5 ta urunish qoldi.")
    except ValueError:
        print("Faqat raqam kiriitng")

print("10 ta imkoniyat tugati")

limit = 10

while True:
    hisob = 0

    while hisob < limit:
        try:
            a = float(input("aylananing diametirini kiriting: "))
            L = 3.14 * a
            print(f"aylana uzunligi: {int(L)}")
            hisob += 1

            if hisob = 5:
                print("yana 5 ta urunish qoldi")
        except ValueError:
            print("xato raqam kiriting")
    print(f"{limit} ta hisboshlash tugadi.")
    promokod = int("davom etish uchun promkod kiriting: ")
    if promokod == "salom":
        limit = 20
        print("promokod togri sizga yana 20 ta imkoniyat berildi")
    else:
        print("promkod xato")
        break