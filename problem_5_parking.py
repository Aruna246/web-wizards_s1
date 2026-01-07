total_slots = 3
occupied = 0
while True:
    choice = int(input("Enter choice: "))
    if choice == 1:
        if occupied < total_slots:
            occupied += 1
            print("Vehicle parked at slot")
            print("Available slots:", total_slots - occupied)
        else:
            print("Parking Full")
    elif choice == 2:
        if occupied > 0:
            occupied -= 1
            print("Vehicle removed from slot")
            print("Available slots:", total_slots - occupied)
        else:
            print("No vehicle to remove")
    else:
        print("Invalid choice")
