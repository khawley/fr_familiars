import sys
from PetFamiliars import PetFamiliars
from Bestiary import Bestiary

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

# B = Bestiary(fr_cookie=FR_COOKIE, verbose=True)
# B.get_list()
# B.print_beasts_breakdown()

# pf = PetFamiliars(fr_cookie=FR_COOKIE,
#                   equip_dragon=DRAGON_ID, verbose=True)
# pf.get_bestiary()
# pf.pet_my_familiars()
# pf.print_taming_breakdown()
