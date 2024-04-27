# Benjamin James and Tasdiq Bashar
# scm6en and rdk3km

# Game description:
# Side scrolling racing game. 
# Race through a scrolling level with another player. 
# The camera will follow the player in the lead as both players race through a map avoiding obstacles, geographic structures, traps, and (maybe) enemies. 
# First person to reach the end of the level wins that level. 
# Each player will have a certain amount of health that will be reduced if a player comes into contact with a trap or an enemy. 
# There will be collectables that each player could collect in order to give them an advantage during the race. 
# There will be 1 or 3 levels. 
# After every race, the players will move onto the next level. Whoever wins a level gets 1 point. 
# First person to win the level (or best 2/3 if we do 3 levels) will be the winner. 
# Players can lose in 2 ways: losing all of their health points by coming into contact with enemies or traps, or falling out of the POV of the camera. 
# Falling out of the POV of the camera will result in an instant loss of the level.



# 3 Basic features:

# User imput:
# Players will be able to move from side to side, jump, or use collectables. 

# Game Over: 
# Game over when one of the players wins a level or one of them loses all their health points

# Graphics and Images:
# Graphics and Images will be used to create the player Icons, geographic structures, and (maybe) enemies of the game



# 4 Additional featurnes: Scrolling level, Obsticles, Traps and (Maybe) Enemies, Health points, Collectables, 2 Players, Multiple levels 

# Scrolling level: 
# Each level will be a longer map strip with unique geography, obstacles, traps, and (maybe) enemies. Players will start at the 
# left side of the map and navigate to the right side. The camera will follow the player in the lead and if the not leading
# player falls outside the POV of the camera then they will lose.

# Obstacles, Traps, and (maybe) Enemies:
# Obsticles will exist to either slow a player down or help them traverse the map. Some examples would be like mud (slow down)
# or a ladder (help traverse).

# Health points:
# Each player will have 5 hearts of health accounting for 5 health points. If at any point a player loses all 5 
# then they will lose the game. Players can lose health by running into traps and enemies. Players can gain health through
# certain collectables.

# Collectables:
# Collectables will spawn on the map at random locations. Collectables exist to help the player who collects them.
# For example make a player go faster, make them invulnerable to damage against traps, enemies, and obstacles, or even get grant
# additional health points. 

# 2 Players:
# There will be 2 players racing against each other. The camera will follow the player in the lead and if the not leading
# player falls outside the POV of the camera then they will lose.

# Multiples Levels (maybe): 
# We may have 3 levels. If we do, then the first person to win 2/3 levels will in the game. 

#Tasdiq Bashar and Benjamin James

#rdk3km and scm6en

import uvage
import random

sh = 600
sw = 800

camera = uvage.Camera(sw, sh)

# level_background = uvage.from_image(6000, sh//2, "alternative_image.png")
# level_background.size=[12600, 600]



player_1 = uvage.from_color(130, 550, "Red", 15, 15)
player_2 = uvage.from_color(120,550, "Blue",15, 15)

# platforms = [
#     #uvage.from_image(500, 450, "big_block.jpg"),
# uvage.from_image(700, 450, "normal_platform.jpg"),
# uvage.from_image(800, 450, "small_normal.jpg"),
# uvage.from_image(900, 450, "small_block.jpg"),
# uvage.from_image(1000, 450, "power_up.jpg"),





game_over = False

x = 70
timer_count = 40
tx = 0
def tick():
    global x
    global timer_count
    global tx
    global game_over
    # global platforms


    #DRAWING
    camera.clear("black")
    # camera.draw(level_background)
    camera.draw(player_1)
    camera.draw(player_2)
    camera.draw(uvage.from_text(tx-300, 50, "Timer " + str(x), 50, "Purple", bold=True))
    # PLATFORMS
    # for platform in platforms:
    #     camera.draw(platform)
    #     player_1.move_to_stop_overlapping(platform)
    #     player_2.move_to_stop_overlapping(platform)
        #if player_1.touches(platform):
            #if uvage.is_pressing("w"):
                #player_1.speedy -= 20

        #if player_2.touches(platform):
            #if uvage.is_pressing("up arrow"):
                #player_2.speedy -= 20

    #MOVING CAMERA
    if player_1.x >= player_2.x:
        camera.x = player_1.x
        tx = player_1.x
    elif player_2.x >= player_1.x:
        camera.x = player_2.x
        tx = player_2.x

    player_1.yspeed += 1
    player_2.yspeed += 1

    #FLOOR
    floor = uvage.from_color(2500, 610, 'white', 30000, 40)
    camera.draw(floor)
    player_1.move_to_stop_overlapping(floor)
    player_2.move_to_stop_overlapping(floor)

    #INPUT
    if game_over == False:

        if uvage.is_pressing("a"):
            player_1.x -= 15

        if uvage.is_pressing("d"):
            player_1.x += 15

        if uvage.is_pressing("left arrow"):
            player_2.x -= 15

        if uvage.is_pressing("right arrow"):
            player_2.x += 15

        if player_1.touches(floor):
            if uvage.is_pressing("w"):
                player_1.speedy -= 20

        if player_2.touches(floor):
            if uvage.is_pressing("up arrow"):
                player_2.speedy -= 20

    player_1.move_speed()
    player_2.move_speed()


    # TIMER
    timer_count -= 1
    if timer_count % 30 == 0 and game_over == False:
        x -= 1



    #GAME OVER
    flag = uvage.from_color(11500, 550, 'green', 50, 100)
    camera.draw(flag)
    player_1.move_to_stop_overlapping(flag)
    player_2.move_to_stop_overlapping(flag)
    if x == 0 or player_1.touches(flag) or player_2.touches(flag):
        #or player_1.x < (player_2.x - 410) or player_2.x < (player_1.x - 410):
        game_over = True
    if game_over:
        x -= 0
        if player_1.touches(flag) or player_1.x > player_2.x:
            winner_1 = uvage.from_text(tx, 300, 'Red Wins!', 50, 'Red', True, True)
            camera.draw(winner_1)
        elif player_2.touches(flag) or player_2.x > player_1.x:
            winner_2 = uvage.from_text(tx, 300, 'Blue Wins!', 50, 'Blue', True, True)
            camera.draw(winner_2)
        elif player_1.x == player_2.x:
            draw = uvage.from_text(tx, 300, 'Tie!', 50, 'yellow', True, True)
            camera.draw(draw)
    if game_over:
        restart = uvage.from_text(tx, 350, 'press space to restart', 40, 'yellow', True, True)
        camera.draw(restart)
        if uvage.is_pressing('space'):
            game_over = False
            x = 70
            player_1.x = 130
            player_2.x = 80
            player_1.y = 550
            player_2.y = 550
    camera.display()


ticks_per_second = 30
uvage.timer_loop(ticks_per_second, tick)
