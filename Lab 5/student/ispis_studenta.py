from ispit import ispis_ispita

def ispis_studenta(student):
    print(f"Student {student['ime']} {student['prezime']} je prijavio: ")
    ispis_ispita(student['ispit'])

def ispis_svih_studenta(studenti):
    print("Popis studenata: ")
    for student in studenti:
        ispis_studenta(student)
