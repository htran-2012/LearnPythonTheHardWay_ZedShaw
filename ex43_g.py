from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print ("This scene is not yet configured. Subclass it and implement enter().")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "You died.  You kinda suck at this."
    ]

    def enter(self):
        print (Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print ("The Gothons of Planet Percal #25 have invaded your ship and destroyed")


        action = input("> ")

        if action == "shoot!":

            print ("you are dead.  Then he eats you.")
            return 'death'

        elif action == "dodge!":

            print ("your head and eats you.")
            return 'death'

        elif action == "tell a joke":

            print ("putting him down, then jump through the Weapon Armory door.")
            return 'laser_weapon_armory'

        else:
            print ("DOES NOT COMPUTE!")
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):

        print ("get the bomb.  The code is 3 digits.")
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
           print ("BZZZZEDDD!")
           guesses += 1
           if guesses == 10:
              break
           print ("guesses =", guesses)
           guess = input("[keypad]> ")

        if guess == code:
            print ("The container clicks open and the seal breaks, letting gas out.")

            return 'the_bridge'
        else:
            print ("The lock buzzes one last time and then you hear a sickening")

            return 'death'



class TheBridge(Scene):

    def enter(self):
        print ("You burst onto the Bridge with the netron destruct bomb")


        action = input("> ")

        if action == "throw the bomb":
            print ("In a panic you throw the bomb at the group of Gothons")

            return 'death'

        elif action == "slowly place the bomb":
            print ("You point your blaster at the bomb under your arm")

            return 'escape_pod'
        else:
            print ("DOES NOT COMPUTE!")
            return "the_bridge"


class EscapePod(Scene):

    def enter(self):
        print ("You rush through the ship desperately trying to make it to")


        good_pod = randint(1,5)
        guess = input("[pod #]> ")


        if int(guess) != good_pod:
            print ("You jump into pod %s and hit the eject button." % guess)

            return 'death'
        else:
            print("You jump into pod %s and hit the eject button." % guess)


            return 'finished'

class Finished(Scene):

    def enter(self):
        print ("You won! Good job.")
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()