import os

cars = [
    {
        'name': 'Chevrolet Tracker', 
        'price': 120,
        'status': 'A'
    },
    {
        'name':'Chevrolet Onix',
        'price': 90,
        'status': 'A'
    },
    {
        'name': 'Chevrolet Spin',
        'price': 150,
        'status': 'A'
    },
    {
        'name': 'Hyundai HB20',
        'price': 85,
        'status': 'A'
    },
    {
        'name': 'Hyundai Tucson',
        'price': 120,
        'status': 'A'
    },
    {
        'name': 'Fiat Uno',
        'price': 160,
        'status': 'A'
    },
    {
        'name' : 'Fiat Mobi',
        'price': 70,
        'status': 'A'
    },
    {
        'name': 'Fiat Pulse',
        'price': 130,
        'status': 'A'
    }
]

def greeting():
    os.system("cls")
    print("============")
    print("Welcome to the Rental car!")
    print("============")
    print("choose a option:")
    print("0 - show the cars options | 1 - rent a car | 2 - return a car")
    print("")
    option = int(input())
    menuOptions(option)

def menuOptions(option):
    if option == 0:
        showCarsList(cars)
        print("")
        print("1 - continue | 9 - return")
        option = int(input())
        if option == 1:
            rentProtocol()
        elif option == 9:
            greeting()
        else:
            greeting()            
    elif option == 1:
        showCarsList(cars)
        rentProtocol()
    elif option == 2:
        print("Wich car do you want to return?")
        showCarsReturn(cars)
        print("Wich car do you want return? (use the number code)")
        carCode = int(input())
        cars[carCode]['status'] = 'A'
        print("Thank you :)")
        os.system("PAUSE")
        greeting()
    else:
        greeting()

def rentProtocol():
    print("")
    print("Wich car do you want rent? (use the number code)")
    carCode = int(input())
    print('How many days do you want rent the {}?'.format(cars[carCode]['name']))
    daysRent = int(input())
    total = cars[carCode]['price'] * daysRent
    print('the total to rent the {0} for {1} days is ${2}. Do you want proceed? (1 - continue | 9 - return)'.format(cars[carCode]['name'], daysRent, total))
    option = int(input())
    if option == 1:
        print("Go to the check out area to get your {} for {} days! Enjoy :)!".format(cars[carCode]['name'], daysRent))
        cars[carCode]['status'] = 'O'
        os.system("PAUSE")
        greeting()
    elif option == 9:
        print("Operation canceled!")
        os.system("PAUSE")
        greeting()

def showCarsList(cars):
    i = 0
    for car in cars:
        if car['status'] == 'A':
            print("[{}] {} ${}/day".format(i, car['name'], car['price']))
            i += 1

def showCarsReturn(cars):
    i = 0
    for car in cars:
        if car['status'] == 'O':
            print("[{}] {}".format(i, car['name']))
            i += 1


greeting()
option = int(input())


    
