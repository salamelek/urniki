days = {0: "ponedeljek", 1: "torek", 2: "sreda", 3: "četrtek", 4: "petek"}
profs = {
    "Gergolet": {
        "prosti_dnevi": [0, 1, 2, 3, 4, 5],
        "delavne_ure": {
            "lekcije": 20,
            "razpolaga": 4
        },
        "predmet": "mat"
    },
    "Neva": {
        "prosti_dnevi": [0, 1, 2, 3, 4, 5],
        "delavne_ure": {
            "lekcije": 20,
            "razpolaga": 4
        },
        "predmet": "ita"
    },
    "Viljena": {
        "prosti_dnevi": [0, 1, 2, 3, 4, 5],
        "delavne_ure": {
            "lekcije": 20,
            "razpolaga": 4
        },
        "predmet": "slo"
    },
    "Posillipo": {
        "prosti_dnevi": [0, 1, 2, 3, 4, 5],
        "delavne_ure": {
            "lekcije": 20,
            "razpolaga": 4
        },
        "predmet": "inf"
    },
    "Cvetek": {
        "prosti_dnevi": [0, 1, 2, 3, 4, 5],
        "delavne_ure": {
            "lekcije": 20,
            "razpolaga": 4
        },
        "predmet": "ver"
    },
    "Segina": {
        "prosti_dnevi": [0, 1, 2, 3, 4, 5],
        "delavne_ure": {
            "lekcije": 20,
            "razpolaga": 4
        },
        "predmet": "nar"
    },
    "Gorjup": {
        "prosti_dnevi": [0, 1, 2, 3, 4, 5],
        "delavne_ure": {
            "lekcije": 20,
            "razpolaga": 4
        },
        "predmet": "fiz"
    },
    "Legiša": {
        "prosti_dnevi": [0, 1, 2, 3, 4, 5],
        "delavne_ure": {
            "lekcije": 20,
            "razpolaga": 4
        },
        "predmet": "fil"
    },
    "Hrovatin": {
        "prosti_dnevi": [0, 1, 2, 3, 4, 5],
        "delavne_ure": {
            "lekcije": 20,
            "razpolaga": 4
        },
        "predmet": "spo"
    },
    "Kralj": {
        "prosti_dnevi": [0, 1, 2, 3, 4, 5],
        "delavne_ure": {
            "lekcije": 20,
            "razpolaga": 4
        },
        "predmet": "ang"
    },
    "Dornik": {
        "prosti_dnevi": [0, 1, 2, 3, 4, 5],
        "delavne_ure": {
            "lekcije": 20,
            "razpolaga": 4
        },
        "predmet": "lik"
    },
    "Piasentier": {
        "prosti_dnevi": [0, 1, 2, 3, 4, 5],
        "delavne_ure": {
            "lekcije": 20,
            "razpolaga": 4
        },
        "predmet": "zgo"
    }
}

razredi = {
    "5Z": {
        "mat": {"ure": 5, "pref_hour": 0, "double_hrs": 0},
        "ita": {"ure": 4, "pref_hour": None, "double_hrs": 1},
        "slo": {"ure": 4, "pref_hour": None, "double_hrs": 1},
        "inf": {"ure": 2, "pref_hour": None, "double_hrs": 0},
        "ver": {"ure": 1, "pref_hour": (0, 7), "double_hrs": 0},
        "nar": {"ure": 5, "pref_hour": None, "double_hrs": 0},
        "fiz": {"ure": 3, "pref_hour": None, "double_hrs": 0},
        "fil": {"ure": 2, "pref_hour": None, "double_hrs": 0},
        "spo": {"ure": 2, "pref_hour": None, "double_hrs": 1},
        "ang": {"ure": 3, "pref_hour": None, "double_hrs": 0},
        "lik": {"ure": 2, "pref_hour": None, "double_hrs": 0},
        "zgo": {"ure": 2, "pref_hour": None, "double_hrs": 0}
    }
}

for day in days:
    for razred in razredi:
        pass