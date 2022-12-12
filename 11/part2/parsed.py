l = 9699690

monkey = {0: {
        "s": [91, 54, 70, 61, 64, 64, 60, 85],
        "worry": lambda old: ((old % l) * 13) % l,
        "test": lambda w: w % 2,
        "c": (5, 2)
    },
    1: {
        "s": [82],
        "worry": lambda old: ((old % l) + 7) % l,
        "test": lambda w: w % 13,
        "c": (4, 3)
    },
    2: {
        "s": [84, 93, 70],
        "worry": lambda old: ((old % l) + 2) % l,
        "test": lambda w: w % 5,
        "c": (5, 1)
    },
    3: {
        "s": [78, 56, 85, 93],
        "worry": lambda old: ((old % l) * 2) % l,
        "test": lambda w: w % 3,
        "c": (6, 7)
    },
    4: {
        "s": [64, 57, 81, 95, 52, 71, 58],
        "worry": lambda old: ((old % l) * (old % l)) % l,
        "test": lambda w: w % 11,
        "c": (7, 3)
    },
    5: {
        "s": [58, 71, 96, 58, 68, 90],
        "worry": lambda old: ((old % l) + 6) % l,
        "test": lambda w: w % 17,
        "c": (4, 1)
    },
    6: {
        "s": [56, 99, 89, 97, 81],
        "worry": lambda old: ((old % l) + 1) % l,
        "test": lambda w: w % 7,
        "c": (0, 2)
    },
    7: {
        "s": [68, 72],
        "worry": lambda old: ((old % l) + 8) % l,
        "test": lambda w: w % 19,
        "c": (6, 0)
    },
    }
