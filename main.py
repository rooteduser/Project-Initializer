import os

dirpath = os.getcwd()
stack = [dirpath] # directory stack
width = os.get_terminal_size().columns
title = r'''
                        ____            _           _     ___       _ _   _       _ _
                       |  _ \ _ __ ___ (_) ___  ___| |_  |_ _|_ __ (_) |_(_) __ _| (_)_______ _ __
                       | |_) | '__/ _ \| |/ _ \/ __| __|  | || '_ \| | __| |/ _` | | |_  / _ \ '__|
                       |  __/| | | (_) | |  __/ (__| |_   | || | | | | |_| | (_| | | |/ /  __/ |
                       |_|   |_|  \___// |\___|\___|\__| |___|_| |_|_|\__|_|\__,_|_|_/___\___|_|
                                     |__/
'''

print(title.center(width))
while True:
    print(f"\nCurrent directory: {dirpath}")
    print("1. Create subdirectory")
    print("2. Create file")
    print("3. Go back one level")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        dirname = input("Enter subdirectory name: ")
        stack.append(dirname)
        dirpath = os.path.join(*stack)
        print(dirpath)
        os.makedirs(dirpath, exist_ok=True)
        print(f"\nCreated: {dirpath}")

    elif choice == "2":
        filename = input("Enter file name:")
        filepath = os.path.join(*stack, filename)
        with open(filepath, "w") as f:
            pass
        print("\nCreated file:", filepath)
        
    elif choice == "3":
        if stack:
            stack.pop()
        dirpath = os.path.join(*stack) if stack else ""

    elif choice == "4":
        print("Done creating directories.")
        break

    else:
        print("Invalid choice.")