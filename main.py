vehicle = ["AC Car for maximum number of 3 passengers",
           "AC Car for maximum number of 4 passengers",
           "NonAC Car for maximum number of 3 passengers",
           "NonAC Car for maximum number of 4 passengers",
           "AC Van for maximum number of 6 passengers",
           "NonAC Van for maximum number of 6 passengers",
           " AC Van for maximum number of 8 passengers",
           "NonAC Van for maximum number of 8 passengers",
           "12ft Truck", "7ft Truck", "2500kg max load Lorry",
           "3500kg max load Lorry",
           "3 Wheeler for maximum number of 3 passengers"]

beginning_of_the_program = ('''      **********Welcome! to RIDE cab service**********
 **********Enter your requirements to get started**********
             (Please enter 0 if not applicable)''')
print(beginning_of_the_program)

noOfPassengers = str(input("Choose number of passengers(3 or 4): "))
AC = (input("AC or NonAC: "))
size = (input("Size (only 7ft and 12 ft):  "))
load = int(input("Load(only 2500Kg and 3500Kg): "))

if AC == "AC" and noOfPassengers == "3":
    print(vehicle[0] + " is available")
elif AC == "AC" and noOfPassengers == "4":
    print(vehicle[1] + " is available")
elif AC == "NonAC" and noOfPassengers == "3":
    print(vehicle[2] + " is available")
elif AC == "NonAC" and noOfPassengers == "4":
    print(vehicle[3] + " is available")
elif AC == "AC" and noOfPassengers == "6":
    print(vehicle[4] + " is available")
elif AC == "AC" and noOfPassengers == "8":
    print(vehicle[6] + " is available")
elif AC == "NonAC" and noOfPassengers == "6":
    print(vehicle[5] + " is available")
elif AC == "NonAC" and noOfPassengers == "8":
    print(vehicle[7] + " is available")
elif noOfPassengers == "0" or (size == "7"):
    print(vehicle[9] + " is available")
elif noOfPassengers == "0" or (size == "12"):
    print(vehicle[8] + " is available")
elif load == "2500":
    print(vehicle[10] + " is available")
elif load == "3500":
    print(vehicle[11] + " is available")
elif noOfPassengers == "3":
    print(vehicle[12] + " is available")
purpose = input('''===What is the service you are looking for===
 1.Add a new vehicle
 2.Remove a vehicle 
 3.Hire a vehicle
 4.Release a vehicle
 5.See available vehicles in each category
 (Enter the the number of the service to proceed): ''')

if purpose == "1":
    add_a_vehicle = input("Enter your vehicle: ")
    vehicle.append(add_a_vehicle)
    print(add_a_vehicle + " is" + " added to the system", vehicle)
    exit_program = input(
        "Do you wish to go back to the main menu or exit the program(Type 1 to go back and 2 to exit): ")
    if exit_program == "1":
        print(beginning_of_the_program)
        noOfPassengers = str(input("Choose number of passengers(3 or 4): "))
        AC = (input("AC or NonAC: "))
        size = (input("Size (only 7ft and 12 ft):  "))
        load = int(input("Load(only 2500Kg and 3500Kg): "))
    elif exit_program == "2":
        print('''!Thank you, have a nice day!''')
elif purpose == "2":
    remove_a_vehicle = input("Enter the vehicle: ")
    vehicle.remove(remove_a_vehicle)
    print(remove_a_vehicle + " is" + " removed from the system", vehicle)
    exit_program = input("Do you wish to go back to the main menu or exit the program(Type 1 to go back and 2 to exit)")
    if exit_program == "1":
        print(beginning_of_the_program)
        noOfPassengers = str(input("Choose number of passengers(3 or 4): "))
        AC = (input("AC or NonAC: "))
        size = (input("Size (only 7ft and 12 ft):  "))
        load = int(input("Load(only 2500Kg and 3500Kg): "))
    elif exit_program == "2":
        print('''!Thank you, have a nice day!''')
elif purpose == "3":
    print(vehicle)
    hire_an_vehicle = input("Enter the vehicle you want to hire: ")
    vehicle.append(hire_an_vehicle)
    print("Congrats! you hired a vehicle")
    exit_program = input("Do you wish to go back to the main menu or exit the program(Type 1 to go back and 2 to exit)")
    if exit_program == "1":
        print(beginning_of_the_program)
        noOfPassengers = str(input("Choose number of passengers(3 or 4): "))
        AC = (input("AC or NonAC: "))
        size = (input("Size (only 7ft and 12 ft):  "))
        load = int(input("Load(only 2500Kg and 3500Kg): "))
    elif exit_program == "2":
        print('''!Thank you, have a nice day!''')
elif purpose == "4":
    decision = (input("What is the vehicle you want to release: "))

    vehicle.append(decision)
    print(vehicle)
    exit_program = input("Do you wish to go back to the main menu or exit the program(Type 1 to go back and 2 to exit)")
    if exit_program == "1":
        print(beginning_of_the_program)
        noOfPassengers = str(input("Choose number of passengers(3 or 4): "))
        AC = (input("AC or NonAC: "))
        size = (input("Size (only 7ft and 12 ft):  "))
        load = int(input("Load(only 2500Kg and 3500Kg): "))
    elif exit_program == "2":
        print('''!Thank you, have a nice day!''')
elif purpose == "5":
    print('''            ===========================================================================
                                     Our Categories
            ===========================================================================
            | Vehicle | AC | NonAC | Number of Passengers |Size(ft) | Maximum Load(kg)|
            ___________________________________________________________________________
            | Car      | X  |   -   |         3           |    -    |        -        | 
            | Car      | X  |   -   |         4           |    -    |        -        |
            | Car      | -  |   X   |         3           |    -    |        -        | 
            | Car      | -  |   X   |         4           |    -    |        -        |
            | Van      | X  |   -   |         6           |    -    |        -        |
            | Van      | X  |   -   |         8           |    -    |        -        |  
            | Van      | -  |   X   |         6           |    -    |        -        |
            | Van      | -  |   X   |         8           |    -    |        -        |  
            | 3 Wheeler| -  |   -   |         3           |    -    |        -        |
            | Truck    | -  |       |         -           |    7    |        -        |
            | Truck    | -  |       |         -           |    12   |        -        |
            | Lorry    | -  |       |         -           |    -    |       2500      |
            | Lorry    | -  |       |         -           |    -    |       3500      |

            '''
          )
    exit_program = input("Do you wish to go back to the main menu or exit the program(Type 1 to go back and 2 to exit)")
    if exit_program == "1":
        print(beginning_of_the_program)
        noOfPassengers = str(input("Choose number of passengers(3 or 4): "))
        AC = (input("AC or NonAC: "))
        size = (input("Size (only 7ft and 12 ft):  "))
        load = int(input("Load(only 2500Kg and 3500Kg): "))
    elif exit_program == "2":
        print('''!Thank you, have a nice day!''')









