import datetime
import random
import string

import coolname
import names


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)


def random_mail():
    domains = ['hotmail.com', 'gmail.com', 'yahoo.com', 'mymail.com', 'myspace.com', 'euromail.eu']
    mail = ''
    mail += coolname.generate_slug()
    mail += '@' + random.choice(domains)
    return mail


def random_phone():
    length = range(1, 4)
    phoneNumber = ''
    prefix = ''
    prefixLength = range(1, 4)
    for i in prefixLength:
        prefix += random.choice(string.digits)
    phoneNumber += prefix + ' '
    for i in length:
        phoneNumber += random.choice(string.digits)
    phoneNumber += '-'
    for i in length:
        phoneNumber += random.choice(string.digits)
    phoneNumber += '-'
    for i in length:
        phoneNumber += random.choice(string.digits)

    return phoneNumber

def random_address():
    number = random.randrange(1,9999)
    adress = '' + str(number) + ' '
    adress += coolname.generate_slug()
    return adress

def generate_client():
    clients = []
    d1 = datetime.date(1970, 1, 1)
    d2 = datetime.date(2005, 1, 1)
    counter = 0
    chosengender = random.choice(['male', 'female'])
    if random.random() > 0.15:
        query = "insert into [dbo].[DimClient](FirstName, SecondName, LastName, Address, BirthDate, Email, Phone) " + \
            "values(\'" + names.get_first_name(gender=chosengender) + "\', " + \
                "null, \'" + \
                names.get_last_name() + "\', \'"
    else:
        counter += 1
        query = "insert into [dbo].[DimClient](FirstName, SecondName, LastName, Address, BirthDate, Email, Phone) " + \
            "values(\'" + names.get_first_name(gender=chosengender) + "\', \'" + \
                names.get_first_name(gender=chosengender) + "\', \'" + \
                names.get_last_name() + "\', \'"
    query += str(random_address()) + "\', \'"
    query += random_date(d1, d2).strftime("%m-%d-%Y") + "\', \'"
    query += random_mail() + "\', \'"
    query += random_phone() + "\');\n"

    return query



def main():
    file = open("sampleClient9.txt", "w")
    clientCount = range(1, 20001)
    for client in clientCount:
        if client % 100 is 0:
            print("A: " + str(client))
        file.write(generate_client())

    #file1 = open("sampleClient5.txt", "w")
    #clientCount = range(1, 100001)
    #for client in clientCount:
    #    if client % 100 is 0:
    #        print("B: " + str(client))
    #    file1.write(generateClient())

    #file2 = open("sampleClient6.txt", "w")
    #clientCount = range(1, 100001)
    #for client in clientCount:
    #    if client % 100 is 0:
    #        print("C: " + str(client))
    #    file2.write(generateClient())

    file.close()
    #file1.close()
    #file2.close()

if __name__ == "__main__":
    main()