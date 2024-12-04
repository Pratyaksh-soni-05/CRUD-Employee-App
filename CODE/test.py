def pyramid_pattern(n):
    # Pyramid pattern with numbers
    for i in range(1, n + 1):
        print(' ' * (n - i), end='')  # Leading spaces
        for j in range(1, i + 1):
            print(j, end=' ')  # Numbers on each level
        print()  # Newline after each row
