import pyttsx3
from f_descriptions import description

# Initializing the engine.
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
setto = 1
description()
# 0 = Eva-US, 1 = Mark-US, 2 = Hazel-GB, 3 = David-US, 4 = Mary-US

# Setting the speech rate.
rate = engine.getProperty('rate')  # Getting the current speaking rate.
#print(rate)  # Printing the current voice rate.
engine.setProperty('rate', 165)  # Setting the new voice rate.

# Setting the voice volume.
volume = engine.getProperty('volume')  # Getting the current volume level.
#print(volume)  # Printing the current volume level.
engine.setProperty('volume', 0.75)  # Setting the volume level between 0 and 1.

# Setting the virtual friend voice.
voices = engine.getProperty('voices')  # Getting the current voice.
#print(voices)  # Printing the current voice.
engine.setProperty('voice', 'voices.id')  # Setting up the male voice.
# engine.setProperty('voice', voices[0].id)  # Setting up the female voice.

# Saving the voice to a file.
#engine.save_to_file('Testing, testing 1, 2, 3', './Sounds/voices/test.mp3')  # Saving a test mp3.
