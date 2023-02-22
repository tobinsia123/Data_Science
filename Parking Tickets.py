day = 1
hour = 0
hours_parked = 25
sum_num = 0
multiplier = 5
checker = 0
discount = 1
charge = 0

amount_given = 0
daily_total = 0

addon = 0

while True:
    print("Days\n1 Sunday\n2 Monday\n3 Tuesday\n4 Wednesday\n5 Thursday\n6 Friday\n7 Saturday")
    print("Is it still day", day, end=" ")
    day_change = input("?")
    if day_change.upper() == "N":
        while True:
            print("The daily total was: ", daily_total)
            daily_total = 0
            day = int(input("Enter Day Number:"))
            if day > 0 and day < 8:
                break

    while True:
        hour = int(
            input("Please enter a number from 8 until 22. \nPlease enter the hour in 24 hour format, so 3pm is 15:"))
        if hour > 7 and hour < 24:
            break

    while True:
        hours_parked = int(input("How many hours would you like to leave your car?"))
        if (hours_parked + hour) >= 24:
            print("You need to leave before midnight")
        else:
            break

    parking_number = input("Please enter Parking Number: ")
    if len(parking_number) == 5:
        print("Correct Length")
        print("Numbers to check", parking_number[0:4])

        for char in parking_number[0:4]:
            sum_num += int(char) * multiplier
            print("Multiplier", multiplier, "Total", sum_num)
            multiplier -= 1
        print("remainder", sum_num % 11)
        print("11 - remainder", 11 - sum_num % 11)
        checker = 11 - sum_num % 11
        if checker == 11:
            checker = "0"
        elif checker == 10:
            checker = "X"
        else:
            checker = str(checker)
        print("Final Checker", checker)

        if checker == parking_number[4]:
            print("Parking Number validated")

            if hour >= 16:
                discount = 0.5

            else:
                discount = 0.9
        else:
            print("Parking not validated")
    else:
        print("Parking number is the wrong length")

    if hour >= 16:
        charge = 2 * discount
        print("\nYou will be charged £", charge)
    else:
        if hour + hours_parked > 16:
            hours_parked -= (hour + hours_parked) - 16
            addon = 2

        if day == 1:
            charge = (2 * hours_parked * discount) + addon
            print("\nYou will be charged £", charge)
        elif day == 7:
            charge = (3 * hours_parked * discount) + addon
            print("\nYou will be charged £", charge)
        else:
            charge = (10 * hours_parked * discount) + addon
            print("\nYou will be charged £", charge)

    while True:
        amount_given = float(input("How much did you pay?"))
        if amount_given >= charge:
            break

    daily_total += amount_given
    print("The running total is", daily_total)