l = 96577

monkey = {0: {
        "s": [79, 98],
        "worry": lambda old: ((old % l) * 19) % l,
        "test": lambda w: w % 23,
        "c": (2, 3)
    },
    1: {
        "s": [54, 65, 75, 74],
        "worry": lambda old: ((old % l) + 6) % l,
        "test": lambda w: w % 19,
        "c": (2, 0)
    },
    2: {
        "s": [79, 60, 97],
        "worry": lambda old: ((old % l) ** 2) % l,
        "test": lambda w: w % 13,
        "c": (1, 3)
    },
    3: {
        "s": [74],
        "worry": lambda old: (((old % l) + 3) % l),
        "test": lambda w: w % 17,
        "c": (0, 1)
    },
}
