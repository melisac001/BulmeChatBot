from re import sub


def remove_punctuations(text):
    return sub(r"(\.|\?|\!$)", "", text)


def tidy_up(text):
    text = text.lower()

    substitutions = [
     ["i'm", "i am"],
     ["'re", " are"]
    ]

    for substitution in substitutions:
        text = sub(substitution[0], substitution[1], text)

    return(text)


def reflect(text):

    substitutions = [
     # first person to second person
     ["ich bin", "du bist"],
     [r"\bmy\b", "deins"],
     [r"\bmine\b", "deins"],
     ["mirselber", "dirselber"],
     [r"\bme\b", "du"],
     [r"wasn't", "sind nicht"],
     [r"\bwas\b", "sind"],
     [r"\bi\b", "ihr"],
     # second person to first person
     ["du bist", "ich bin"],
     ["bist du", "bin ich"],
     ["do you", "DO I"],
     [r"\byour\b", "mein"],
     [r"\byours\b", "meins"],
     ["dirselber", "mirselber"],
     ["weren't", "war nicht"],
     [r"\bwere\b", "war"],
     [r"you$", "mir"],
     [r"du auch", "ich zu"],
     [r"du", "ich"]
    ]

    for substitution in substitutions:
        text = sub(substitution[0], substitution[1], text)

    return text.lower()
