# Vasil Ivanov III
# This is a basic adventure game ot show off my Python skills.

# Introduction
import math
import random

def main():
    print_intro()
    valid_character = False
    while valid_character == False:
        name_first = input("Please tell me your first name. ")
        if name_first == "admin" or name_first == "Admin":
            name_first = "Vasil"
            name_last = "Ivanov"
            age = 18
            hometown = "Naples"
        else:
            name_last = input("And your last name? ")
            age = input("How old are you? ")
            age_test = age.isnumeric()
            while (age_test == False):
                age = input("\nPlease provide a real number."
                            "\nHow old are you? ")
                age_test = age.isnumeric()
            hometown = input("Where are you from? ")
        # Prof. Vanselow: Define variables in main, use as arguments in calls
        # to functions.
        # Variables get received as parameters in headers of functions.
        valid_character = check_character(name_first, name_last, age, hometown)
    print_backstory(name_first, name_last)
    valid_stats = False
    while valid_stats == False:
        print("\nAnswer based on a scale of 1 to 10 for each question.")
        atk = input("\nIf 1 = Twig limbs and 10 = Arnold Schwarzenegger,"
                    "\nHow strong are you? ")
        if atk == "admin" or atk == "Admin":
            atk = 10
            defense = 10
            speed = 10
            intel = 10
            magic = 10
        else:
            atk_test = atk.isnumeric()
            while (atk_test == False):
                atk = input("\nPlease provide a real number."
                            "\nIf 1 = Twig limbs and 10 = Arnold Schwarzenegge"
                            "r,\nHow strong are you? ")
                atk_test = atk.isnumeric()
            defense = input("\nIf 1 = Paper and 10 = Titanium,"
                            "\nHow durable are you? ")
            defense_test = defense.isnumeric()
            while (defense_test == False):
                defense = input("\nPlease provide a real number."
                                "\nIf 1 = Paper and 10 = Titanium,"
                                "\nHow durable are you? ")
                defense_test = defense.isnumeric()
            speed = input("\nIf 1 = A snail and 10 = Usain Bolt,"
                          "\nHow fast are you? ")
            speed_test = speed.isnumeric()
            while (speed_test == False):
                speed = input("\nPlease provide a real number."
                              "\nIf 1 = A snail and 10 = Usain Bolt,"
                              "\nHow fast are you? ")
                speed_test = speed.isnumeric()
            intel = input("\nIf 1 = Rocks for Brains and 10 = Super-Mega-Ultra"
                          " Nerd,\nHow smart are you? ")
            intel_test = intel.isnumeric()
            while (intel_test == False):
                intel = input("\nPlease provide a real number."
                              "\nIf 1 = Rocks for Brains and 10 = Super-Mega-U"
                              "ltra Nerd,\nHow smart are you? ")
                intel_test = intel.isnumeric()
            magic = input("\nIf 1 = Another sheep in the herd and 10 = Having "
                          "a lion as a house pet,\nHow weird are you? ")
            magic_test = magic.isnumeric()
            while (magic_test == False):
                magic = input("\nPlease provide a real number."
                              "\nIf 1 = Another sheep in the herd and 10 = Hav"
                              "ing a lion as a house pet,"
                              "\nHow weird are you? ")
                magic_test = magic.isnumeric()
        valid_stats = check_stats(atk, defense, speed, intel, magic)
    m_hp = int(defense) * 20
    m_hp += m_hp % 17
    c_hp = m_hp
    m_mp = int(magic) * 10
    c_mp = m_mp
    atk = int(atk)**2
    defense = int(defense)*5
    agility = (int(speed) * 5) / 2
    smarts = (int(intel) + int(age)) // 2 - (int(age) // 5)
    print_stats(m_hp, m_mp, atk, defense, agility, smarts)
    list_stats_short = ["HP", "MP", "Atk", "Def", "Spd", "Per"]
    list_stats = [str(c_hp)+"/"+str(m_hp), str(c_mp)+"/"+str(m_mp), str(atk),
                  str(defense), str(agility), str(smarts)]
    equipment = "Fists"
    list_battle = ["Attack", "Guard", "Use Item", "Check Stats", "Run"]
    list_attack = ["Go Back", equipment, "Magic"]
    list_magic = ["Fire", "Ice", "Lightning", "Earth", "Void"]
    a_battle(list_battle, list_attack, list_stats_short, list_stats, atk,
             agility, list_magic, c_mp, m_mp, defense, c_hp, m_hp)


