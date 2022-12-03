import csv
import datetime
import hashlib
import random

def main():
    #combine_csvs('imiona_meskie.csv', 'imiona_zenskie.csv', 'imiona.csv', 'IMIĘ_PIERWSZE')
    #combine_csvs('nazwiska_meskie.csv', 'nazwiska_zenskie.csv', 'nazwiska.txt', 'Nazwisko aktualne')
    #generateSqlNames(200, 1)
    #getStreetsFromCity('0974133')
    #generateSqlAdresses(100, 1)
    #generateSqlContactInfo(200, 1)
    #generateSqlFreeDates(50)
    #generateSqlDeliveryCompany(25, 1)
    #generateSqlCategories()
    #generateSqlProductsDeliveries()
    #generateSqlWorkers(10, 1)
    #generateSqlWorkersHours(100)
    #generateSqlPasswords(200)
    #generateSqlBaskets(100)
    #generateSqlUsersBaskets(200)
    #generateSqlWarehouse()
    #generateSqlDeliveryMethods()
    #generateSqlPaymentMethods()
    #generateSqlAvaibleRegions()
    #generateSqlRemovedProducts(3)
    #generateSqlPromotions(2)
    #generateSqlOrders(10)
    #generateSqlSentOrders(5)
    #shortestNames()
    #filipContacts(303, 50)
    #filipEmployeesDetails(101)
    #filipProducts()
    #filipReklamacje(50)
    #filipSuppilerDetails(50)
    #filipOrders(100)
    #filipOrderDetials(100)
    #lysyUczniowie(200)
    #lysyNauczyciele(10)
    #lysyOpiekunowie(350)
    #kubaStock(250)
    #kubaSuppliers(250)
    #kubaHistory(250)
    #kubaEmployees(250)
    #kubaShipmentAdress(250)
    #kubaCunstactAdress(250)
    #kubaCartProducts(250)
    #kubaCart(250)
    #kubaCouriers()
    #kubaProducts()
    #kubaCustomers(250)
    #kubaOrders(250)
    kubaOrderDetails(250)
    pass


def combine_csvs(first, second, output, firstRow):
    with open(first, 'r', encoding='utf-8') as imiona_meskie:
        with open(second, 'r', encoding='utf-8') as imiona_zenskie:
            with open(output, 'w', encoding='utf-8') as imiona:
                
                reader_m = csv.reader(imiona_meskie)
                reader_z = csv.reader(imiona_zenskie)

                for row in reader_m:
                    # skip header
                    if row[0] == firstRow:
                        continue
                    # write to file
                    imiona.write(row[0] + '\n')

                for row in reader_z:
                    if row[0] == firstRow:
                        continue
                    imiona.write(row[0] + '\n')


def getStreetsFromCity(city):
    # get streets from city
    with open('ulice.csv', 'r', encoding='utf-8') as ulice:
        with open('ulice.txt', 'w', encoding='utf-8') as output:
            reader = csv.reader(ulice, delimiter=';')
            for row in reader:
                try:
                    if row[4] == city:
                        if row[6] == 'ul.' or row[6] == 'pl.':
                            output.write(row[6] + ' ' + row[7]+'\n')
                except:
                    pass


def getRandomName():
    # read first name from imiona.txt and last name from nazwiska.txt
    with open('imiona.txt', 'r', encoding='utf-8') as imiona:
        with open('nazwiska.txt', 'r', encoding='utf-8') as nazwiska:
            imiona_list = imiona.readlines()
            nazwiska_list = nazwiska.readlines()
            imie = random.choice(imiona_list).strip()
            nazwisko = random.choice(nazwiska_list).strip()
            # capitalize first letters of names
            imie = imie[0].upper() + imie[1:].lower()
            nazwisko = nazwisko[0].upper() + nazwisko[1:].lower()
            return imie, nazwisko


def getRandomStreet():
    # get random street from ulice.txt
    with open('ulice.txt', 'r', encoding='utf-8') as ulice:
        ulice_list = ulice.readlines()
        ulica = random.choice(ulice_list).strip()
        return ulica


def getRandomPhoneNumber():
    # generate random phone number
    return f'48{random.randint(100000000, 999999999)}'


def getRandomEmail():
    # generate random email
    # example email: user12345@gmail.com
    number = random.randint(10000, 99999999)
    return  f'user{number}@gmail.com'


def getRandomDateInFuture():
    # generate random date in future
    # example date: 2021-12-31
    year = random.randint(2023, 2026)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f'{year}-{month}-{day}'


def getRandomCompanyName():
    # generate random company name
    adjectives = ['Świetny', 'Polski', 'Dobry', 'Nowoczesny', 'Mały', 'Szybki']
    colors = ['Czerwony', 'Niebieski', 'Zielony', 'Żółty', 'Pomarańczowy', 'Fioletowy', 'Czarny', 'Biały', 'Szary', 'Brązowy']
    items = ['Dywan', 'Stół', 'Laptop', 'Telefon', 'Zegarek', 'Kubek', 'Produkt', 'Mistrz', 'Pomocnik']
    animals = ['Kot', 'Pies', 'Koń', 'Królik', 'Słoń', 'Krokodyl', 'Kangur', 'Koala', 'Orzeł', 'Żółw']
    # example company name: Czerwony Smok
    # select random color or adjective
    firstPart = random.choice(colors + adjectives)
    # select random item or animal
    secondPart = random.choice(items + animals)
    # 10% to add at the end 'ex'
    if random.randint(1, 10) == 1:
        secondPart += 'ex'
    return f'{firstPart} {secondPart}'


