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


        elif action == "tell a joke":

            print ("putting him down, then jump through the Weapon Armory door.")
            return 'escape_pod'

        else:
            print ("DOES NOT COMPUTE!")
            return 'central_corridor'
            
            
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