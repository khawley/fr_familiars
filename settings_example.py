"""
 Copy this file to settings.py. It will not be saved in git
 fill in your settings like the examples below.
 The cookie can be copied from your web-browser,
 and may be longer or contain more fields than below
"""


"""
 Required: This is the login credentials for your account.
    DO NOT USE YOUR USERNAME & PASSWORD.  Grab the Cookie Header.
 Example:
    'Cookie: PHPSESSID=askldfjlkanfln;'
"""
FR_COOKIE = ''


"""
  Optional: dragon to use to equip familiars that are in Hoard
  Example: '0123456789'
"""
DRAGON_ID = ''


"""
  Optional: lair id will check when a familiar has gotten a gold,
    and swap for an unequipped familiar, then send to vault
  Example: '0123456789'
"""
LAIR_ID = ''

"""
  Optional: you might run Dragon Lair once and import the list here.
    If you Lair changes frequently or you have many changes in familiars,
    then you may not wish to store your dragons.
  Example Code to get list:
    d = DragonLair(LAIR_ID, FR_COOKIE)
    DRAGON_LIST = d.get_list()
"""
DRAGON_LIST = []


"""
  Optional: you might store your bestiary list here. If you are switching
    from Loyal to Awakened frequently, this list should be updated.
  Example Code to get list:
    b = Bestiary(FR_COOKIE)
    BESTIARY_BREAKDOWN = b.get_all()
"""
BESTIARY_BREAKDOWN = {}
