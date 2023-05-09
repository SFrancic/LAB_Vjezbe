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