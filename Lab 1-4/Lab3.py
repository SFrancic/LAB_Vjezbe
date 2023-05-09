from datetime import date

kolegiji = []
ispiti = []
studenti = []

broj_kolegija = int(input("Unesite broj kolegija: "))
for i in range(1, broj_kolegija+1):
    kolegij = {}
    kolegij['ime'] = input(f"Unesite ime {i}. kolegija:").upper()
    kolegij['ects'] = int(input(f"Unesite broj ects bodova {i}. kolegija: "))
    kolegiji.append(kolegij)

#print("Popis svih kolegija: ")
#for kolegij in kolegiji:
#    print(f"\tKolegij {kolegij['ime']} nosi {kolegij['ects']} ECTS bodova")


broj_ispita = int(input("Unesite broj ispita: "))
for i in range(1, broj_ispita+1):
    ispit = {}
    for j, kolegij in enumerate(kolegiji, start=1):
        print(f"\t{j}. {kolegij['ime']}")

    odabrani_kolegij = int(input("Odaberite kolegij: "))
    ispit['kolegij'] = kolegiji[odabrani_kolegij-1]

    dan = int(input(f"Unesite dan {i}. ispita: "))
    mjesec = int(input(f"Unesite mjesec {i}. ispita: "))
    godina = int(input(f"Unesite godinu {i}. ispita: "))
    ispit['datum'] = date(godina, mjesec, dan)
    ispiti.append(ispit)

#print("Popis svih ispita: ")
#for ispit in ispiti:
#    print(f"Kolegij {ispit['kolegij']['ime']} koji nosi {ispit['kolegij']['ects']} ECTS bodova održat će se {ispit['datum']} ")

broj_studenata = int(input("Unesite broj studenata: "))
for i in range(1, broj_studenata+1):
    student = {}
    student['ime'] = input(f"Unesite ime {i}. studenta: ").capitalize()
    student['prezime'] = input(f"Unesite prezime {i}. studenta: ").capitalize()

    print("Popis ispita: ")
    for j, ispit in enumerate(ispiti, start=1):
        print(f"\t{j}. {ispit['kolegij']['ime']} {ispit['datum']}")
    odabrani_ispit = int(input("Odaberite ispit: "))
    student['ispit'] = ispiti[odabrani_ispit-1]
    studenti.append(student)

print("Popis studenata:")
for student in studenti:
    print(f"Student {student['ime']} {student['prezime']} je prijavio ispit iz kolegija {student['ispit']['kolegij']['ime']} koji nosi {student['ispit']['kolegij']['ects']} ECTS bodova. ")
