import math as m

while True:
    print("\nCombinatorics Calculator")
    print("1. Permutations")
    print("2. Combinations")
    print("3. Exit")

    choice = input("Select option: ").strip()

    if choice == "1":

        condition_permutation = input(
            "Enter r for repeating, nr for non-repeating, c for circular: "
        ).lower().strip()

        n = int(input("Enter n: "))
        r = int(input("Enter r: "))

        if condition_permutation == "nr" and n >= r:
            result = m.factorial(n) // m.factorial(n - r)
            print("Result:", result)

        elif condition_permutation == "r":
            result = n ** r
            print("Result:", result)

        elif condition_permutation == "c":
            result = m.factorial(n - 1)
            print("Result:", result)

        else:
            print("Invalid input")

    elif choice == "2":

        combination_type = input(
            "Enter 'nr' for no replacement or 'r' for repetition: "
        ).lower().strip()

        n = int(input("Enter n value: "))
        r = int(input("Enter r value: "))

        if combination_type == "nr" and n >= r:
            result = m.factorial(n) // (m.factorial(r) * m.factorial(n - r))
            print("Result:", result)

        elif combination_type == "r" and n >= r:
            result = m.factorial(n + (r - 1)) // (
                m.factorial(r) * m.factorial((n + (r - 1)) - r)
            )
            print("Result:", result)

        else:
            print("Invalid input")

    elif choice == "3":
        break

    else:
        print("Invalid choice")