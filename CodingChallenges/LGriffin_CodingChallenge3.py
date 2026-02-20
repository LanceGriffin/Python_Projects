# ----------------- Practice Activity 1 -----------------
while True:
    print("Do you like theses football teams? (Type 'done' to finish)")
    Ravens = input("Do you like the Ravens? (yes/no): ")
    Bengals = input("Do you like the Bengals? (yes/no): ")
    Browns = input("Do you like the Browns? (yes/no): ")
    Steelers = input("Do you like the Steelers? (yes/no): ")
    Texans = input("Do you like the Texans? (yes/no): ")
    print("Almost halfway there!")
    Colts = input("Do you like the Colts? (yes/no): ")
    Jaguars = input("Do you like the Jaguars? (yes/no): ")
    Titans = input("Do you like the Titans? (yes/no): ")
    Bils = input("Do you like the Bills? (yes/no): ")
    Dolphins = input("Do you like the Dolphins? (yes/no): ")
    Patriots = input("Do you like the Patriots? (yes/no): ")
    Jets = input("Do you like the Jets? (yes/no): ")
    Broncos = input("Do you like the Broncos? (yes/no): ")
    Chiefs = input("Do you like the Chiefs? (yes/no): ")
    print("Halfway!")
    Raiders = input("Do you like the Raiders? (yes/no): ")
    Chargers = input("Do you like the Chargers? (yes/no): ")
    Bears = input("Do you like the Bears? (yes/no): ")
    Lions = input("Do you like the Lions? (yes/no): ")
    Packers = input("Do you like the Packers? (yes/no): ")
    Vikings = input("Do you like the Vikings? (yes/no): ")
    Falcons = input("Do you like the Falcons? (yes/no): ")
    Panthers = input("Do you like the Panthers? (yes/no): ")
    print("Only a few more teams to go!")
    Saints = input("Do you like the Saints? (yes/no): ")
    Buccaneers = input("Do you like the Buccaneers? (yes/no): ")
    Cowboys = input("Do you like the Cowboys? (yes/no): ")
    Giants = input("Do you like the Giants? (yes/no): ")
    Eagles = input("Do you like the Eagles? (yes/no): ")
    print("Just a few more teams to go!")
    Commanders = input("Do you like the Commanders? (yes/no): ")
    Cardinals = input("Do you like the Cardinals? (yes/no): ")
    Rams = input("Do you like the Rams? (yes/no): ")
    Seahawks = input("Do you like the Seahawks? (yes/no): ")
    SF = input("Do you like the 49ers? (yes/no): ")
    print("Thanks for sharing your opinions on the teams! Let's see how many you like.")
    teams = [Ravens, Bengals, Browns, Steelers, Texans, Colts, Jaguars, Titans, Bils, 
             Dolphins, Patriots, Jets, Broncos, Chiefs, Raiders, Chargers, Bears, Lions, 
             Packers, Vikings, Falcons, Panthers, Saints, Buccaneers, Cowboys, Giants, Eagles, 
             Commanders, Cardinals, Rams, Seahawks, SF]
    count = teams.count("yes")
    print(f"You like {count} teams!")
    break

if exit == input("Do you want to exit the program? (yes/no): "):
    if exit == "yes":
        print("Goodbye!")
    else:
        print("Let's start over!")

# ----------------- Practice Activity 2 -----------------
# For loop for how many letters are in a word
word = input("Enter a word: ")
count = 0
for letter in word:
    count += 1
print(f"The word '{word}' has {count} letters, including spaces.")