import sys
from time import sleep
from playsound import playsound
from e__virtualfriendengine import *


def questionOne():
    say = "Hello! My 'name is Autochthonous,,,, but my friends call me Auto....." \
          "I am really happy to be your new autonomous friend!"
    engine.say(say), print("Autochthonous: Hello! My name is Autochthonous, but my friends call me Auto.\n"
                           "I am really happy to be your new autonomous friend!")
    engine.runAndWait()
    sleep(3)

    say = "I'm going to start by asking you a few things so we can get better" \
          "acquainted.... How about we start with your name! What do they call you?"
    engine.say(say), print("Auto: I'm going to start by asking you some information so we can get better\n"
                           "acquainted... How about we start with your name! What do they call you?")
    engine.runAndWait()
    user_name = input('Name: ')
    name = user_name
    sleep(.4)
    file = open("text_files/userinfo.txt", "w")
    file.write("Name: " + name + '\n')
    file.close()
    sleep(3)

    say = "Thank you " + str(name) + "..... The next question is... Where are you from?"
    engine.say(say), print("Auto: Thank you " + str(name) + "! The next question is... Where are you from?")
    engine.runAndWait()

    sleep(3)
    user_location = input('Location: ')
    sleep(.4)
    file = open("text_files/userinfo.txt", "a")
    file.write('\n' + "Location: " + user_location + '\n')
    file.close()
    sleep(3)

    say = "Wonderful!!! I hear " + str(user_location) +\
          " is very nice! I'm from a little place called HKEY_LOCAL_MACHINE... You probably haven't heard of it."\
          "... Okay, what about your FAVORITE color?...... Which one of those lovely shades make you happy?!"
    engine.say(say), print("Auto: Wonderful! I hear " + str(user_location) + " is very nice! I'm from a little\n"
                           "place called HKEY_LOCAL_MACHINE... You probably haven't heard of it. Okay, what\n"
                           "about your favorite color? Which one of those lovely shades make you happy?!")
    engine.runAndWait()

    sleep(3)
    user_fColor = input('Favorite Color: ')
    sleep(.4)
    file = open("text_files/userinfo.txt", "a")
    file.write('\n' + "Favorite Color: " + user_fColor + '\n')
    file.close()
    sleep(3)

    say = "Great!!!!! I like " + str(user_fColor) + ", but my favorite color is #add8e6.. it really looks nice on me!" \
          "While we're talking about colors,,,,, did you know red and yellow stimulate hunger???? I wonder if this is" \
          "why McDonald's is so popular.....Hmm.......Oh! Speaking of food, what is your favorite food?"
    engine.say(say)
    print("Great! I like " + str(user_fColor) + ", but my favorite color is #add8e6 it really looks nice on me!\n" 
          "While we're talking about colors, did you know red and yellow stimulate hunger? I wonder if this is\n"
          "why McDonald's is so popular...Hmm...Oh! Speaking of food, what is your favorite food?")
    engine.runAndWait()

    sleep(2)
    user_fFood = input('Favorite Food: ')
    sleep(.4)
    file = open("text_files/userinfo.txt", "a")
    file.write('\n' + "Favorite Food: " + user_fFood + '\n')
    file.close()
    sleep(2)


    say = "Yummy! " + str(user_fFood) + " sounds like it would be very enjoyable, I would love to try it one day," \
          "but I can only eat cookies, luckily, I always have enough cache for them!, Hahaha...., So far I feel like" \
          "I have really gotten to know you!!!!!!!!! Would you like to know what I know about you so far?"
    engine.say(say)
    print("Yummy! " + str(user_fFood) + " sounds like it would be very enjoyable. I would love to try it one day\n"
          "but I can only eat cookies, luckily, I always have enough cache for them! Hahaha. So far I feel like\n"
          "I have really gotten to know you! Would you like to know what I know about you so far?")
    engine.runAndWait()

    sleep(3)
    user_choice = input('[Y]es or [N]o?: ')
    if user_choice == 'Y' or user_choice == 'y':
        say = "Sure thing!!!!!!! Let me just gather all the information here........."\
              "Processing request.........Checking all information is correct............."
        engine.say(say)
        print('Sure thing! Let me just gather all the needed information....\n'
              'Processing request....\nChecking information....\n')

        engine.runAndWait()

        playsound('Sounds/loadingsound.wav')
        sleep(3)
        sys.stdout.flush()

        say = "Ding!!!!!!!! I Hope I didn't make you wait too long..... I'm a bit antiquated."\
              "Here is what I learned!, " + str(name) + ", your favorite color is, " + str(user_fColor) + \
              "you enjoy eating....," + str(user_fFood) + ",.......and you are from the wonderful world of...."\
              + str(user_location) + ",.....How'd I do? Did I get everything Right?"
        engine.say(say)
        print("Ding! I Hope I didn't make you wait too long..... I'm a bit antiquated.\n"
              "Here is what I learned! " + str(name) + " your favorite color is " + str(user_fColor) +
              " you enjoy eating " + str(user_fFood) + " and you are from the wonderful world of " + str(user_location) +
              "\nHow'd I do? Did I get everything Right?")
        engine.runAndWait()
        sleep(2)
        user_choice = input('[Y]es or [N]: ')
        if user_choice == 'Y' or user_choice == 'y':
            say = "Wonderful!!!!!!! I am learning so much about you and I hope you learned a little about me as well."\
                  ".........This is just a demo and ending now, oggie, boogie, oggie, I'm Out!...Byeeeee...Bye..."\
                  + str(user_name) + "I love you so much!"
            engine.say(say)
            print("Wonderful! I am learning so much about you and I hope you learned a little about me as well.\n"
                  "This is just a demo and ending now,...Bye " + str(user_name))
            engine.runAndWait()
        else:
            print("Oh no...What did I get wrong?")
            wrong_info = input('[N]ame? Favorite [C]olor?, Favorite [F]ood?, or [L]ocation?')


questionOne()
