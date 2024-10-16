# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Nia", image="nia")
define a = Character("Aurelia", image="aurelia")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

   n default "You should be able to pull up by the entrance, I know the family that owns this place."

    "Looking at the rear view mirror I saw the cabbie nod in agreement."

    hide n default 

    "After gathering my belongings from the boot, with the help of the cabbie. I give my thanks and look towards where I'll be staying for the next week."

    scene bg country 

    "Lisette really downplayed how fancy this place is. Though I should have known when she mentioned her great grandfather built this place from scratch."

    "Bzzt!"

    "I couldn't help but let out a sigh."

    "As expected when I looked at my phone my notifications were all work related. Mostly from my boss but there were some from my colleagues."

    "It's like they don't know how to function without me."

    "I can't say I'm all that surprised either. Which is exactly why I packed my work laptop in my suitcase."

    "I'm bound to have to work whilst on holiday anyway."

    "Now that I think about it I haven't seen Lisette and the others for ages."
     
    "Work's been too hectic for me to even think of going out casually for drinks. I'm sure that everyone, except for Lisette I guess, feels something similar otherwise we wouldn't have arranged something like this." 

    return
