def roman_numerals_to_int(roman_numeral):
    translater = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    int_numeral = 0
    prev = 0

    try:
        for i in reversed(roman_numeral):
            value = translater.get(i)
            if value is None:
                return None

            if value < prev:
                int_numeral -= value
            else:
                int_numeral += value

            prev = value

    except TypeError:
        return None
    return int_numeral