def generateSqlNames(number, firstIndex):
    # generate sql file with random names
    # example query: INSERT INTO Uzytkownik (Id, Imie, Nazwisko) VALUES (1, 'Jan', 'Kowalski')
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            imie, nazwisko = getRandomName()
            output.write(f"INSERT INTO Uzytkownik (Id, Imie, Nazwisko) VALUES ({firstIndex+i}, '{imie}', '{nazwisko}');\n")

def generateSqlAdresses(number, firstIndex):
    # example query: INSERT INTO Adres (Id, Miasto, Ulica, NrBudynku, KodPocztowy, Imie, Nazwisko, NrTelefonu, dodatkoweinformacje) VALUES (1, 'Rzeszów', 'ul. Kolejowa', '1', '35-001', 'Jan', 'Nowak', '123456789', 'blok');
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            imie, nazwisko = getRandomName()
            ulica = getRandomStreet()
            nrBudynku = random.randint(1, 100)
            # kodPcztowy must be in format 35-000
            kodPocztowy = f'35-{random.randint(0, 999):03}'
            nrTelefonu = getRandomPhoneNumber()
            dodatkoweInformacje = ''
            if random.randint(1, 10) == 1:
                dodatkoweInformacje = 'blok'
            elif random.randint(1, 10) <= 2:
                dodatkoweInformacje = 'firma'
            output.write(f"INSERT INTO Adres (Id, Miasto, Ulica, NrBudynku, KodPocztowy, Imie, Nazwisko, NrTelefonu, dodatkoweinformacje) VALUES ({firstIndex+i}, 'Rzeszów', '{ulica}', '{nrBudynku}', '{kodPocztowy}', '{imie}', '{nazwisko}', '{nrTelefonu}', '{dodatkoweInformacje}');\n")


def generateSqlContactInfo(number, firstIndex):
    # example query: INSERT INTO DaneKontaktowe (IdUzytkownika, [e-mail], NrTelefonu) VALUES (1, 'user12345@gmail.com', '48123456789');
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            email = getRandomEmail()
            nrTelefonu = getRandomPhoneNumber()
            output.write(f"INSERT INTO DaneKontaktowe (IdUzytkownika, [e-mail], NrTelefonu) VALUES ({firstIndex+i}, '{email}', '{nrTelefonu}');\n")


def generateSqlFreeDates(number):
    # example query: INSERT INTO DniWolne (Data) Values ('2021-12-31');
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            data = getRandomDateInFuture()
            output.write(f"INSERT INTO DniWolne (Data) Values ('{data}');\n")


def generateSqlDeliveryCompany(number, firstIndex):
    # example query: INSERT INTO Dostawca (Id, Nazwa, IdAdresu) VALUES (1, 'Czerwony Smok', 201);
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            nazwa = getRandomCompanyName()
            idAdresu = random.randint(201, 300)
            output.write(f"INSERT INTO Dostawca (Id, Nazwa, IdAdresu) VALUES ({firstIndex+i}, '{nazwa}', {idAdresu});\n")


def generateSqlCategories():
    categories = ['Książki', 'Filmy', 'Muzyka', 'Gry', 'Elektronika', 'Sport', 'Moda', 'Dom', 'Zdrowie', 'Motoryzacja', 'Zabawki', 'Inne']
    # example query: INSERT INTO Kategoria (Id, Nazwa) VALUES (1, 'Książki');
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(len(categories)):
            output.write(f"INSERT INTO Kategoria (Id, Nazwa) VALUES ({i+1}, '{categories[i]}');\n")


def genereteSqlProducts():
    products = ['Książka', 'Film', 'Płyta', 'Gra', 'Telefon', 'Buty', 'Meble', 'Zegarek', 'Laptop', 'Samochód', 'Zabawka']
    # example query: INSERT INTO Produkt (Id, Nazwa, IdKategorii, Cena) VALUES (1, 'Książka', 1, 20.99);
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(len(products)):
            nazwa = products[i]
            idKategorii = random.randint(1, 12)
            cena = random.randint(1, 1000) + random.randint(0, 99) / 100
            output.write(f"INSERT INTO Produkt (Id, Nazwa, IdKategorii, Cena) VALUES ({i+1}, '{nazwa}', {idKategorii}, {cena});\n")


def generateSqlProductsDeliveries():
    # example query: INSERT INTO DostawyProduktow (IdDostawcy, IdProduktu) VALUES (1, 1);
    # for deliveries form 1 to 25 assign random product from 1 to 11
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(1, 26):
            idProduktu = random.randint(1, 11)
            output.write(f"INSERT INTO DostawyProduktow (IdDostawcy, IdProduktu) VALUES ({i}, {idProduktu});\n")



