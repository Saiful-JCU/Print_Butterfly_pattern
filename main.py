def butterfly(n):
    # this loop for upper half of the butterfly
    for i in range(n):
        print("*" * (i + 1) + ' ' * (n - i - 1) + ' ' * (n - i -1) + '*' * (i + 1))

    #this line loop for lower half of the butterfly
    for i in range(n - 1, -1, -1):
        print("*" * (i + 1) + ' ' * (n - i - 1) + ' ' * (n - i - 1) + '*' * (i + 1))


butterfly(5)
