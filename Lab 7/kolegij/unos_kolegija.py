from .kolegij import Kolegij
def unos_kolegija(redni_broj):
    ime = input(f"Upisite ime {redni_broj}. kolegija: ")
    ECTS = int(input(f"Unesite broj ECTS bodova {redni_broj}. kolegija: "))
    return Kolegij(ime, ECTS)