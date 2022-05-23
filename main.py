import random

destinations_list = ["Mammoth","Bishop","Lone Pine","Bridgeport", "Lee Vining"]
transporations_list = ["Car","Tour Bus","Horse", "Town Trolley", "Bicycle"]

# Mammoth lists of Resturants and Attractions
mammoth_rests_list = ["Robertos","Burgers","Giovanni's","The Stove","The Yodler"]
mammoth_attracts_list = ["Go Skiing", "Visit Hot Springs", "Look for Bears", "Go for a Hike", "Play golf"]

# Bishop lists of Resturants and Attractions
bishop_rests_list = ["Whiskey Creek", "Yamitani", "Salsa's", "El Pollo Loco", "Schat's Bakery"]
bishop_attracts_list= ["Float the River", "Go Rock Climbing", "Go Fishing", "Horsebackriding", "Have an Offroad Adventure"]

# Lone Pine lists of Resturants and Attractions
lone_rests_list = ["Merry-go-Round", "Jersey Mikes", "Still Life Cafe", "Coppertop BBQ", "Two Brothers Pizza"]
lone_attracts_list= ["Climb Mt. Whitney", "Walk along the John Muir Trail", "Go Camping", "Visit Death Valley", "Tour Scotty's Castle"]

# Bridgeport lists of Resturants and Attractions
bridgeport_rests_list = ["Virginia Creek", "Rhino's Bar and Grill", "Bridgeport Cafe", "Growler's Cafe"]
bridgeport_attacts_list = ["Visit Bodie Ghost Town", "Fly fish on the River", "Go Boating on the lake", "Look at the Cows"]

# Lee Vining lists of Resturants and Attractions
leevining_rests_list = ["Mono Cone", "Mobile Mart", "Mono Inn", "Tioga Resort", "Brine Shrimp Factory"]
leevining_attracts_list = ["Mono Lake", "Yosemite National Park", "Inyo Craters", "Visit the Sand Tuffas", "Double Eagle Spa"]

def welcome ():
    print("              ")
    print("Welcome to the Eastern Sierra, lets create a day of adventure!")
    print("First let's pick your destination!")


def destination_random ():
    destination_result = random.choice(destinations_list)
    print(destination_result)
    return destination_result
    

def transportation_random ():
    transportation_result = random.choice(transporations_list)
    return transportation_result

def mammoth_attract_random ():
    mammoth_attract_result= random.choice(mammoth_attracts_list)
    return mammoth_attract_result

def mammoth_food_random ():
    mammoth_food_result= random.choice(mammoth_rests_list)
    return mammoth_food_result

def bishop_attract_random ():
    bishop_attract_result= random.choice(bishop_attracts_list)
    return bishop_attract_result

def bishop_food_random():
    bishop_food_result = random.choice(bishop_rests_list)
    return bishop_food_result

def lone_attract_random ():
    lone_attract_result= random.choice(lone_attracts_list)
    return lone_attract_result

def lone_food_random ():
    lone_food_result= random.choice(lone_rests_list)
    return lone_food_result

def bridgeport_attract_random ():
    bridgeport_attract_result= random.choice(bridgeport_attacts_list)
    return bridgeport_attract_result

def bridgeport_food_random():
    bridgeport_food_result = random.choice(bridgeport_rests_list)
    return bridgeport_food_result

def leevining_attract_random ():
    leevining_attract_result= random.choice(leevining_attracts_list)
    return leevining_attract_result

def leevining_food_random():
    leevining_food_result = random.choice(leevining_rests_list)
    return leevining_food_result

def get_destination():
    destination_result = destination_random()
    dest_answer = input(f"How would you like to spend the day in {destination_result}? Enter y/n?  ")
    if dest_answer == "y":
        print("Great, Let's find something to do!")
    elif dest_answer == "n":
        print("Too Bad! We can pick another..")
        get_destination()
    return destination_result

def get_attraction(destination_result):
    if destination_result == "Mammoth":
      mammoth_get_attract()
    elif destination_result == "Bishop":
        bish_get_attract()
    elif destination_result == "Bridgeport":
        bridgeport_get_attract()
    elif destination_result == "Lee Vining":
        leevining_get_attract()
    elif destination_result == "Lone Pine":
        lone_get_attract()
   
    
def mammoth_get_attract():
    mammoth_attraction = mammoth_attract_random()
    mammoth_attraction_answer = input(f"How about ....{mammoth_attraction}? Enter y/n?  ")
    if mammoth_attraction_answer == "y":
        print("YAY! Let's find somewhere to eat!")
    elif mammoth_attraction_answer == "n":
        print("Alright,it's your trip. Let's try another.")
        mammoth_get_attract()

