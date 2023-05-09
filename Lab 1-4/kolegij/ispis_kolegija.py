def ispis_kolegija(kolegij):
    print(f"Kolegij {kolegij['ime']} nosi {kolegij['ects']} bodova.")
    return kolegij
def get_kolegij(redni_broj, kolegij):
    return f"\t {redni_broj}. {kolegij['ime']}"