def print_intro():
    input("\nHello, and welcome to The Quest!  This adventure is very simple"
          "\nand straight-forward, but you will face combat, manage your"
          "\nitems, and make choices that affect the story.\n"
          "\n(Whenever you see this icon (*) at the end of a sentence,"
          "\nmake sure the cursor is next to it and press the Enter key"
          "\nto advance the text.  Try it with this line here!) *")
    input("\n(Perfect!  Now, do it once more to advance the story.) *")
    input("\nNow then, for there to be an adventure, there"
          "\nmust be an adventurer.  Let's create the adventurer now... *")
    print("")


def check_character(name_first, name_last, age, hometown):
    print("\nLet me make sure I got this right..."
          "\nYour first name is", name_first + "."
          "\nYour last name is", name_last + "."
          "\nYou are", age, "years old."
          "\nYou are from",hometown + ".\n")
    c_check_answers = ["Yes", "yes", "YES", "NO", "no", "No"]
    c_check = input("Is this correct? ")
    if (c_check in c_check_answers):
        if (c_check == "Yes" or c_check == "yes" or c_check == "YES"):
            input("\nGreat!  Let me tell you about the setting, then. *")
            return True
        elif (c_check == "No" or c_check == "no" or c_check == "NO"):
            print("\n*sigh* Let's try this again...\n")
            return False
    while (c_check not in c_check_answers):
        c_check = input("\nLet me ask you again.\n"
                        "Is this information correct? ")


def print_backstory(name_first, name_last):
    # Reformat this paragraph
    print("\nOne morning, you received a strange letter from the postman:\n")
    print("~" * 71)
    print("    Dear", name_first, "of House", name_last + ",\n"
          "\n       If this letter reaches you, I ask for your aid."
          "\n    The evil brute Taniks has taken over the land of Europa.  Our"
          "\n    people are in grave danger.  I know not how much longer we"
          "\n    can last.  If the legends are true, I know you will answer ou"
          "r\n    call for help.  Please tell me they are true...\n"
          "\n    Please help us, Sir", name_first + "!\n"
          "\n    ~ Princess Roselia")
    print("~" * 71)
    input("\nAfter reading the letter, you clutch your fist with determination"
          ".\nYou know what must be done.  You set off for Europa!\n"
          "\n   The Quest awaits... *")
    input("\nNow, before we go any further, your adventurer needs "
          "combat stats.\nLet's get you equipped. *")


def check_stats(attack, defense, speed, intelligence, magic):
    print("\nLet me make sure I got this right...")
    print("For how strong you are, you put", str(attack) + ".")
    print("For how durable you are, you put", str(defense) + ".")
    print("For how fast you are, you put", str(speed) + ".")
    print("For how smart you are, you put", str(intelligence) + ".")
    print("For how weird you are, you put", str(magic) + ".")
    s_check_answers = ["Yes", "yes", "YES", "NO", "no", "No"]
    s_check = input("\nAre you happy with these? ")
    if (s_check in s_check_answers):
        if (s_check == "Yes" or s_check == "yes" or s_check == "YES"):
            input("\nGreat!  Let me calculate your stats... *")
            return True
        elif (s_check == "No" or s_check == "no" or s_check == "NO"):
            print("\n*sigh* Let's try this again...\n")
            return False
    while (s_check not in s_check_answers):
        print("\nLet me ask you again.")
        s_check = input("Are you happy with your responses? ")


# Stats - Outputs
def print_stats(max_hp, max_mp, attack, defense, agility, smarts):
    input(". *")
    input(".. *")
    input("... *")
    print("\nYour stats are as follows:\n")
    print("Max HP (Health Points):  " + str(max_hp))
    print("Max MP (Magic Points):   " + str(max_mp))
    print("Attack:  " + str(attack))
    print("Defense: " + str(defense))
    print("Speed: " + str(agility))
    print("Perception:  " + str(smarts))