def generateSqlWorkers(number, firstIndex):
    # example query: INSERT INTO Pracownik (IdUzytkownika, Stanowisko, Dzial) VALUES (1, 'Kierownik', 'Sprzedaż');
    stanowiska = ['Kierownik', 'Sprzedawca', 'Magazynier', 'Kierowca']
    dzialy = ['Sprzedaż', 'Magazyn', 'Dostawa']
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            idUzytkownika = random.randint(1, 200)
            stanowisko = stanowiska[random.randint(0, 3)]
            dzial = dzialy[random.randint(0, 2)]
            output.write(f"INSERT INTO Pracownik (IdUzytkownika, Stanowisko, Dzial) VALUES ({firstIndex+i}, '{stanowisko}', '{dzial}');\n")


def generateSqlWorkersHours(number):
    # example query: INSERT INTO HarmonogramPracy (IdPracownika, DataRozpoczeciaZmiany, DataZakonczeniaZmiany) VALUES (1, '2021-12-31 08:00:00', '2021-12-31 16:00:00');
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            idPracownika = random.randint(1, 10)
            dataRozpoczeniaZmiany = getRandomDateInFuture()
            dataRozpoczeniaZmiany = datetime.datetime.strptime(dataRozpoczeniaZmiany, '%Y-%m-%d') + datetime.timedelta(hours=random.randint(1, 23))
            # add between 6 and 8 hours to start date
            dataZakonczeniaZmiany = dataRozpoczeniaZmiany + datetime.timedelta(hours=random.randint(6, 8))
            output.write(f"INSERT INTO HarmonogramPracy (IdPracownika, DataRozpoczeciaZmiany, DataZakonczeniaZmiany) VALUES ({idPracownika}, '{dataRozpoczeniaZmiany}', '{dataZakonczeniaZmiany}');\n")


def generateSqlPasswords(number):
    # examle query: INSERT INTO Haslo (IdUzytkownika, Haslo) VALUES (1, '!@sdk2#adj$1as3');
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            idUzytkownika = i+1
            # use md5 to generate random password
            haslo = hashlib.md5(str(random.randint(1, 1000000000)).encode('utf-8')).hexdigest()
            output.write(f"INSERT INTO Haslo (IdUzytkownika, Haslo) VALUES ({idUzytkownika}, '{haslo}');\n")


def generateSqlBaskets(number):
    # example query: INSERT INTO Koszyk (Id, IdProduktu, Ilosc) VALUES (1, 1, 1);
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            id = i+1
            # for each basket add random number of products from 1 to 10
            for j in range(random.randint(1, 10)):
                idProduktu = random.randint(1, 11)
                ilosc = random.randint(1, 10)
                output.write(f"INSERT INTO Koszyk (Id, IdProduktu, Ilosc) VALUES ({id}, {idProduktu}, {ilosc});\n")


def generateSqlUsersBaskets(number):
    # example query: INSERT INTO KoszykUzytkownika (IdUzytkownika, IdKoszyka) VALUES (1, 1);
    # for each user allign basket
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            idUzytkownika = i+1
            idKoszyka = i+1
            output.write(f"INSERT INTO KoszykUzytkownika (IdUzytkownika, IdKoszyka) VALUES ({idUzytkownika}, {idKoszyka});\n")


def generateSqlWarehouse():
    # example query: INSERT INTO Magazyn (IdProduktu, Ilosc) VALUES (1, 10);
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(1, 12):
            ilosc = random.randint(0, 20)
            output.write(f"INSERT INTO Magazyn (IdProduktu, Ilosc) VALUES ({i}, {ilosc});\n")


def generateSqlDeliveryMethods():
    # example query: INSERT INTO MetodaDostawy (Id, Nazwa, Cena) VALUES (1, 'Kurier', 10.00);
    metody = ['Kurier', 'Poczta', 'Odbiór osobisty', 'Paczkomat', 'Paczka w ruchu']
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(1, 6):
            nazwa = metody[i-1]
            cena = random.randint(0, 20)
            output.write(f"INSERT INTO MetodaDostawy (Id, Nazwa, Cena) VALUES ({i}, '{nazwa}', {cena});\n")


def generateSqlPaymentMethods():
    # example query: INSERT INTO MetodaPlatnosci (Id, Nazwa, Oplata) VALUES (1, 'Karta płatnicza', 0.00);
    metody = ['Karta płatnicza', 'Przelew', 'Gotówka', 'Płatność online']
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(1, 5):
            nazwa = metody[i-1]
            oplata = random.randint(0, 20)
            output.write(f"INSERT INTO MetodaPlatnosci (Id, Nazwa, Oplata) VALUES ({i}, '{nazwa}', {oplata});\n")


def generateSqlAvaibleRegions():
    # example query: INSERT INTO ObslugiwaneRegiony (KodPocztowy) VALUES ('35-000');
    # from 35-000 to 35-399
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(400):
            kodPocztowy = f'35-{i:03}'
            output.write(f"INSERT INTO ObslugiwaneRegiony (KodPocztowy) VALUES ('{kodPocztowy}');\n")


def getRandomDateInPast():
    # generate random date in past
    year = random.randint(2020, 2021)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f'{year}-{month:02}-{day:02}'


