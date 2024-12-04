def pyramid_pattern(n):
    # Pyramid pattern with numbers
    for i in range(1, n + 1):
        print(' ' * (n - i), end='')  # Leading spaces
        for j in range(1, i + 1): #prints the numbers from 1 to i+1
            print(j, end=' ')  # Numbers on each level
        print()  # Newline after each row


def rhombus_pattern(n):
    # Rhombus pattern with numbers
    for i in range(1, n + 1):
        print(' ' * (n - i), end='')  # Leading spaces
        for j in range(1, n + 1): #prints the same numbers from 1 to n
            print(j, end=' ')  # Numbers on each row
        print()


def square_pattern(n):
    # Square pattern with numbers
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(j, end=' ')  # Numbers on each row
        print()


def triangle_pattern(n):
    # Triangle pattern with numbers
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=' ')  # Numbers on each row
        print()


def circle_pattern(n):
    # Simulating a circle pattern with numbers (not a true circle, but an approximation)
    radius = n // 2
    for i in range(-radius, radius + 1):
        for j in range(-radius, radius + 1):
            if i**2 + j**2 <= radius**2:
                print('*', end=' ')  # '*' represents part of the circle
            else:
                print(' ', end=' ')  # Spaces outside the circle
        print()


def play_pattern_game():
    print("Welcome to the Number Pattern Generating Game!")
    print("Choose a pattern to generate:")
    print("1. Pyramid")
    print("2. Rhombus")
    print("3. Square")
    print("4. Triangle")
    print("5. Circle")

    choice = int(input("Enter your choice (1-5): "))
    n = int(input("Enter the size of the pattern: "))

    if choice == 1:
        print("\nPyramid Pattern:")
        pyramid_pattern(n)
    elif choice == 2:
        print("\nRhombus Pattern:")
        rhombus_pattern(n)
    elif choice == 3:
        print("\nSquare Pattern:")
        square_pattern(n)
    elif choice == 4:
        print("\nTriangle Pattern:")
        triangle_pattern(n)
    elif choice == 5:
        print("\nCircle Pattern:")
        circle_pattern(n)
    else:
        print("Invalid choice! Please select a valid option.")

    replay = input("Do you want to generate another pattern? (yes/no): ").lower()
    if replay == 'yes':
        play_pattern_game()


play_pattern_game()
