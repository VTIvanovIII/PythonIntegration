# Vasil Ivanov III
# This is a basic adventure game ot show off my Python skills.

# Introduction
print("\nHello, and welcome to The Quest!  This adventure is very simple and ")
print("straight-forward, but you will face combat, manage your items, and ")
print("make choices that affect the story.\n")
print("(Whenever you see this icon (*) at the end of a sentence, make sure the")
print("cursor is next to it and press the Enter key to advance the text.")
input("Try it with this line here!) *")
input("\n(Perfect!  Now, do it once more to advance the story.) *")
print("\nNow then, for there to be an adventure, there must be an adventurer.")
input("Let's create the adventurer now... *")
print("")


# Character Creation
def create_character():
    global name_first
    name_first = input("Please tell me your first name. ")
    global name_last
    name_last = input("And your last name? ")
    global age
    age = input("How old are you? ")
    global age_test
    age_test = age.isnumeric()
    while (age_test == False):
        print("Please provide a real number.")
        age = input("How old are you? ")
        age_test = age.isnumeric()
    global hometown
    hometown = input("Where are you from? ")


create_character()
print("\nLet me make sure I got this right...")
print("Your first name is", name_first + ".")
print("Your last name is", name_last + ".")
print("You are", age, "years old.")
print("You are from", hometown + ".\n")
c_check = input("Is this correct? ")


def char_invalid():
    print("\nLet me ask you again.")
    global c_check
    c_check = input("Is this information correct? ")


def char_false():
    print("\n*sigh* Let's try this again...\n")
    create_character()
    print("\nLet me make sure I got this right...")
    print("Your first name is", name_first + ".")
    print("Your last name is", name_last + ".")
    print("You are", age, "years old.")
    print("You are from", hometown + ".")
    global c_check
    c_check = input("\nIs this correct? ")


while (c_check != "No" and c_check != "no" and c_check != "Yes" and c_check != "yes"):
    char_invalid()
while (c_check == "No" or c_check == "no"):
    char_false()
if (c_check == "Yes" or c_check == "yes"):
    input("\nGreat!  Let me tell you about the setting, then. *")

print("\nOne morning, you received a strange letter from the postman:\n")
print("~" * 71)
print("    Dear", name_first, "of House", name_last + ",")
print("\n       If this letter reaches you, I ask for your aid.")
print("    The evil brute Taniks has taken over the land of Europa.  Our")
print("    people are in grave danger.  I know not how much longer we can")
print("    last.  If the legends are true, I know you will answer our call")
print("    for help.  Please tell me they are true...\n")
print("    Please help us, Sir", name_first + "!\n")
print("    ~ Princess Roselia\n")
print("~" * 71)
print("\nAfter reading the letter, you clutch your fist with determination.")
print("You know what must be done.  You set off for Europa!")
input("\n   The Quest awaits... *")

print("\nNow, before we go any further, your adventurer needs combat stats.")
input("Let's get you equipped. *")


# Stats - Inputs
def stat_defining():
    print("\nAnswer based on a scale of 1 to 10 for each question.")
    global attack
    print("\nIf 1 = Twig limbs and 10 = Arnold Schwarzenegger,")
    attack = int(input("How strong are you? "))
    global defense
    print("\nIf 1 = Paper and 10 = Titanium,")
    defense = int(input("How durable are you? "))
    global speed
    print("\nIf 1 = A snail and 10 = Usain Bolt,")
    speed = int(input("How fast are you? "))
    global intelligence
    print("\nIf 1 = Rocks for Brains and 10 = Super-Mega-Ultra Nerd,")
    intelligence = int(input("How smart are you? "))
    global magic
    print("\nIf 1 = Another sheep in the herd and 10 = Having a lion as a house pet,")
    magic = int(input("How weird are you? "))


stat_defining()
print("\nLet me make sure I got this right...")
print("For how strong you are, you put", str(attack) + ".")
print("For how durable you are, you put", str(defense) + ".")
print("For how fast you are, you put", str(speed) + ".")
print("For how smart you are, you put", str(intelligence) + ".")
print("For how weird you are, you put", str(magic) + ".")
stat_check = input("\nIs this correct? ")


def stat_invalid():
    print("\nLet me ask you again.")
    global stat_check
    stat_check = input("Is this information correct? ")


def stat_false():
    print("\n*sigh* Let's try this again...")
    stat_defining()
    print("\nLet me make sure I got this right...")
    print("For how strong you are, you put", str(attack) + ".")
    print("For how durable you are, you put", str(defense) + ".")
    print("For how fast you are, you put", str(speed) + ".")
    print("For how smart you are, you put", str(intelligence) + ".")
    print("For how weird you are, you put", str(magic) + ".")
    global stat_check
    stat_check = input("\nIs this correct? ")


while (stat_check != "No" and stat_check != "no" and stat_check != "Yes" and stat_check != "yes"):
    stat_invalid()
while (stat_check == "No" or stat_check == "no"):
    stat_false()
if (stat_check == "Yes" or stat_check == "yes"):
    input("\nGreat!  Let me calculate your stats... *")

# Stats - Calculations
max_hp = defense * 20
max_hp += max_hp % 17
current_hp = max_hp
max_mp = magic * 10
current_mp = max_mp
attack **= 2
defense *= 5
agility = (speed * 5) / 2
smarts = (intelligence + int(age)) // 2 - (int(age) // 5)

# Stats - Outputs
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


def menu_stats():
    print("\nStats")
    print("-" * 17)
    # "-" * 17 prints - 17 times
    print("HP:      " + str(current_hp) + "/" + str(max_hp))
    # + in this line and the next line concatenates the strings
    print("MP:      " + str(current_mp) + "/" + str(max_mp))
    print("Atk:     " + str(attack))
    print("Def:     " + str(defense))
    print("Spd:     " + str(agility))
    print("Per:     " + str(smarts))
    print("-" * 17, "\n")