def getRandomDateInBigPast():
    # generate random date in past
    year = random.randint(1980, 2000)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f'{year}-{month:02}-{day:02}'


def generateSqlRemovedProducts(number):
    # example query: INSERT INTO ProduktyWycofane (IdProduktu, DataWycofania) VALUES (1, '2020-01-01');
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            idProduktu = random.randint(1, 11)
            dataWycofania = getRandomDateInPast()
            output.write(f"INSERT INTO ProduktyWycofane (IdProduktu, DataWycofania) VALUES ({idProduktu}, '{dataWycofania}');\n")


def generateSqlPromotions(number):
    # example query: INSERT INTO Promocja (IdProduktu, ProcentCenyPoczatkowej) VALUES (1, 10);
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            idProduktu = random.randint(1, 11)
            procentCenyPoczatkowej = random.randint(1, 100)
            output.write(f"INSERT INTO Promocja (IdProduktu, ProcentCenyPoczatkowej) VALUES ({idProduktu}, {procentCenyPoczatkowej});\n")


def generateSqlOrders(number):
    # example query: INSERT INTO Zamowienie (Id, IdUzytkownika, IdKoszyka, IdMetodaDostawy, IdAdresDostawy, IdMetodaPlatnosci, IdPracownik) VALUES (1, 1, 1, 1, 1, 1, 1);
    # IdPracownika from 1 to 10
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            id = i+1
            idUzytkownika = random.randint(1, 200)
            idKoszyka = random.randint(1, 100)
            idMetodaDostawy = random.randint(1, 5)
            idAdresDostawy = random.randint(1, 200)
            idMetodaPlatnosci = random.randint(1, 4)
            idPracownik = random.randint(1, 10)
            output.write(f"INSERT INTO Zamowienie (Id, IdUzytkownika, IdKoszyka, IdMetodaDostawy, IdAdresDostawy, IdMetodaPlatnosci, IdPracownik) VALUES ({id}, {idUzytkownika}, {idKoszyka}, {idMetodaDostawy}, {idAdresDostawy}, {idMetodaPlatnosci}, {idPracownik});\n")


def generateSqlSentOrders(number):
    # example query: INSERT INTO Wysylka (IdZamowienia, data) VALUES (1, '2020-01-01');
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            idZamowienia = random.randint(1, 10)
            data = getRandomDateInPast()
            output.write(f"INSERT INTO Wysylka (IdZamowienia, data) VALUES ({idZamowienia}, '{data}');\n")


def shortestNames():
    # find in imiana.txt shortest names
    with open('imiona.txt', 'r', encoding='utf-8') as input:
        names = input.readlines()
        names = [name.strip() for name in names]
        names = [name for name in names if len(name) <= 1]
        print(names)


def filipContacts(firstIndex, number):
    # example query: (id, phoneNumber, fax, email) - (1, '123456789', '0-000-000-0000', 'aaa@gmail.com')
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            id = firstIndex+i+1
            phoneNumber = random.randint(100000000, 999999999)
            fax = f'{random.randint(0, 9)}-{random.randint(0, 999):03}-{random.randint(0, 999):03}-{random.randint(0, 9999):04}'
            imie, nazwisko = getRandomName()
            email = imie + '.' + nazwisko + '@gmail.com'
            output.write(f"({id}, '{phoneNumber}', '{fax}', '{email}'),\n")


def filipEmployeesDetails(number):
    # (1,'filip','duda','2010-11-23',2000,'IT','2010-11-23'), id, imie. nazwisko, dataZatrudnienia, wy[plata,department, dataUrodzina
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            id = i+1
            imie, nazwisko = getRandomName()
            dataZatrudnienia = getRandomDateInPast()
            wyplata = random.randint(1000, 10000)
            departments = ['IT', 'HR', 'Marketing', 'Sales', 'Finance']
            department = random.choice(departments)
            dataUrodzenia = getRandomDateInBigPast()
            output.write(f"({id},'{imie}','{nazwisko}','{dataZatrudnienia}',{wyplata},'{department}','{dataUrodzenia}'),\n")


def filipRandomWord():
    # generate and return random word
    slowa = ['jablko', 'banan', 'gruszka', 'pomidor', 'marchewka', 'papryka', 'ogorek', 'cebula', 'czosnek', 'ziemniak',
             'kalafior', 'brokul', 'jajko', 'mleko', 'ser', 'chleb', 'maslo', 'pierogi', 'zupa', 'makaron', 'woda', 'kawa',
             'herbata', 'cukier', 'sok', 'sok pomaranczowy', 'sok jablkowy', 'sok malinowy', 'sok winogronowy', 'sok truskawkowy',
             'sok brzoskwiniowy', 'sok jagodowy', 'sok gruszkowy', 'sok cytrynowy', 'sok kaki', 'sok z brzoskwiniami',
             'sok z malinami', 'sok z winogronami', 'sok z truskawkami', 'sok z jagodami', 'sok z gruszkami', 'sok z kaki',
             'sok z cytryny', 'sok z pomaranczy', 'sok z jablk', 'sok z malin', 'sok z winogron', 'sok z truskawek',
             'sok z brzoskwin', 'sok z jagod', 'sok z gruszek', 'sok z kaki', 'sok z cytryn', 'sok z pomarancz', 'kompot',
             'kompot z brzoskwiniami', 'kompot z malinami', 'kompot z winogronami', 'kompot z truskawkami', 'kompot z jagodami',
             'kompot z gruszkami', 'kompot z kaki', 'kompot z cytryny', 'kompot z pomaranczy', 'kompot z jablk', 'kompot z malin']
    return random.choice(slowa)


