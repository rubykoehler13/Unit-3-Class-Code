#operations with strings and values

character_class = "wizard"
character_race = "gnome"
character_mana = 50

#I want to print the string "Your character is a wizard gnome with 50 mana"

#by joining strings and values with addition (concatenation)
print("Your character is a " + character_class + " " + character_race + " with " + str(character_mana) + " mana.")
#Use str() to typecast a value to a string type

#by joining strings and values with commas
print("Your character is a", character_class,character_race,"with",character_mana,"mana.")

# f strings
print(f"Your character is a {character_class} {character_race} with {character_mana}")

#multiplication
print("There is an","echo"*5)
#print the following
#ask the user how many times they want to cast their spell if each cast is 10 mana
#if they use more than 50 mana, just default to 5 casts
n = int(input("How many times would you like to cast your spell if each cast is 10 mana? "))
if 0<= n <= 5:
    print(f"The {character_class} {character_race} cast a fire spell {n} times.")
    print("|===o"," ~~ x x x ~~"*n)
else:
    print(f"The {character_class} {character_race} cast a fire spell 5 times.")
    print("|===0", " ~~ x x x ~~ "*5)

#print the following (if n were 3)
#"The {class} {race} cast a fire spell {n} times" (use any method you want)
#|===o  ~~ x x x ~~    ~~ x x x ~~    ~~ x x x ~~ (use multiplication)