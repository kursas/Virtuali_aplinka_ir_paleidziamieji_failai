# Sukurti paleidžiamąjį failą iš programos, kuri:
# • Leistų vartotojui įvesti metus nuo ir metus iki
# • Atspausdintų visus keliamuosius metus pagal duotą rėžį
# • Paleidžiamasis failas turi turėti norimą ikoną

year1 = int(input("iveskite metus nuo:"))
year2 = int(input("iveskite metus iki:"))
sarasas=list(range(year1,year2))#Sukurtų sąrašą iš skaičių nuo 0 iki 50
print(sarasas)
def count(sarasas):
    for x in range(len(sarasas)):
    # print(sarasas[x])
        if (sarasas[x] % 4 == 0 and sarasas[x] % 100 != 0 or sarasas[x] % 400 == 0):
            print(f"Keliamieji metai!:")
        else:
            print("Nekeliamieji metai!")
    return sarasas
count(sarasas)