def filipFakturki(number):
    # id, data tytul, opis, cenaBrutto, cenaNetto, vat = 23
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            id = i+1
            data = getRandomDateInPast()
            tytul = filipRandomWord()
            opis = "dostawa " + tytul
            cenaBrutto = random.randint(100, 10000)
            vat = 23
            cenaNetto = round(cenaBrutto / (1 + vat / 100), 2)
            output.write(f"({id}, '{data}', '{tytul}','{opis}',{cenaBrutto},{cenaNetto},{vat}),\n")


def filipReklamacje(number):
    # id, tytul, opis, isSolved, data, id, id
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            id = i+1
            tytul = "Brak zamowienia"
            opis = "Brak zamowienia " + filipRandomWord()
            isSolved = random.randint(0, 1)
            data = getRandomDateInPast()
            output.write(f"({id},'{tytul}','{opis}',{isSolved},'{data}',{id},{id}),\n")


def filipProducts():
    # id, productName, unitPrice, expirationDate, WareHouseId, ProductsCategoriesId, SuppliersId, TerritoriesId
    with open('output.txt', 'w', encoding='utf-8') as output:
        produkty = ['jablko', 'banan', 'gruszka', 'pomidor', 'marchewka', 'papryka', 'ogorek', 'cebula', 'czosnek', 'ziemniak',
                'kalafior', 'brokul', 'jajko', 'mleko', 'ser', 'chleb', 'maslo', 'pierogi', 'zupa', 'makaron', 'woda', 'kawa',
                'herbata', 'cukier', 'sok', 'sok pomaranczowy', 'sok jablkowy', 'sok malinowy', 'sok winogronowy', 'sok truskawkowy',
                'sok brzoskwiniowy', 'sok jagodowy', 'sok gruszkowy', 'sok cytrynowy', 'sok kaki', 'sok z brzoskwiniami',
                'sok z malinami', 'sok z winogronami', 'sok z truskawkami', 'sok z jagodami', 'sok z gruszkami', 'sok z kaki',
                'sok z cytryny', 'sok z pomaranczy', 'sok z jablk', 'sok z malin', 'sok z winogron', 'sok z truskawek',
                'sok z brzoskwin', 'sok z jagod', 'sok z gruszek', 'sok z kaki', 'sok z cytryn', 'sok z pomarancz', 'kompot',
                'kompot z brzoskwiniami', 'kompot z malinami', 'kompot z winogronami', 'kompot z truskawkami', 'kompot z jagodami',
                'kompot z gruszkami', 'kompot z kaki', 'kompot z cytryny', 'kompot z pomaranczy', 'kompot z jablk', 'kompot z malin']
        for productName in produkty:
            id = produkty.index(productName) + 1
            unitPrice = random.randint(1, 100)
            expirationDate = getRandomDateInFuture()
            WareHouseId = id
            ProductsCategoriesId = random.randint(1, 5)
            SuppliersId = random.randint(1, 50)
            TerritoriesId = random.randint(1, 50)
            output.write(f"({id},'{productName}',{unitPrice},'{expirationDate}',{WareHouseId},{ProductsCategoriesId},{SuppliersId},{TerritoriesId}),\n")


def filipSuppilerDetails(number):
    # id, companyName, NIP, REGON, homePage
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            id = i+1
            companyName = getRandomCompanyName()
            NIP = random.randint(1000000000, 9999999999)
            REGON = random.randint(100000000, 999999999)
            homePage = "www." + companyName.replace(' ', '_') + ".com"
            output.write(f"({id},'{companyName}',{NIP},{REGON},'{homePage}'),\n")


def filipOrders(number):
    # id, orderDate, shippedDate, shipAddress, CustomerId, EmployeesId, InvoiceId
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            id = i+1
            orderDate = getRandomDateInPast()
            shippedDate = getRandomDateInFuture()
            miasta = ['Warszawa', 'Krakow', 'Wroclaw', 'Poznan', 'Gdansk', 'Szczecin', 'Bydgoszcz', 'Lublin', 'Katowice', 'Bialystok']
            shipAddress = getRandomStreet() + " " + str(random.randint(1, 100)) + ", " + random.choice(miasta)
            CustomerId = random.randint(1, 100)
            EmployeesId = random.randint(1, 100)
            InvoiceId = id
            output.write(f"({id},'{orderDate}','{shippedDate}','{shipAddress}',{CustomerId},{EmployeesId},{InvoiceId}),\n")


def filipOrderDetials(number):
    # orderId, ProductId, quantity, discount unitPrice
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            orderId = i+1
            ProductId = random.randint(1, 66)
            quantity = random.randint(100, 1000)
            discount = random.randint(0, 5)
            unitPrice = random.randint(5, 100)
            output.write(f"({orderId},{ProductId},{quantity},{discount},{unitPrice}),\n")


