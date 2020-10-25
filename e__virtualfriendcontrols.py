from f_typewriter import typewrite
import pyttsx3

if __name__ == '__main__':

    typewrite("Welcome to My Buddy Auto!\n"
              "Lets go ahead and get some options set so you can enjoy Auto.")
    typewrite("First we want to get set a voice you would prefer to hear and\n"
              "luckily we have a few different ones to select from.\n")
    typewrite("Since there is a total of 13 different voices we want to make\n"
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
                typewrite("Hey I also like to just press random keys, but to make sure\n"
                          "you get a voice you like. Please enter 'M' or 'F', and if you\n"
                          "don't want to press the shift key it's okay, I promise.")
                maxAttempts = maxAttempts - 1
                continue
            if maxAttempts == 1:
                typewrite("Hey I also like to just press random keys, but to make sure\n"
                          "you get a voice you like. Please enter 'M' or 'F', and if you\n"
                          "don't want to press the shift key it's okay, I promise.")
                maxAttempts = maxAttempts - 1
                continue
            if maxAttempts == 0:
                typewrite("...Okay...I mean that's cool, I'm not mad or anything but I really\n"
                          "would have preferred for you to selected your own choice but here\n"
                          "we are.\n Umm...\n soooo....\n I guess this one will do...Have fun...")
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
        voices = engine.getProperty('voices')
        engine.setProperty()
    from setuptools.command.easy_install import main

    main()
