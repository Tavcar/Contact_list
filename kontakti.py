# -*- coding: utf-8 -*-

class Kontakt(object):
    def __init__(self, ime, telefonska_st, email):
        self.ime = ime
        self.telefonska_st = telefonska_st
        self.email = email

def main():
    kontakti_file = open("kontakti.txt", "r+")
    kontakti_list = []

    for kontakt in kontakti_file:
        ime, telefonska_st, email = kontakt.split(";")

        kontakt = Kontakt(ime, telefonska_st, email)
        kontakti_list.append(kontakt)

    izbira = raw_input("Želite:\na) ogledati list kontaktov,\nb) dodati nov kontakt,\nc) urediti kontakt ali\nd) izbrisati kontakt?\n(a, b, c ali d): ")
    print(" ")

    if izbira.lower() == "a":
        izpis_kontaktov(kontakti_list)

    elif izbira.lower() == "b":
        dodaj_kontakt(kontakti_list)

    elif izbira.lower() == "c":
        uredi_kontakt(kontakti_list)

    elif izbira.lower() == "d":
        izbris_kontakta(kontakti_list)

    shrani(kontakti_list, kontakti_file)
    kontakti_file.close()

def shrani(kontakti_list, kontakti_file):
    kontakti_file.close()
    kontakti_file = open("kontakti.txt", "w")
    for kontakt in kontakti_list:
        kontakti_file.write(kontakt.ime + ";" + kontakt.telefonska_st + ";" + kontakt.email)


def izpis_kontaktov(kontakti_list):
    for kontakt in kontakti_list:
        print "Ime: " + kontakt.ime
        print "tel. št.: " + kontakt.telefonska_st
        print "e-mail: " + kontakt.email


def dodaj_kontakt(kontakti_list):
    ime = raw_input("Ime kontakta: ")
    telefonska_st = raw_input("Telefonska številka: ")
    email = raw_input("e-pošta: ")

    oseba = Kontakt(ime="\n" + ime, telefonska_st=telefonska_st, email=email)
    kontakti_list.append(oseba)
    print "Kontakt dodan."


def uredi_kontakt(kontakti_list):
    for kontakt in kontakti_list:
        print kontakt.ime
        dopisi = raw_input("Želite urediti del kontakta? (ime/stevilka/email/ne): ")

        if dopisi.lower() == "ime":
            print "Ime: " + kontakt.ime
            kontakt.ime = raw_input("Ime: ")

        elif dopisi.lower() == "stevilka":
            print "Telefonska številka: " + kontakt.telefonska_st
            kontakt.telefonska_st = raw_input("Nova telefonska številka: ")

        elif dopisi.lower() == "email":
            print "e-mail: " + kontakt.email
            kontakt.email = raw_input("Novi e-mail: ") + "\n"


def izbris_kontakta(kontakti_list):
    for kontakt in kontakti_list:
        print kontakt.ime
        izbris = raw_input("Želite izbrisati kontakt? (da/ne) ")
        if izbris.lower() == "da":
            kontakti_list.remove(kontakt)


if __name__ == "__main__":
    main()
    print("Konec")