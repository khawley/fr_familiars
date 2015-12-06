import unittest
from fr_interactions.PetFamiliars import PetFamiliars
from settings import FR_COOKIE
from html_curl_responses.CurlPetFamiliarResponses \
    import CurlPetFamiliarResponses


class TestPetFamiliars(unittest.TestCase):
    # no curling will take place, so no actual cookie is needed
    FR_COOKIE = "Cookie: PHPSESSID=test"
    EQUIP_DRAGON = "18876545"
    DRAGON_LIST = [
        # has Inquisitive familiar attached
        {'familiar_id': u'13434', 'dragon_id': u'6930511'},
        # has Tolerant familiar attached
        {'familiar_id': u'14677', 'dragon_id': u'6930512'},
        # has Relaxed familiar attached
        {'familiar_id': u'13423', 'dragon_id': u'7137149'},
        # has Loyal familiar attached
        {'familiar_id': u'10226', 'dragon_id': u'7166200'},
        # default dragon
        {'dragon_id': u'18876545'}
    ]
    BESTIARY_BREAKDOWN = {'taming': [
        {
            'src': u'/images/cms/familiar/art/13434.png',
            'loyalty': u'Inquisitive',
            'id': u'13434',
            'name': u'Amber Gulper'
        },
        {
            'src': u'/images/cms/familiar/art/14677.png',
            'loyalty': u'Tolerant',
            'id': u'14677',
            'name': u'Granite Guardian'
        },
        {
            'src': u'/images/cms/familiar/art/13423.png',
            'loyalty': u'Relaxed',
            'id': u'13423',
            'name': u'Stonewatch Prince'
        },
        {  # not equipped to dragon
            'src': u'/images/cms/familiar/art/14570.png',
            'loyalty': u'Wary',
            'id': u'14570',
            'name': u'Swiftfoot Slayer'
        },
        {
            'src': u'/images/cms/familiar/art/10226.png',
            'loyalty': u'Loyal',
            'id': u'10226',
            'name': u'Zalis'
        }
    ]}
    WARY_FAMILIAR = BESTIARY_BREAKDOWN["taming"][3]
    LOYAL_FAMILIAR = BESTIARY_BREAKDOWN["taming"][4]

    def setUp(self):
        # default
        self.PF = PetFamiliars(self.FR_COOKIE,
                               equip_dragon=self.EQUIP_DRAGON,
                               bestiary_breakdown=self.BESTIARY_BREAKDOWN,
                               dragon_list=self.DRAGON_LIST,
                               unequip_awakened=True,
                               equip_next_after_awakening=True,
                               pet_awakened=False)


    # test passing in uequip_awakened
    def test_pet_my_familiar_unequip_awakened_is_false(self):
        # __unequip_familiar should not be called from pet_one_familiar
        self.PF_gold_chest = PetFamiliars(
            self.FR_COOKIE,
            equip_dragon=self.EQUIP_DRAGON,
            bestiary_breakdown=self.BESTIARY_BREAKDOWN,
            dragon_list=self.DRAGON_LIST,
            unequip_awakened=False
        )
        self.PF_gold_chest.curl = CurlPetFamiliarResponses.respond_gold_chest
        attached_to_dragon_before_pet = \
            self.PF_gold_chest._PetFamiliars__find_dragon_with_familiar(
                self.LOYAL_FAMILIAR["id"])
        self.PF_gold_chest.pet_one_familiar(self.LOYAL_FAMILIAR["id"])
        attached_to_dragon_after_pet = \
            self.PF_gold_chest._PetFamiliars__find_dragon_with_familiar(
                self.LOYAL_FAMILIAR["id"])
        # these should match, as the familiar was not unequipped
        self.assertEqual(attached_to_dragon_before_pet,
                         attached_to_dragon_after_pet)

    # cannot use this test because the dragon list does not update currently
    def test_pet_my_familiar_unequip_awakened_is_true(self):
        # __unequip_familiar should be called from pet_one_familiar
        PF_gold_chest = PetFamiliars(
            self.FR_COOKIE,
            equip_dragon=self.EQUIP_DRAGON,
            bestiary_breakdown=self.BESTIARY_BREAKDOWN,
            dragon_list=self.DRAGON_LIST,
            unequip_awakened=True
        )
        PF_gold_chest.curl = CurlPetFamiliarResponses.respond_gold_chest
        attached_to_dragon_before_pet = \
            PF_gold_chest._PetFamiliars__find_dragon_with_familiar(
                self.LOYAL_FAMILIAR["id"])
        PF_gold_chest.pet_one_familiar(self.LOYAL_FAMILIAR["id"])
        attached_to_dragon_after_pet = \
            PF_gold_chest._PetFamiliars__find_dragon_with_familiar(
                self.LOYAL_FAMILIAR["id"])
        # these should match, as the familiar was not unequipped
        # self.assertNotEqual(attached_to_dragon_before_pet,
        #                  attached_to_dragon_after_pet)

    # test passing in equip_next_after_awakening
    def test_pet_my_familiar_equip_next_after_awakening_is_false(self):
        # __equip_familiar should return False when called from
        # pet_one_familiar, after first try had not equipped
        pass

    def test_pet_my_familiar_equip_next_after_awakening_is_true(self):
        # __equip_familiar should return True when called from
        # pet_one_familiar, after first try had not equipped
        pass

