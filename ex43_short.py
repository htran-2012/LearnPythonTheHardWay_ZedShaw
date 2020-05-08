from sys import exit
from random import randint
from textwrap import dedent



class Scene(object):
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
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
            
        current_scene.enter()

class Death(Scene):
    quips = [
"You died. You kinda suck at this.",
"Such a luser.",
"I have a small puppy that's better at this.",
]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""
The Gothons of Planet Percal #25 have invaded your ship and
destroyed your entire crew. 
A Gothon jumps out. He's blocking the door to the Armory.
"""))
        action = input(">>> ")
        if action == "shoot!":
            print(dedent("""
Quick on the draw you yank out your blaster and fire
it at the Gothon. He eats you.
"""))
            return 'death'
        elif action == "dodge!":
            print(dedent("""
Like a world class boxer you dodge, weave, slip.
The Gothon stomps on your head and eats you.
"""))
            return 'death'
        elif action == "tell a joke":
            print(dedent("""
Lucky for you they made you learn Gothon insults.
While the Gorthon's laughing you run up and put him down, 
then jump through the Weapon Armory door.
"""))
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'



class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
You do a dive roll into the Weapon Armory. The
code is 2 digits.
"""))

        code = f"{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while int(guess) != int(code) and guesses < 9:
            print("BZZZZEDDD!")
            if int(guess) < int(code):
                print('guess < code')
            elif int(guess) > int(code):
                print('guess > code')
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
The container clicks open and the seal breaks.
You ran to the bridge.
"""))
            return 'the_bridge'
        else:
            print(dedent("""
The Gothons blow up the ship from their ship and you die.
"""))
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print(dedent("""
You burst onto the Bridge. The active bomb under your arm.
"""))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
In a panic you throw the bomb .You die.
"""))
            return 'death'

        elif action == "slowly place the bomb":
            print(dedent("""
Now that the bomb is placed
you run to the escape pod to get off this tin can.
"""))

            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"



class EscapePod(Scene):

    def enter(self):
        print(dedent("""
You need to pick one pod to take.
There's 5 pods, which one do you take?
"""))

        good_pod = randint(1,5)
        guess = input("[pod #]> ")


        if int(guess) != good_pod:
            print(dedent(f"""
You jump into pod {guess}.
Wrong pod. You died.
"""))
            return 'death'
        else:
            print(dedent(f"""
You jump into pod {guess}.
Right pod. You won!
"""))

            return 'finished'

class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
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