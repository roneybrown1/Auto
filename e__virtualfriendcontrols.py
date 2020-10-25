from f_typewriter import typewrite
from os import system, name
from time import sleep
from f_virtualfriend import questionOne
from setuptools.command.easy_install import main
import pyttsx3


def clear():
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


if __name__ == '__main__':

    typewrite("Welcome to My Buddy Auto!\n"
              "Lets go ahead and get some options set so you can enjoy Auto.")
    typewrite("First I want to get a voice set that you would prefer to hear and\n"
              "luckily we have a few different ones to select from.\n")
    typewrite("Since there is a total of 13 different voices I want to make\n"
              "it a little easier on you and break them up into Male and Female\n"
              "selections. Which would you like to hear first? ")

    maxAttempts = 3
    while True:
        gselect = input('[M]ale or [F]emale? ').lower()
        if gselect == 'm' or gselect == 'f':
            break
        else:
            if maxAttempts == 3:
                typewrite("Hey I also like to just press random keys, but to make sure\n"
                          "you get a voice you like. Please enter 'M' or 'F', and if you\n"
                          "don't want to press the shift key it's okay, I promise.")
                maxAttempts = maxAttempts - 1
                continue
            if maxAttempts == 2:
                typewrite("Okay...No, it's fine lets just try this again...So to have a\n"
                          "voice you like. Please enter 'M' or 'F', that means either the\n"
                          "M or the F key on your keyboard.")
                maxAttempts = maxAttempts - 1
                continue
            if maxAttempts == 1:
                typewrite("Is either one of those keys broken on your keyboard? I mean...\n"
                          "I just need you press M or F, nothing else...Just M or F...\n"
                          "Please press ONLY M or F....")
                maxAttempts = maxAttempts - 1
                continue
            if maxAttempts == 0:
                typewrite("...Okay...I mean that's cool, I'm not mad or anything but I really\n"
                          "would have preferred for you to selected your own choice but here\n"
                          "we are.\nUmm...\nSoooo....\nI guess this one will do...Have fun...")
                sleep(7)
                break

    if gselect == 'm':
        typewrite("Awesome! Now lets go ahead and get a voice you like selected!")

    if gselect == 'f':
        typewrite("Awesome! Now lets go ahead and get a voice you like selected!")
    # elif gselect != 'm' or 'f':
    # typewrite("Hey I also like to just press random keys, but to make sure "
    # "you get a voice you like. Please enter 'M' or 'F', and if you "
    # "don't want to press the shift key it's okay, I promise.")
    if maxAttempts == 0:
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', 300)
        volume = engine.getProperty('volume')
        engine.setProperty('volume', 0.95)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        sleep(0.4)
        questionOne()


main()
