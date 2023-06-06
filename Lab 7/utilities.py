def unos_intervala(min, max):
    while True:
        try:
            broj = int(input(f"Unesite broj u intervalu od {min} do {max}: "))

            if broj<min or broj>max:
                raise Exception (f"Unesite broj u intervalu od {min} do {max}: ")


        except ValueError:
            print("Niste unjeli cijeli broj")

        except Exception as e:
            print (e)

        else:
            return broj

from datetime import date


def unos_pozitivnog_cijelog_broja(poruka):
    while True:
        try:
            broj = int(input(poruka))

            if broj < 0:
                raise Exception('Morate upisati cijeli pozitivni broj!')

        except ValueError:
            print('Unijeli ste znak, a ne cijeli broj!')

        except Exception as e:
            print(e)

        else:
            return broj


def unos_pozitivnog_realnog_broja(poruka):
    while True:
        try:
            broj = float(input(poruka))

            if broj < 0:
                raise Exception('Morate upisati pozitivni realni broj!')

        except ValueError:
            print('Unijeli ste znak, a ne realni broj!')

        except Exception as e:
            print(e)

        else:
            return broj


def unos_datuma(poruka):
    while True:
        try:
            dan = int(input(poruka))
            mjesec = int(input(f'Unesite mjesec isteka prodaje: '))
            godina = int(input(f'Unesite godinu isteka prodaje: '))
            datum = date(godina, mjesec, dan)

        except ValueError as e:
            print(e)

        else:
            return datum


def unos_teksta(poruka):
    while True:
        try:
            tekst = input(poruka)

            if not tekst.isalpha():
                raise Exception("Morate unijeti samo slova!")

        except Exception as e:
            print(e)

        else:
            return tekst


def unos_emaila(poruka):
    while True:
        email = input(poruka)

        try:
            email.index("@")

        except ValueError:
            print("Morate unijeti ispravnu email adresu!")

        else:
            return email