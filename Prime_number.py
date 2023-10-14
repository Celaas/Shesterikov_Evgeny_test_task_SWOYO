def prime_numbers(low, high):
    numbers = []

    try:
        if int(low) == low and int(high) == high:
            low = int(low)
            high = int(high)

        for i in range(low, high + 1):
            for j in range(2, i + 1):
                if i % j == 0 and i != 2:
                    break
                elif i // j <= j:
                    numbers.append(i)
                    break

    except TypeError:
        return numbers

    return numbers