def lysyUczniowie(number):
    # example query: INSERT INTO public.uczniowie (id_ucznia, imie, drugie_imie, nazwisko, plec, telefon, pesel, email) VALUES (1, 'Jan', 'Piotr', 'Kowalski', 'M', '123-456-789', '12345678901', 'jan.piotr@gmail.com');
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            id_ucznia = i+1
            imie, nazwisko = getRandomName()
            drugie_imie, _ = getRandomName()
            plec = random.choice(['M', 'K'])
            telefon = getRandomPhoneNumber()
            pesel =  random.randint(10000000000, 99999999999)
            email = imie.lower() + "." + drugie_imie.lower() + "@" + nazwisko.lower() + ".com"
            output.write(f"INSERT INTO public.uczniowie (id_ucznia, imie, drugie_imie, nazwisko, plec, telefon, pesel, email) VALUES ({id_ucznia}, '{imie}', '{drugie_imie}', '{nazwisko}', '{plec}', '{telefon}', '{pesel}', '{email}');\n")


def lysyNauczyciele(number):
    # example query: INSERT INTO public.nauczyciele (id_nauczyciela, imie, drugie_imie, nazwisko, plec, telefon, pesel, email) VALUES (1, 'Jan', 'Krzysztof', 'Duda', 'M', '123-456-789', '12345678901', 'jan.krzysztof@gmail.com');
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            id_nauczyciela = i+1
            imie, nazwisko = getRandomName()
            drugie_imie, _ = getRandomName()
            plec = random.choice(['M', 'K'])
            telefon = getRandomPhoneNumber()
            pesel =  random.randint(10000000000, 99999999999)
            email = imie.lower() + "." + drugie_imie.lower() + "@" + nazwisko.lower() + ".com"
            output.write(f"INSERT INTO public.nauczyciele (id_nauczyciela, imie, drugie_imie, nazwisko, plec, telefon, pesel, email) VALUES ({id_nauczyciela}, '{imie}', '{drugie_imie}', '{nazwisko}', '{plec}', '{telefon}', '{pesel}', '{email}');\n")


def lysyOpiekunowie(number):
    # example query: INSERT INTO public.opiekunowie (id_opiekuna, imie, drugie_imie, nazwisko, plec, telefon, pesel, email) VALUES (1, 'Kamil', 'Robert', 'Slimak', 'M', '481-856-761', '46768365021', 'kamil.slimak@gmail.com');
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            id_opiekuna = i+1
            imie, nazwisko = getRandomName()
            drugie_imie, _ = getRandomName()
            plec = random.choice(['M', 'K'])
            telefon = getRandomPhoneNumber()
            pesel =  random.randint(10000000000, 99999999999)
            email = imie.lower() + "." + drugie_imie.lower() + "@" + nazwisko.lower() + ".com"
            output.write(f"INSERT INTO public.opiekunowie (id_opiekuna, imie, drugie_imie, nazwisko, plec, telefon, pesel, email) VALUES ({id_opiekuna}, '{imie}', '{drugie_imie}', '{nazwisko}', '{plec}', '{telefon}', '{pesel}', '{email}');\n")


def kubaStock(number):
    # example query INSERT INTO Products.Stock(stockID,amount,lastRestock) VALUES (1,423,'2021-10-19');
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            stockID = i+1
            amount = random.randint(0, 5000)
            lastRestock = getRandomDateInPast()
            output.write(f"INSERT INTO Products.Stock(stockID,amount,lastRestock) VALUES ({stockID},{amount},'{lastRestock}');\n")


def kubaSuppliers(number):
    # example query INSERT INTO Products.Suppliers(supplierID,CompanyName,Address,City,Country,Phone,Fax) VALUES (1,Czerwony_Niedzwiedz,ul. Mala,Rzeszow,Polska,824551323,3-231-341-4511)
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            supplierID = i+1
            CompanyName = getRandomCompanyName()
            Address = getRandomStreet()
            Cities = ['Rzeszow', 'Warszawa', 'Krakow', 'Wroclaw', 'Poznan', 'Gdansk', 'Szczecin', 'Lodz', 'Bydgoszcz', 'Lublin', 'Katowice', 'Bialystok', 'Gdynia', 'Czestochowa', 'Sosnowiec', 'Radom', 'Gliwice', 'Torun', 'Bielsko-Biala', 'Bytom', 'Zabrze', 'Kielce', 'Ruda Slaska', 'Rybnik', 'Walbrzych', 'Tychy', 'Olsztyn', 'Opole', 'Wadowice']
            City =  random.choice(Cities)
            Counteries = ['Polska', 'Niemcy', 'Czechy', 'Rosja', 'Ukraina', 'Belgia', 'Francja', 'Wlochy', 'Hiszpania', 'Szwajcaria', 'Wielka Brytania', 'Irlandia', 'Szwecja', 'Dania', 'Norwegia', 'Finlandia', 'Estonia', 'Litwa', 'Latwia', 'Szwecja', 'Austria', 'Słowacja', 'Słowenia', 'Chorwacja', 'Węgry', 'Bułgaria', 'Grecja', 'Malta', 'Cypr', 'Portugalia', 'Niderlandy', 'Belgia', 'Luksemburg', 'Andora', 'Monako', 'San Marino', 'Liechtenstein', 'Watykan']
            Country = random.choice(Counteries)
            Phone = getRandomPhoneNumber()
            Fax = f'{random.randint(0, 9)}-{random.randint(0, 999):03}-{random.randint(0, 999):03}-{random.randint(0, 9999):04}'
            output.write(f"INSERT INTO Products.Suppliers(supplierID,CompanyName,Address,City,Country,Phone,Fax) VALUES ({supplierID},'{CompanyName}','{Address}','{City}','{Country}','{Phone}','{Fax}');\n")


