def ispis_kolegija(kolegij):
    print(f"Kolegij {kolegij['ime']} nosi {kolegij['ects']} ECTS bodova.")
    return kolegij
def get_kolegij(redni_broj, kolegij):
    return f"\t {redni_broj}. {kolegij['ime']}"

def ispis_svih_kolegija(kolegiji):
    print("Popis kolegija: ")
    for kolegij in kolegiji:
        ispis_kolegija(kolegij)