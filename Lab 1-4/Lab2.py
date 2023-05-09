from datetime import date

kolegij = {}
kolegij['ime'] = input("Unesite ime kolegija: ").upper()
kolegij['ects'] = int(input("Unesite broj ECTS bodova: "))
#print("Kolegij", kolegij['ime'], "nosi", kolegij['ects'], "ECTS bodova")

ispit = {}
dan = int(input("Unesite dan ispita:"))
mjesec = int(input("Unesite mjesec ispita:"))
godina = int(input("Unesite godinu ispita:"))
ispit['kolegij'] = kolegij
ispit['datum'] = date(godina, mjesec, dan)
#print("Kolegij", ispit['kolegij']['ime'], "nosi", ispit['kolegij']['ects'], "ECTS bodova")
#print("Datum ispita je:", ispit['datum'])

student = {}
student['ispit'] = ispit
student['ime'] = input("Unesite ime studenta: ").title()
student['prezime'] = input("Unesite prezime studenta: ").title()
print("Student", student['ime'], student['prezime'], "je prijavio ispit iz kolegija", student['ispit']['kolegij']['ime'], "koji nosi", student['ispit']['kolegij']['ects'], "ECTS bodova.")
print("Datum ispita je: ", student['ispit']['datum'])
