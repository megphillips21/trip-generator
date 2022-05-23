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
    destination_result= random.choice(destinations_list)
    return destination_result

def transportation_random ():
    transportation_result= random.choice(transporations_list)
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

welcome()


def confirm_destination(final_destination):
    user_answer = input(f"How does spending the day in {final_destination} sound? Enter yes/no ") 
    if user_answer == "yes" or "Yes":
        print("Great, let's pick something to do!")
    elif user_answer == "no" or "No":
        print( "Ok.. let's look for somewhere else")
    else print("Try again!")

confirm_destination(final_destination)