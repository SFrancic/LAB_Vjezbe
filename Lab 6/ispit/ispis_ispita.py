def ispis_ispita(ispit):
    print(f"Ispit iz kolegija {ispit['kolegij']['ime']} koji nosi {ispit['kolegij']['ects']} ECTS bodova. \nIspit će se održati {ispit['datum']}.")

def get_ispit(redni_broj, ispit):
    return f"{redni_broj}. {ispit.kolegij.ime}"

def ispis_svih_ispita(ispiti):
    print("Popis svih ispita:")
    for ispit in ispiti:
        ispit.ispis()