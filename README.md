# Pet My Familiars, on Flight Rising
## Introduction
This set of python files is a compilation of my hacking around one day.  I have over a hundred familiars I am actively petting in my lair, and I got tired of clicking through and equipping each one.  So, I hacked a script, then hacked some classes, then hacked it even further.

I have a more features in mind, but for now, it does the basic function of finding all the familiars I am currently 'taming' and pets or equips them as needed.

## Getting Started

### Prep your environment
This is a python script, and will need a couple extra packages.  If you already have pip installed, you can run

    >> pip install -r requirements.txt

### Create your Settings file
First, look at the **settings_example.py**.  This file holds all the 'global' settings needed to make the classes work.  Some are optional, a couple are _required_.
  
The easiest way to get your Flight Rising Cookie, in Chrome, is to navigate to your dragon lair page, then open the _inspector_ and right click on any url in the Network tab and _Copy Request Headers_.  Your Cookie will be a string in the result.  _Copy the entire line._

** Don't grab a Cookie set from the www1 domain.  It may not work with the python script. (You should see a PHPSESSID as part of the Cookie string if you are on the correct domain.)

## Running it
Once you have **settings_example.py** setup and your Cookie in it, you can use **pet_my_familiars.py** to pet all your familiars.
    
    >> python pet_my_famliars

Thats it.  The code is set to run _verbosely_ in that file, so you'll see a lot of print out on the command line.  If you don't want that, set `verbose=False` in the classes listed.  

## Errors...
If it breaks or something goes wrong, send me an issue!  I'd like to fix it.

