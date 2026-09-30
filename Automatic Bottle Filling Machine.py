# Automatic-Bottle-Filling-Machine
# Automatic Bottle Filling Machine

bottle_capacity = 500  # ml

while True:
    print("\n--- AUTOMATIC BOTTLE FILLING MACHINE ---")
    print("1. Start Filling")
    print("2. Stop Machine")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\nBottle detected!")
        print("Filling started...")

        water = 0

        while water < bottle_capacity:
            water += 100
            print("Water filled:", water, "ml")

        print("Bottle is FULL!")
        print("Filling stopped automatically.")

    elif choice == "2":
        print("Machine stopped.")

    elif choice == "3":
        print("Program closed.")
        break

    else:
        print("Invalid choice!")