def menu_stats(c_hp, m_hp, c_mp, m_mp, atk, defense, agility, smarts):
    print("\nStats")
    print("-" * 17)
    # "-" * 17 prints - 17 times
    print("HP:      " + str(c_hp) + "/" + str(m_hp))
    # + in this line and the next line concatenates the strings
    print("MP:      " + str(c_mp) + "/" + str(m_mp))
    print("Atk:     " + str(atk))
    print("Def:     " + str(defense))
    print("Spd:     " + str(agility))
    print("Per:     " + str(smarts))
    print("-" * 17, "\n")


# Define functions to print menus so you can return to them in other menus
def print_menu(menu):
    for index in range(len(menu)):
        print(str(index+1) + ".  ", menu[index])


def print_sub_menu(menu):
    for index in range(len(menu)):
        print(str(index) + ".  ", menu[index])


def print_menu_stats(short, stats):
    print("\nStats")
    print("-" * 17)
    for index in range(len(stats)):
        print(short[index] + ":   " + stats[index])
    print("-" * 17, "\n")
    input("*")


def calculate_damage(attack, defense):
    damage = int(abs((2*attack) - (2*defense)))
    damage *= random.random()
    damage = round(damage)
    return damage


def a_battle(list_battle, list_attack, stats_short, stats_menu, atk, agility,
             list_magic, c_mp, m_mp, defense, c_hp, m_hp):
    input("\nNow that your stats are defined, your quest can finally begin!\n"
          "\nAdvance this text to begin The Quest. *")
    input("\nYou arrive in Europa with nothing but the clothes on you back,"
          "\nyour bare fists, and your trusty satchel.\n"
          "\nAs you cross over the hill, you see a vast, birch forest"
          "\nblocking your path to the local town.  The only way to the town"
          "\nis through the trees, so you head into the forest. *")
    input("\nYou creep through the forest as the forest itself creeps you"
          "\nout.  You hear the rustling of leaves, the chirping of bugs, and"
          "\nthe distant cries of deer.  You continue to walk through...\n"
          "\nWhen suddenly... *")
    input("\nROAR!\n"
          "\nA wild black bear blindsides you!\n\nIts hungry eyes glare at you"
          " as it ponders what piece of you to eat first. *")
    e_name = "black bear"
    e_hp = 100
    e_mp = 0
    e_atk = 5
    e_def = 25
    e_speed = 10
    e_per = 1
    input("\nWhat will you do? *")
    print("\nWill you... \n"
          "(For menus like this, write the number of the action after the "
          "> and press Enter)\n")
    battle_over = 1
    while (battle_over == 1):
        print_menu(list_battle)
        battle_input = input("\n> ")
        if (battle_input == "1"):
            print("Attack with what?")
            print_sub_menu(list_attack)
            attack_input = input("\n> ")
            if (attack_input == "0"):
                battle_over = 1
                print("Will you...\n")
            elif (attack_input == "1"):
                print("You throw a strong jab at the enemy", e_name + ".")
                dmg = calculate_damage(atk, e_def)
                e_hp = e_hp - dmg
                if (e_hp <= 0):
                    print("\nKnockout!\n"
                          "\nThe enemy", e_name, "is dead!")
                    battle_over = 0
                else:
                    print("You dealt", dmg, "damage to the enemy", e_name+".")
                    battle_over = 1
                    print("Will you...\n")
            elif (attack_input == "2"):
                # Run magic attack function
                print("What spell will you use?")
                print_menu(list_magic)
                magic_input = input("\n> ")
                if (magic_input == "1"):
                    print("You cast a fireball and throw it at the enemy",
                          e_name + ".")
                    dmg = calculate_damage(atk, e_def)
                    e_hp = e_hp - dmg
                    c_mp = c_mp - 4
                    if (e_hp <= 0):
                        print("\nKnockout!\n"
                              "\nThe enemy", e_name, "is dead!")
                        battle_over = 0
                    else:
                        print("You dealt", dmg, "damage to the enemy", e_name +
                              "."
                              "\nCurrent MP:    " + str(c_mp) + "/" + str(m_mp)
                              )
                        input("\n*")
                        battle_over = 1
                        print("Will you...\n")
                elif (magic_input == "2"):
                    print("You cast a large icicle and throw it like a spear a"
                          "t the enemy", e_name + ".")
                    dmg = calculate_damage(atk, e_def)
                    e_hp = e_hp - dmg
                    c_mp = c_mp - 4
                    if (e_hp <= 0):
                        print("\nKnockout!\n"
                              "\nThe enemy", e_name, "is dead!")
                        battle_over = 0
                    else:
                        print("You dealt", dmg, "damage to the enemy", e_name +
                              "."
                              "\nCurrent MP:    " + str(c_mp) + "/" + str(m_mp)
                              )
                        input("\n*")
                        battle_over = 1
                        print("Will you...\n")
                elif (magic_input == "3"):
                    print("You channel electricity though your hand and shoot "
                          "it at the enemy", e_name + ".")
                    dmg = calculate_damage(atk, e_def)
                    e_hp = e_hp - dmg
                    c_mp = c_mp - 5
                    if (e_hp <= 0):
                        print("\nKnockout!\n"
                              "\nThe enemy", e_name, "is dead!")
                        battle_over = 0
                    else:
                        print("You dealt", dmg, "damage to the enemy", e_name +
                              "."
                              "\nCurrent MP:    " + str(c_mp) + "/" + str(m_mp)
                              )
                        input("\n*")
                        battle_over = 1
                        print("Will you...\n")
                elif (magic_input == "4"):
                    print("Razor-sharp leaves form in-between your fingers, an"
                          "d you throw them at the enemy", e_name + ".")
                    dmg = calculate_damage(atk, e_def)
                    e_hp = e_hp - dmg
                    c_mp = c_mp - 3
                    if (e_hp <= 0):
                        print("\nKnockout!\n"
                              "\nThe enemy", e_name, "is dead!")
                        battle_over = 0
                    else:
                        print("You dealt", dmg, "damage to the enemy", e_name +
                              "."
                              "\nCurrent MP:    " + str(c_mp) + "/" + str(m_mp)
                              )
                        input("\n*")
                        battle_over = 1
                        print("Will you...\n")
                elif (magic_input == "5"):
                    print("You cast a dark ball of chaotic energy and hurl it "
                          "at the enemy", e_name + ".")
                    dmg = calculate_damage(atk, e_def)
                    e_hp = e_hp - dmg
                    c_mp = c_mp - 6
                    if (e_hp <= 0):
                        print("\nKnockout!\n"
                              "\nThe enemy", e_name, "is dead!")
                        battle_over = 0
                    else:
                        print("You dealt", dmg, "damage to the enemy", e_name +
                              "."
                              "\nCurrent MP:    " + str(c_mp) + "/" + str(m_mp)
                              )
                        input("\n*")
                        battle_over = 1
                        print("Will you...\n")
            else:
                battle_over = 1
        elif (battle_input == "2"):
            print("You guard your face with your arms as the", e_name, "swings"
                  " its paws at you.")
            dmg = calculate_damage(e_atk, defense)
            c_hp = c_hp - dmg
            if (c_hp <= 0):
                print("\nThe blow was too much for you to take!"
                      "\nYou fall to the ground in defeat...\n"
                      "\nYou died.\n\nGame Over\n")
                battle_over = 0
            else:
                print("You took", dmg, "damage from the enemy", e_name + ".")
                battle_over = 1
                print("Will you...\n")
        elif (battle_input == "3"):
            # Run item menu
            print("You don't have any items yet."
                  "\nWill you...\n")
        elif (battle_input == "4"):
            print_menu_stats(stats_short, stats_menu)
            battle_over = 1
            print("Will you...\n")
        elif (battle_input == "5"):
            if (agility >= e_speed):
                print("\nSuccess!\n"
                      "\nYou run away from the enemy", e_name + "!")
                battle_over = 0
            else:
                print("You couldn't escape the enemy", e_name + "."
                      "\nWill you...\n")
        else:
            battle_over = 1
            print("Will you...\n")
    print("\nBattle over!")


main()
