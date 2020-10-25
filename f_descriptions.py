import e__virtualfriendengine
from e__virtualfriendengine import *
# This module is to get a description printed for the different voices used.
# 0 = Eva-US, 1 = Mark-US, 2 = Hazel-GB, 3 = David-US, 4 = Mary-US


def description():
    if e__virtualfriendengine.setto == 1:
        print(
            'Option: 1,',
            'Name: Eva,',
            'Gender: F,',
            'Language: English,',
            'Accent: US''')
    elif e__virtualfriendengine.setto == 2:
        print(
            'Option: 2',
            'Name: Mark',
            'Gender: M',
            'Language: English',
            'Accent: US')
    elif e__virtualfriendengine.setto == 3:
        print(
            'Option: 3',
            'Name: Hazel',
            'Gender: F',
            'Language: English',
            'Accent: GB')
    elif e__virtualfriendengine.setto == 4:
        print(
            'Option: 4',
            'Name: Hazel',
            'Gender: F',
            'Language: English',
            'Accent: GB')
