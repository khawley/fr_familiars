import sys

from fr_interactions import Bestiary, DragonLair, PetFamiliars

try:
    from settings import FR_COOKIE, DRAGON_ID, \
        LAIR_ID, DRAGON_LIST, BESTIARY_BREAKDOWN
except ImportError:
    sys.stderr.write("*ERROR: settings.py has not been configured.\n"
                     "        Please see settings_example.py for help.\n")
    exit()

if not FR_COOKIE:
    sys.stderr.write("*ERROR: Please add FR_COOKIE to inputs.py\n"
                     "        See settings_example.py for help.\n")
    exit()

# gets a list of all your dragons, and their equipped familiars
if not DRAGON_LIST:
    D = DragonLair(LAIR_ID, FR_COOKIE, verbose=True)
    DRAGON_LIST = D.get_list()

# get a dict with all your familiars and their current loyalty status
if not BESTIARY_BREAKDOWN:
    B = Bestiary(fr_cookie=FR_COOKIE, verbose=True)
    BESTIARY_BREAKDOWN = B.get_all()

# pets all your currently being tamed familiars & prints the results
pf = PetFamiliars(fr_cookie=FR_COOKIE,
                  equip_dragon=DRAGON_ID,
                  bestiary_breakdown=BESTIARY_BREAKDOWN,
                  dragon_list=DRAGON_LIST,
                  verbose=True)
pf.pet_my_familiars()
pf.print_taming_breakdown()
