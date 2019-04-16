import interface


def play():
    print(interface.ask_discrete("Êtes-vous :", [["1", "Jeune"], ["2", "Normal"], ["3", "Vieux"]]))
