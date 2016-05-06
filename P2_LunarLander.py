#
# -------LUNAR LANDER-------
# (it's a oldie but a goodie)
#
def main():
           
    def chooseDifficulty():
        difficulty = raw_input("Select a difficulty level (1-5):")
        try:
            difficulty = int(difficulty)
        except ValueError:
            print "Difficulty level must be a number."
            chooseDifficulty()
        if difficulty < 1 or difficulty > 5:
            print "Difficulty must be between 1 and 5."
            chooseDifficulty()
        else:
            return difficulty

    def chooseInitial():
        defaultVelocity = random.randint(-1000,0)
        velocity = raw_input("Choose initial velocity or enter to accept random assignment: ") or defaultVelocity
        try:
            velocity = int(velocity)
        except ValueError:
            print "Initial velocity must be a number."
            chooseInitial()
        return velocity

    def play(altitude, velocity, fuel, threshold):
        if altitude > 0:
            print "\n ALTITUDE: ",altitude,"     VELOCITY: ",velocity," m/s     FUEL: ",fuel," lbs"
            burn = raw_input("How many pounds of fuel do you want to burn? ")
            if burn.isdigit():
                burn = int(burn)
                #print burn, fuel, type(burn), type(fuel)
                if burn < 0:
                    print "Burn has to be non-negative, of course!"
                    play(altitude, velocity, fuel, threshold)
                elif burn > fuel:
                    print "You don't have that much fuel."
                    play(altitude, velocity, fuel, threshold)
                else:
                    fuel = fuel - burn
                    newVelocity = velocity + burn - gravity
                    altitude = altitude + ((velocity + newVelocity)/2)
                    velocity = newVelocity
                    play(altitude, velocity, fuel, threshold)
            else:
                print "Burn rate must be a number."
                play(altitude, velocity, fuel, threshold)
        else:
            if velocity > threshold:
                print "\nNice Landing!  You arrived on the surface with a velocity of ",velocity," m/s and ",fuel," pounds of fuel left."
                choice=raw_input("Do you want to play again? (y/n)")
                if choice == "y":
                    main()
                else:
                    sys.exit
            else:
                print "\nCRASH!!!  You plowed into the surface with a velocity\
                of ",velocity," m/s."
                choice=raw_input("Do you want to play again? (y/n)")
                if choice == "y":
                    main()
                else:
                    sys.exit


    import sys
    import random
    print "\n\n ************************************ "
    print "\n LUNAR LANDER--An oldie but a goodie! "
    print "\n ************************************ \n"
    print "The object is to start at 10,000 feet and arrive at the surface\
    \nwith vertical velocity below the damage threshold.\
    \nYou will be asked how many pounds of fuel you want to burn\
    \nfor each second of flight. \n\n"
    
    altitude = 10000
    gravity = 10
    burn=0
    difficulty = chooseDifficulty()
    threshold = -22 + (difficulty * 4)
    fuel = 1000-(difficulty * 50)
    print "Level",difficulty,": Your landing velocity must be greater than ",threshold," m/s.\n\n"
    velocity = chooseInitial()
    
    print "\n\n"
    play(altitude, velocity, fuel, threshold)


if __name__ == "__main__":
    main()
