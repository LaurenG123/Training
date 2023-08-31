

pays = input("Insérer le nom du pays sans espaces: ")

def article(pays):
    exceptions = ["Belize", "Cambodge", "Mexique", "Zaire", "Zimbabwe"]
    voyelles = ("aeiouhAEIOUH")

    if pays[0] in voyelles:
        if pays[-1] == 's':
            return f"Les {pays}"

        else:
            return f"l'{pays}"



    elif pays[-1] == 'e':
        if pays in exceptions:
            return f"Le {pays}"

        else:
            return f"La {pays}"

    else:
        return f"Le {pays}"


print(article(pays))