def bish_get_attract():
    bishop_attraction = bishop_attract_random()
    bishop_attraction_answer = input(f"How about ....{bishop_attraction}? Enter  y/n?  ")
    if bishop_attraction_answer == "y":
        print("YAY! Let's find somewhere to eat!")
    elif bishop_attraction_answer == "n":
        print("Alright,it's your trip. Let's try another.")
        bish_get_attract()

def bridgeport_get_attract():
    bridgeport_attraction = bridgeport_attract_random()
    bridgeport_attraction_answer = input(f"How about ....{bridgeport_attraction}? Enter y/n?  ")
    if bridgeport_attraction_answer == "y":
        print("YAY! Let's find somewhere to eat!")
    elif bridgeport_attraction_answer == "n":
        print("Alright,it's your trip. Let's try another.")
        bridgeport_get_attract()

def leevining_get_attract():
    leevining_attraction = leevining_attract_random()
    leevining_attraction_answer = input(f"How about ....{leevining_attraction}? Enter  y/n?  ")
    if leevining_attraction_answer == "y":
        print("YAY! Let's find somewhere to eat!")
    elif leevining_attraction_answer == "n":
        print("Alright,it's your trip. Let's try another.")
        leevining_get_attract()

def lone_get_attract():
    lone_attraction = lone_attract_random()
    lone_attraction_answer = input(f"How about ....{lone_attraction}? Enter  y/n?  ")
    if lone_attraction_answer == "y":
        print("YAY! Let's find somewhere to eat!")
    elif lone_attraction_answer == "n":
        print("Alright,it's your trip. Let's try another.")
        lone_get_attract()


def get_resturant(destination_result):
    if destination_result == "Mammoth":
      mammoth_get_food()
    elif destination_result == "Bishop":
        bish_get_food()
    elif destination_result == "Bridgeport":
        bridgeport_get_food()
    elif destination_result == "Lee Vining":
        leevining_get_food()
    elif destination_result == "Lone Pine":
        lone_get_food()

def mammoth_get_food():
    mammoth_food = mammoth_food_random()
    mammoth_food_answer = input(f"Does {mammoth_food} sound good? Enter y/n? ")
    if mammoth_food_answer == "y":
        print("That does sound yummy! Let's cover transportation!")
    elif mammoth_food_answer == "n":
        print("Bummer, sounded yummy to me.. How about we pick another?")
        mammoth_get_food()

def bishop_get_food():
    bishop_food = bishop_food_random()
    bishop_food_answer = input(f"Does {bishop_food} sound good? Enter y/n? ")
    if bishop_food_answer == "y":
        print("That does sound yummy! Let's cover transportation!")
    elif bishop_food_answer == "n":
        print("Bummer, sounded yummy to me.. How about we pick another?")
        bishop_get_food()

def leevining_get_food():
    leevining_food = leevining_food_random()
    leevining_food_answer = input(f"Does {leevining_food} sound good? Enter y/n? ")
    if leevining_food_answer == "y":
        print("That does sound yummy! Let's cover transportation!")
    elif leevining_food_answer == "n":
        print("Bummer, sounded yummy to me.. How about we pick another?")
        leevining_get_food()


def bridgeport_get_food():
    bridgeport_food = bridgeport_food_random()
    bridgeport_food_answer = input(f"Does {bridgeport_food} sound good? Enter y/n? ")
    if bridgeport_food_answer == "y":
        print("That does sound yummy! Let's cover transportation!")
    elif bridgeport_food_answer == "n":
        print("Bummer, sounded yummy to me.. How about we pick another?")
        bridgeport_get_food()

def lone_get_food():
    lone_food = bishop_food_random()
    lone_food_answer = input(f"Does {lone_food} sound good? Enter y/n? ")
    if lone_food_answer == "y":
        print("That does sound yummy! Let's cover transportation!")
    elif lone_food_answer == "n":
        print("Bummer, sounded yummy to me.. How about we pick another?")
        bishop_get_food()

welcome()
destination_result= get_destination()
get_attraction(destination_result)




# def confirm_destination(final_destination):
#     user_answer = input(f"How does spending the day in {final_destination} sound? Enter yes/no ") 
#     if user_answer == "yes" or "Yes":
#         print("Great, let's pick something to do!")
#     elif user_answer == "no" or "No":
#         print( "Ok.. let's look for somewhere else")
#     else print("Try again!")

# confirm_destination(final_destination)