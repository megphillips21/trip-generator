from ast import Return
import random
from tkinter import N

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
        return destination_result
    elif dest_answer == "n":
        print("Too Bad! We can pick another..")
        return get_destination()
    

def get_attraction(destination_result):
    if destination_result == "Mammoth":
        attraction = mammoth_get_attract()
        return attraction
    elif destination_result == "Bishop":
        attraction = bish_get_attract()
        return attraction
    elif destination_result == "Bridgeport":
        attraction = bridgeport_get_attract()
        return attraction
    elif destination_result == "Lee Vining":
        attraction = leevining_get_attract()
        return attraction
    elif destination_result == "Lone Pine":
        attraction = lone_get_attract()
        return attraction
   
   
    
def mammoth_get_attract():
    attraction = mammoth_attract_random()
    mammoth_attraction_answer = input(f"How about ....{attraction}? Enter y/n?  ")
    if mammoth_attraction_answer == "y":
        print("YAY! Let's find somewhere to eat!")
        return attraction
    elif mammoth_attraction_answer == "n":
        print("Alright,it's your trip. Let's try another.")
        return mammoth_get_attract()
    

def bish_get_attract():
    attraction = bishop_attract_random()
    bishop_attraction_answer = input(f"How about ....{attraction}? Enter  y/n?  ")
    if bishop_attraction_answer == "y":
        print("YAY! Let's find somewhere to eat!")
        return attraction
    elif bishop_attraction_answer == "n":
        print("Alright,it's your trip. Let's try another.")
        return bish_get_attract()
    

def bridgeport_get_attract():
    attraction = bridgeport_attract_random()
    bridgeport_attraction_answer = input(f"How about ....{attraction}? Enter y/n?  ")
    if bridgeport_attraction_answer == "y":
        print("YAY! Let's find somewhere to eat!")
        return attraction
    elif bridgeport_attraction_answer == "n":
        print("Alright,it's your trip. Let's try another.")
        return bridgeport_get_attract()
    

def leevining_get_attract():
    attraction = leevining_attract_random()
    leevining_attraction_answer = input(f"How about ....{attraction}? Enter  y/n?  ")
    if leevining_attraction_answer == "y":
        print("YAY! Let's find somewhere to eat!")
        return attraction
    elif leevining_attraction_answer == "n":
        print("Alright,it's your trip. Let's try another.")
        return leevining_get_attract()
    

def lone_get_attract():
    attraction = lone_attract_random()
    lone_attraction_answer = input(f"How about ....{attraction}? Enter  y/n?  ")
    if lone_attraction_answer == "y":
        print("YAY! Let's find somewhere to eat!")
        return attraction
    elif lone_attraction_answer == "n":
        print("Alright,it's your trip. Let's try another.")
        return lone_get_attract()
    


def get_resturant(destination_result):
    if destination_result == "Mammoth":
     food = mammoth_get_food()
     return food
       
    elif destination_result == "Bishop":
      food = bishop_get_food()
      return food
        
    elif destination_result == "Bridgeport":
     food = bridgeport_get_food()
     return food
       
    elif destination_result == "Lee Vining":
       food = leevining_get_food()
       return food
        
    elif destination_result == "Lone Pine":
       food =  lone_get_food()
       return food
        


def mammoth_get_food():
    food = mammoth_food_random()
    mammoth_food_answer = input(f"Does {food} sound good? Enter y/n? ")
    if mammoth_food_answer == "y":
        print("That does sound yummy! Let's cover transportation!")  
        return food
    elif mammoth_food_answer == "n":
        print("Bummer, sounded yummy to me.. How about we pick another?")
        return mammoth_get_food()


def bishop_get_food():
    food = bishop_food_random()
    bishop_food_answer = input(f"Does {food} sound good? Enter y/n? ")
    if bishop_food_answer == "y":
        print("That does sound yummy! Let's cover transportation!")
        return food
    elif bishop_food_answer == "n":
        print("Bummer, sounded yummy to me.. How about we pick another?")
        return bishop_get_food()
    

def leevining_get_food():
    food = leevining_food_random()
    leevining_food_answer = input(f"Does {food} sound good? Enter y/n? ")
    if leevining_food_answer == "y":
        print("That does sound yummy! Let's cover transportation!")
        return food
    elif leevining_food_answer == "n":
        print("Bummer, sounded yummy to me.. How about we pick another?")
        return leevining_get_food()
    

def bridgeport_get_food():
    food = bridgeport_food_random()
    bridgeport_food_answer = input(f"Does {food} sound good? Enter y/n? ")
    if bridgeport_food_answer == "y":
        print("That does sound yummy! Let's cover transportation!")
        return food
    elif bridgeport_food_answer == "n":
        print("Bummer, sounded yummy to me.. How about we pick another?")
        return bridgeport_get_food()
    

def lone_get_food():
    food = lone_food_random()
    lone_food_answer = input(f"Does {food} sound good? Enter y/n? ")
    if lone_food_answer == "y":
        print("That does sound yummy! Let's cover transportation!")
        return food
    elif lone_food_answer == "n":
        print("Bummer, sounded yummy to me.. How about we pick another?")
        return lone_get_food()
    

def get_transportation():
    transportation = transportation_random()
    transportation_answer = input(f"Transportation for your day trip is ...{transportation}. Does that sound good? Enter y/n? ")
    if transportation_answer == "y":
        print("Awesome! you are all set for your trip!")
        return transportation
    elif transportation_answer == "n":
        print("No worries, let's try again!")
        return get_transportation()
    

def final_trip ():
    print("                      ")
    print(f"Your day to is all set! You are visiting {destination_result}. You will travel by {transportation} to {attraction}, and eat at {food}. We hope you enjoy the Eastern Sierra! WATCH OUT FOR BEARS!")



welcome()
destination_result= get_destination()
attraction= get_attraction(destination_result)
food= get_resturant(destination_result)
transportation = get_transportation()
trip = final_trip()

