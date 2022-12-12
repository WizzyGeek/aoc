
monkey = {0: {
        "s": [79, 98],
        "worry": lambda old: ((old * 19) // 3),
        "test": lambda w: w % 23,
        "c": (2, 3)
    },
    1: {
        "s": [54, 65, 75, 74],
        "worry": lambda old: ((old + 6) // 3),
        "test": lambda w: w % 19,
        "c": (2, 0)
    },
    2: {
        "s": [79, 60, 97],
        "worry": lambda old: ((old * old) // 3),
        "test": lambda w: w % 13,
        "c": (1, 3)
    },
    3: {
        "s": [74],
        "worry": lambda old: ((old + 3) // 3),
        "test": lambda w: w % 17,
        "c": (0, 1)
    },
}