def kubaHistory(number):
    # example query INSERT INTO Orders.History(HistoryID,orderDate,deliveryDate) VALUES (1,'2021-10-16','2021-10-20');
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            HistoryID = i+1
            now = datetime.datetime.now()
            days = random.randint(50, 365)
            orderDate = now - datetime.timedelta(days=days)
            deliveryDate = orderDate + datetime.timedelta(days=random.randint(1, 10))
            orderDate = orderDate.strftime('%Y-%m-%d')
            deliveryDate = deliveryDate.strftime('%Y-%m-%d')
            output.write(f"INSERT INTO Orders.History(HistoryID,orderDate,deliveryDate) VALUES ({HistoryID},'{orderDate}','{deliveryDate}');\n")


def kubaEmployees(number):
    # example query: INSERT INTO Employees(employeeID, firstName, lastName, birthDate, salary, department, hireDate) VALUES (1,'Jan','Kowalski','1970-11-20','43244','Salesman','2019-09-24');
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            employeeID = i+1
            firstName, lastName = getRandomName()
            birthDate = getRandomDateInBigPast()
            salary = random.randint(1000, 10000)
            departments = ['Salesman', 'Manager', 'Accountant', 'IT', 'HR']
            department = random.choice(departments)
            hireDate = getRandomDateInPast()
            output.write(f"INSERT INTO Employees(employeeID, firstName, lastName, birthDate, salary, department, hireDate) VALUES ({employeeID},'{firstName}','{lastName}','{birthDate}','{salary}','{department}','{hireDate}');\n")


def kubaShipmentAdress(number):
    # example query: INSERT INTO Customers.ShipmentAddress(shipmentAddressID, ShipAddress, ShipCity, ShipPostalCode, ShipCountry) VALUES (1,'ul. Mala','Rzeszow','35-123','Polska');
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            shipmentAddressID = i+1
            ShipAddress = getRandomStreet()
            Cities = ['Rzeszow', 'Warszawa', 'Krakow', 'Wroclaw', 'Poznan', 'Gdansk', 'Szczecin', 'Lodz', 'Bydgoszcz', 'Lublin', 'Katowice', 'Bialystok', 'Gdynia', 'Czestochowa', 'Sosnowiec', 'Radom', 'Gliwice', 'Torun', 'Bielsko-Biala', 'Bytom', 'Zabrze', 'Kielce', 'Ruda Slaska', 'Rybnik', 'Walbrzych', 'Tychy', 'Olsztyn', 'Opole', 'Wadowice']
            ShipCity =  random.choice(Cities)
            ShipPostalCode = f'{random.randint(0, 99):02}-{random.randint(0, 999):03}'
            Counteries = ['Polska', 'Niemcy', 'Czechy', 'Rosja', 'Ukraina', 'Belgia', 'Francja', 'Wlochy', 'Hiszpania', 'Szwajcaria', 'Wielka Brytania', 'Irlandia', 'Szwecja', 'Dania', 'Norwegia', 'Finlandia', 'Estonia', 'Litwa', 'Latwia', 'Szwecja', 'Austria', 'Słowacja', 'Słowenia', 'Chorwacja', 'Węgry', 'Bułgaria', 'Grecja', 'Malta', 'Cypr', 'Portugalia', 'Niderlandy', 'Belgia', 'Luksemburg', 'Andora', 'Monako', 'San Marino', 'Liechtenstein', 'Watykan']
            ShipCountry = random.choice(Counteries)
            output.write(f"INSERT INTO Customers.ShipmentAddress(shipmentAddressID, ShipAddress, ShipCity, ShipPostalCode, ShipCountry) VALUES ({shipmentAddressID},'{ShipAddress}','{ShipCity}','{ShipPostalCode}','{ShipCountry}');\n")


def kubaCunstactAdress(number):
    # example query: INSERT INTO Customers.ContactAddress(contactAddressID, Email, PhoneNumber, Fax) VALUES (1,'test@gmail.com','482499123','1-234-423-4442');
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            contactAddressID = i+1
            Email = getRandomEmail()
            PhoneNumber = getRandomPhoneNumber()
            Fax = f'{random.randint(0, 9)}-{random.randint(0, 999):03}-{random.randint(0, 999):03}-{random.randint(0, 9999):04}'
            output.write(f"INSERT INTO Customers.ContactAddress(contactAddressID, Email, PhoneNumber, Fax) VALUES ({contactAddressID},'{Email}','{PhoneNumber}','{Fax}');\n")


