import sys

from fr_interactions import Bestiary, DragonLair, PetFamiliars, Chests

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


# adjust your verbosity here,
# and whether you want to force the DragonLair & Bestiary
# and whether to open chests after petting familiars
VERBOSITY = 1
FULL_RUN = True
OPEN_CHESTS_AFTER = True


# gets a list of all your dragons, and their equipped familiars
if FULL_RUN or not DRAGON_LIST:
    D = DragonLair(LAIR_ID, FR_COOKIE, verbosity=VERBOSITY)
    DRAGON_LIST = D.get_list()
    print "DRAGON_LIST =", DRAGON_LIST

# get a dict with all your familiars and their current loyalty status
if FULL_RUN or not BESTIARY_BREAKDOWN:
    B = Bestiary(fr_cookie=FR_COOKIE, verbosity=VERBOSITY)
    BESTIARY_BREAKDOWN = B.get_all()
    print "BESTIARY_BREAKDOWN =", BESTIARY_BREAKDOWN

# pets all your currently being tamed familiars & prints the results
pf = PetFamiliars(fr_cookie=FR_COOKIE,
                  equip_dragon=DRAGON_ID,
                  bestiary_breakdown=BESTIARY_BREAKDOWN,
                  dragon_list=DRAGON_LIST,
                  unequip_awakened=True,
                  equip_next_after_awakening=True,
                  pet_awakened=False,
                  verbosity=VERBOSITY)
pf.pet_my_familiars()
pf.print_taming_breakdown()

if OPEN_CHESTS_AFTER:
    C = Chests(FR_COOKIE, verbosity=VERBOSITY)
    C.open_all_chests()
    print "ITEM_MAP =", C.item_map
    C.print_chest_results()
