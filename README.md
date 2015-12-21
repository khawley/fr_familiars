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
Once you have **settings.py** setup and your Cookie in it, you can use **pet_my_familiars.py** to pet all your familiars.
    
    >> python pet_my_famliars

Thats it.  The code is set to run _medium verbosity_ in that file, so you'll see a lot of print out on the command line.  If you don't want that, you can it to `VERBOSITY=0` near the top of **pet_my_familiars.py**.

It is also set to do a full run, collecting all your dragons and all your beasts.  If you decide to run those separately and store them in the **settings.py** file (instructions are in that file), you can change to `FULL_RUN=False`

## Errors...
If it breaks or something goes wrong, send me an issue!  I'd like to fix it.

## Version Changes
**1.3.1**

 - important bug fix

**1.3**

 - No longer need to pass in the 'Cookie: ' part of the `FR_COOKIE` string.  (will be removed if you do)
  - Now can pass in the `ITEM_MAP` to the Chests, so you can keep building it out, instead of building it once, then trashing it.
  - Will check to confirm that the script is receiving a 'logged in' response.  This check makes sure there is no login form showing.  Is not perfect (example: PetFamiliars) when dependent on partial ajax responses.

**1.2.3**

 - *Bestiary* class has deprecated `pages` as a variable on initialization.  Now, the logic to find the last bestiary page is done automatically (like in *DragonLair* class).

**1.2.2**

 - allows for non logged in state when gathering dragons from a lair

**1.2.1**

 - added an init var to `Chests` to prevent auto opening all chests, unless explicitly passed.  `only_open_specified=True`

**1.2**

 - added new class `Chests` that will open all chests (rusted, iron or gilded) in your hoard.
 - settings file now includes `ITEM_MAP` to help with querying chest items

**1.1**

 - added new variables to PetFamiliars for options on handling newly awakened familiars
    - `unequip_awakened`- if True, will unequip a newly awakened familiar.  False, leaves the familiar attached to its dragon
    - `equip_next_after_awakening`- if True, and unequipping awakening, the original dragon will equip the next available familiar
 - now petting familiars by order of _loyalty_, from Loyal to Wary.  This helps when `equip_next_after_awakening` is True

**1.0.1**

 - added a level of verbosity to print statements
 - stopped Bestiary and DragonLair from adding new and duplicate results to existing data