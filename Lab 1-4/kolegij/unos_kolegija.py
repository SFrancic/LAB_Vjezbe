def unos_kolegija(redni_broj):
    kolegij = {}
    kolegij['ime'] = input(f"Unesite ime {redni_broj}. kolegija:").upper()
    kolegij['ects'] = int(input(f"Unesite broj ects bodova {redni_broj}. kolegija: "))
    return kolegij