def kubaCartProducts(number):
    # example query: INSERT INTO Customers.CartProducts(cartProductsID,productID,amount) VALUES (1,1,2);
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            cartProductsID = i+1
            productID = random.randint(1, 250)
            amount = random.randint(1, 10)
            output.write(f"INSERT INTO Customers.CartProducts(cartProductsID,productID,amount) VALUES ({cartProductsID},{productID},{amount});\n")


def kubaCart(number):
    # example query: INSERT INTO Customers.Cart(cartID,couponID,cartProductsID) VALUES (1,1,2);
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            cartID = i+1
            couponID = random.randint(1, 6)
            cartProductsID = random.randint(1, 250)
            output.write(f"INSERT INTO Customers.Cart(cartID,couponID,cartProductsID) VALUES ({cartID},{couponID},{cartProductsID});\n")


def kubaCouriers():
    # example query: INSERT INTO Couriers(courierID,phone,companyName) VALUES (1,'482499123','DHL');
    kurierzy = ['DHL', 'UPS', 'FedEx', 'GLS', 'DPD', 'TNT', 'InPost', 'Poczta Polska']
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(len(kurierzy)):
            courierID = i+1
            phone = getRandomPhoneNumber()
            companyName = kurierzy[i]
            output.write(f"INSERT INTO Couriers(courierID,phone,companyName) VALUES ({courierID},'{phone}','{companyName}');\n")


def kubaProducts():
    # example query: INSERT INTO Products.Product(productID,cartID,categoryID,supplierID,stockID,unitPrice,expirationDate,productName) VALUES (1,1,1,1,1,10,'2021-10-19','Mleko');
    with open('output.txt', 'w', encoding='utf-8') as output:
        products = ['marcherwka', 'mleko', 'jajka', 'ser', 'chleb', 'maslo', 'pomidor', 'cebula', 'ogorek', 'papryka', 'sok pomaranczowy',
                        'sok jabłkowy', 'sok truskawkowy', 'sok malinowy', 'sok wiśniowy', 'sok gruszkowy', 'sok brzoskwiniowy', 'sok czarnej porzeczki',
                        'sok malinowy', 'jajka', 'mięso', 'woda', 'cola', 'fanta', 'sprite', 'piwo', 'wino', 'wódka', 'whisky', 'rum', 'wódka', 'wódka', 'wódka']
        for i in range(len(products)):
            productID = i+1
            cartID = random.randint(1, 250)
            categoryID = random.randint(1, 6)
            supplierID = random.randint(1, 250)
            stockID = random.randint(1, 250)
            unitPrice = random.randint(5, 200)
            expirationDate = getRandomDateInFuture()
            productName = products[i]
            output.write(f"INSERT INTO Products.Product(productID,cartID,categoryID,supplierID,stockID,unitPrice,expirationDate,productName) VALUES ({productID},{cartID},{categoryID},{supplierID},{stockID},{unitPrice},'{expirationDate}','{productName}');\n")


def kubaCustomers(number):
    # example query: INSERT INTO Customers.Customer(customerID,firstName,lastName,contactAddressID,shipmentAddressID,cartID,gender) VALUES (1,'Jan','Kowalski',250,250,250,'M');
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            customerID = i+1
            firstName, lastname = getRandomName()
            contactAddressID = random.randint(1, 250)
            shipmentAddressID = random.randint(1, 250)
            cartID = random.randint(1, 250)
            gender = random.choice(['M', 'F'])
            output.write(f"INSERT INTO Customers.Customer(customerID,firstName,lastName,contactAddressID,shipmentAddressID,cartID,gender) VALUES ({customerID},'{firstName}','{lastname}',{contactAddressID},{shipmentAddressID},{cartID},'{gender}');\n")


def kubaOrders(number):
    # example query: INSERT INTO Orders.Order(orderID,customerID,employeeID,courierID,detailsID,historyID,returnsID) VALUES (1,250,30,8,250,250,10);
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            orderID = i+1
            customerID = orderID
            employeeID = random.randint(1, 30)
            courierID = random.randint(1, 8)
            detailsID = orderID
            historyID = orderID
            returnsID = random.randint(1, 10)
            output.write(f"INSERT INTO Orders.Order(orderID,customerID,employeeID,courierID,detailsID,historyID,returnsID) VALUES ({orderID},{customerID},{employeeID},{courierID},{detailsID},{historyID},{returnsID});\n")


def kubaOrderDetails(number):
    # example qyery: INSERT INTO Orders.Details(detailsID,productID,statusID,orderID,paymentID,quantity,discount) VALUES (1,33,5,250,3,20,10);
    with open('output.txt', 'w', encoding='utf-8') as output:
        for i in range(number):
            detailsID = i+1
            productID = random.randint(1, 33)
            statusID = random.randint(1, 5)
            orderID = detailsID
            paymentID = random.randint(1, 3)
            quantity = random.randint(1, 20)
            discount = random.randint(0, 10)
            output.write(f"INSERT INTO Orders.Details(detailsID,productID,statusID,orderID,paymentID,quantity,discount) VALUES ({detailsID},{productID},{statusID},{orderID},{paymentID},{quantity},{discount});\n")


if __name__ == '__main__':
    main()
