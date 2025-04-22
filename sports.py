import player_status
import random
import time
#This is the file for the sports career
print("This is the sports career")

def end_game():
    print("\nGame Over!")
    print(f"Final stats for {you.name}:")
    print(f"Position: {you.get_postiton()}")
    print(f"Level: {you.get_level()}")
    print("Thanks for playing!")
    exit()

name = input("Enter your name: ")

you = player_status.player(name)

print("What would you like to play in football?")


while True:
    answer = input("Enter the sport you want to play in football: ")


    if "wide receiver" in answer:
        print("You are a wide receiver")
        you.set_postiton("wide receiver")
        break
    elif "quarterback" in answer:
        print("You are a quarterback")
        you.set_postiton("quarterback")
        break
    elif "running back" in answer:
        print("You are a running back")
        you.set_postiton("running back")
        break
    elif "defensive back" in answer:
        print("You are a defensive back")
        you.set_postiton("defensive back")
        break
    elif "defensive line" in answer:
        print("You are a defensive line")
        you.set_postiton("defensive line")
        break
    elif "linebacker" in answer:
        print("You are a linebacker")
        you.set_postiton("linebacker")
        break
    elif "cornerback" in answer:
        print("You are a cornerback")
        you.set_postiton("cornerback")
        break
    elif "safety" in answer:
        print("You are a safety")
        you.set_postiton("safety")
        break   
    else:
        print("Invalid input")

print("You are a " + you.get_postiton())
print("you play a game of football")

score = random.randint(0, 100)
time.sleep(4)
if score > 10:
    print("You scored a touchdown")
    you.level_up(you.level)
    print("You are now level " + str(you.level))
else:
    print("You lost the game")
    end_game()

time.sleep(4)

if score > 30:
    print("You scored a touchdown")
    you.level_up(you.level)
    print("You are now level " + str(you.level))
else:
    print("You lost the game")
    end_game()

time.sleep(4)
if score > 50:
    print("You scored a touchdown")
    you.level_up(you.level)
    print("You are now level " + str(you.level))
    print("You are a superstar")
    print("You made the all-star team")
else:
    print("You lost the game")
    end_game()

time.sleep(4)
if score == 70:
    print("You scored a touchdown")
    you.level_up(you.level)
    print("You are now level " + str(you.level))
    print("You are a superstar")
    print("You are the MVP of the game")
    exit()
    




    