while True:
    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        rows = int(input("Enter the number of rows for the pattern: "))
        for i in range(1, rows + 1):
            print("*" * i)

    elif choice == 2:
        start = int(input("Enter the start of range: "))
        end = int(input("Enter the end of range: "))
        
        total = 0
        for num in range(start  , end + 1 ):
            if num%2 == 0:
                print(f"{num} is Even number")
            else:
                print(f"{num} is Odd numbzer")
                total+=num
        
        print(f"Sum from {start} to {end} = {total}")

    elif choice==3:
        print("Exit the program, good bye!")
        break
   
    else:
        print("Invalid option! Try again.")

