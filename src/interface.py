import string_utils
import time


def story(text):
    storyParts = text.split('*')
    for part in storyParts:
        if string_utils.isNumber(part):
            time.sleep(float(part))
        else:
            print(part)


def ask(question):
    ret = input(question + "\n")
    print()
    return ret


def ask_discrete(question, options):
    print(question)
    for option in options:
        print(" - " + option[0] + " : " + option[1], sep="", end="\n")
    ret = input("\n")
    print()
    return ret
