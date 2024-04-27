
# Tasdiq Bashar and Benjamin James
# rdk3km and scm6en

#GAME DESCRIPTION
"""
A 2 player side-scrolling, platformer racing game on a hand-crafted and designed single level.
The players race to the flag at the end of the level, traversing through obstacles, platform, and
traps.
"""
#CHANGES SINCE CP1
"""
The assignment asks for changes since CP2, but I am going to assume we are expected to discuss
changes from CP1. We initially said we would make multiple levels, but we decided against it
due to time constraints. We were also going to initially randomize the powerups and level design, 
but we thought it would be more creative to hand design it and think about where everything
should go. We also decided to do sprite animations and timer in addition to the 4 we stated.
"""
#THREE BASIC FEATURES
#1 INPUT
"""
The Player_letters can move left, right, and jump with "a", "d", "w" and the Player_arrows
can do the same with left, right, and up arrows.
"""
#2 GAME OVER
"""
As stated in the description the player wins by reaching the flag at the end of the level first.
However, if the timer runs out prior to reaching the flag, the player who is ahead at the end of the timer wins. If
both players are at the same location it is a draw. If a player falls behind the camera they will deplete
1 health point every second until they die and lose. There are also powerups and traps planted throughout the map.
If the player gets hit by a trap they lose health. If they lose all health points they die and lose.
"""
#3 GRAPHICS
"""
We used graphics for the background, the platforms, the powerups, and the traps.
"""
#FOUR ADDITIONAL FEATURES
#1 SCROLLING LEVEL
"""
We found a image that would be a suitable for a scrolling level background and resized it to be much wider.
The camera centers on the player that is further ahead, and the camera moves with them.
"""
#2 COLLECTIBLES
"""
Three distinct powerups are scattered throughout the map and as well as a bomb trap. 
If collected, the powerup/trap disappears from the map.
The speed powerup makes it so the player moves twice as fast for a brief time.
The warp powerup warps you to the other player (which can help you or hurt you)
The health powerup gives an additional health point
The bomb trap lowers the players' health by two points

"""
#3 TIMER
"""
The timer counts down from 75. Once it reaches 0, the game stops 
and whoever is ahead wins the game. However, the player can also test
how fast they can traverse the level with the timer.
"""
#4 TWO PLAYERS SIMULTANEOUSLY
"""
It is stated in the input section, but there are two players racing to the finish.
Player_letters utilizes a, d, w and Player_arrows utilizes left, right and up arrow to
move left, right, and jump
"""

# ADDITIONAL- ADDITIONAL FEATURES
#5 SPRITE ANIMATIONS
"""
Both of our characters use sprite animations.
"""
import uvage

sh = 600
sw = 800

camera = uvage.Camera(sw, sh)

level_background = uvage.from_image(6000, sh // 2, "alternative_image.png")
level_background.size = [12600, 600]

player_1_image = uvage.load_sprite_sheet("player_images.png", 1, 4)
player_1 = uvage.from_image(100, 550, player_1_image[-1])
player_1.size = [60, 60]
player_2_image = uvage.load_sprite_sheet("player2_images.png", 1, 4)
player_2 = uvage.from_image(100, 550, player_2_image[-1])
player_2.size = [60, 60]
current_frame = 0

player1_move = False
player2_move = False
speedup1 = 1
speedup2 = 1
facing_right1 = True
facing_right2 = True
powered_up1 = False
powered_up2 = False
player_speed = 8

#LEVEL DESIGN
platforms = [
uvage.from_image(1100, 450, "big_block.jpg"),
uvage.from_image(700, 450, "normal_platform.jpg"),
uvage.from_image(800, 450, "small_normal.jpg"),
uvage.from_image(900, 450, "small_block.jpg"),
uvage.from_image(1000, 450, "power_up.jpg"),
uvage.from_image(1600, 350, "normal_platform.jpg"),
uvage.from_image(1950, 320, "small_normal.jpg"),
uvage.from_image(1850, 500, "small_normal.jpg"),
uvage.from_image(2200, 450, "big_block.jpg"),
uvage.from_image(2450, 275, "small_normal.jpg"),
uvage.from_image(2600, 150, "small_normal.jpg"),
uvage.from_image(2750, 420, "normal_platform.jpg"),
uvage.from_image(3075, 235, "big_block.jpg"),
uvage.from_image(3300, 550, "small_block.jpg"),
uvage.from_image(3300, 250, "power_up.jpg"),
uvage.from_image(3700, 325, "normal_platform.jpg"),
uvage.from_image(4000, 375, "big_block.jpg"),
uvage.from_image(4200, 325, "small_normal.jpg"),
uvage.from_image(4300, 450, "small_normal.jpg"),
uvage.from_image(4600, 0, "big_block.jpg"),
uvage.from_image(4600, 350, "big_block.jpg"),
uvage.from_image(4600, 550, "big_block.jpg"),
uvage.from_image(4800, 450, "small_normal.jpg"),
uvage.from_image(4900, 350, "small_normal.jpg"),
uvage.from_image(5050, 240, "small_block.jpg"),
uvage.from_image(5200, 450, "normal_platform.jpg"),
uvage.from_image(5400, 50, "big_block.jpg"),
uvage.from_image(5400, 300, "big_block.jpg"),
uvage.from_image(5650, 300, "small_block.jpg"),
uvage.from_image(5900, 550, "normal_platform.jpg"),
uvage.from_image(6000, 450, "normal_platform.jpg"),
uvage.from_image(6100, 350, "normal_platform.jpg"),
uvage.from_image(6000, 120, "power_up.jpg"),
uvage.from_image(6500, 300, "big_block.jpg"),
uvage.from_image(6700, 225, "small_normal.jpg"),
uvage.from_image(6700, 550, "power_up.jpg"),
uvage.from_image(6800, 275, "small_normal.jpg"),
uvage.from_image(6800, 475, "small_normal.jpg"),
uvage.from_image(7000, 25, "big_block.jpg"),
uvage.from_image(7000, 575, "big_block.jpg"),
uvage.from_image(7550, 350, "normal_platform.jpg"),
uvage.from_image(7550, 450, "normal_platform.jpg"),
uvage.from_image(7550, 550, "normal_platform.jpg"),
uvage.from_image(7550, 350, "normal_platform.jpg"),
uvage.from_image(8270, 450, "normal_platform.jpg"),
uvage.from_image(8270, 550, "normal_platform.jpg"),
uvage.from_image(8600, 475, "small_normal.jpg"),
uvage.from_image(8800, 375, "small_normal.jpg"),
uvage.from_image(9000, 275, "small_normal.jpg"),
uvage.from_image(9200, 475, "small_normal.jpg"),
uvage.from_image(9400, 575, "small_normal.jpg"),
uvage.from_image(9460, 210, "small_normal.jpg"),
uvage.from_image(9525, 400, "small_normal.jpg"),
uvage.from_image(9625, 575, "small_normal.jpg"),
uvage.from_image(9900, 250, "small_normal.jpg"),
uvage.from_image(9950, 575, "small_normal.jpg"),
uvage.from_image(10500, 400, "normal_platform.jpg"),
uvage.from_image(10900, 550, "power_up.jpg"),
uvage.from_image(11000, 550, "power_up.jpg"),
uvage.from_image(11100, 550, "power_up.jpg"),
uvage.from_image(11200, 550, "power_up.jpg"),
uvage.from_image(11300, 550, "power_up.jpg"),
uvage.from_image(11400, 550, "power_up.jpg"),
uvage.from_image(11500, 550, "power_up.jpg"),

]

#Powerup and Trap Locations
lavas = [
    uvage.from_image(8140, 600, 'lava.png'),
    uvage.from_image(9700, 600, 'lava.png'),
]

bombs = [
    uvage.from_image(1630, 250, 'spikedball.png'),
    uvage.from_image(4000, 175, 'spikedball.png'),
    uvage.from_image(7000, 300, 'spikedball.png'),
    uvage.from_image(9200, 400, 'spikedball.png')
]

speed_coins = [
    uvage.from_image(6000, 50, 'speed.png'),
    uvage.from_image(3300, 175, 'speed.png'),
    uvage.from_image(11000, 480, 'speed.png'),
]

warp_coins = [
    uvage.from_image(8270, 380, 'Teleport.png'),
    uvage.from_image(2800, 200, 'Teleport.png'),
uvage.from_image(5200, 50, 'Teleport.png'),
]

health_coins = [
    uvage.from_image(1600, 500, "heart.png"),
    uvage.from_image(6700, 450, "heart.png"),
]

game_over = False

timer = 75
timer_count = 0
tx = 0
powerup_timer1 = 3
powerup_timer2 = 3

health1 = 5
health2 = 5

def tick():
    """
    :return: It doesn't return anything, but it runs nearly all the game's features since there are no helper functions.
    It also draws the entire level. The tick function runs 30
    times each second because we have ticks_per_second equal to 30 in the uvage timer loop.
    """
    global timer, timer_count, tx, game_over, player_speed, platforms
    global speed_coins, warp_coins, health_coins, powered_up1, powered_up2, powerup_timer1, powerup_timer2
    global player1_move, player2_move, speedup1, speedup2, facing_right1, facing_right2, current_frame
    global health1, health2, lavas, bombs

    # DRAWING
    camera.clear("black")
    camera.draw(level_background)
    camera.draw(player_1)
    camera.draw(player_2)
    camera.draw(uvage.from_text(tx - 300, 50, "Timer " + str(timer), 50, "Yellow", bold=True))

    # PLATFORMS
    for platform in platforms:
        camera.draw(platform)
        player_1.move_to_stop_overlapping(platform)
        player_2.move_to_stop_overlapping(platform)

        if player_1.left_touches(platform) or player_1.right_touches(platform):
            player_1.move_to_stop_overlapping(platform)
        if player_1.bottom_touches(platform):
            if player_1.speedy == 0 and uvage.is_pressing("w") and game_over == False:
                player_1.speedy = -20

        if player_2.left_touches(platform) or player_2.right_touches(platform):
            player_2.move_to_stop_overlapping(platform)
        if player_2.bottom_touches(platform): #This prevents the player from double jumping
            if player_2.speedy == 0 and uvage.is_pressing("up arrow") and game_over == False:
                player_2.speedy = -20

    # MOVING CAMERA
    if player_1.x >= player_2.x: #Camera centers on the player that is ahead
        camera.x = player_1.x
        tx = player_1.x
    elif player_2.x >= player_1.x: #Camera centers on the player that is ahead
        camera.x = player_2.x
        tx = player_2.x

    player_1.yspeed += 1
    player_2.yspeed += 1

    # FLOOR
    floor = uvage.from_color(2500, 610, 'black', 30000, 40)
    camera.draw(floor)

    player_1.move_to_stop_overlapping(floor)
    player_2.move_to_stop_overlapping(floor)

    camera.draw(uvage.from_text(tx - 300, 50, "Timer " + str(timer), 50, "yellow", bold=True))

    # INPUT
    if game_over == False:
        if uvage.is_pressing("a"):  #Move left
            player_1.x -= player_speed * speedup1
            if facing_right1:
                facing_right1 = False
                player_1.flip()
            player1_move = True

        if uvage.is_pressing("d"): #Move right
            player_1.x += player_speed * speedup1
            if not facing_right1:
                facing_right1 = True
                player_1.flip()
            player1_move = True

        if player_1.touches(floor):
            if uvage.is_pressing("w"):
                player_1.speedy -= 20

        if uvage.is_pressing("left arrow"): #Move left
            player_2.x -= player_speed * speedup2
            if facing_right2:
                facing_right2 = False
                player_2.flip()
            player2_move = True

        if uvage.is_pressing("right arrow"): #Move right
            player_2.x += player_speed * speedup2
            if not facing_right2:
                facing_right2 = True
                player_2.flip()
            player2_move = True

        if player_2.touches(floor): #Jumping and prevents double jumping
            if uvage.is_pressing("up arrow"):
                player_2.speedy -= 20

    # SPRITE
    if player1_move:  #Animations for sprite
        current_frame += 0.29
        if current_frame >= 4:
            current_frame = 0
        player_1.image = player_1_image[int(current_frame)]
    else:
        player_1.image = player_1_image[1]

    if player2_move: #Animations for sprite
        current_frame += 0.29
        if current_frame >= 4:
            current_frame = 0
        player_2.image = player_2_image[int(current_frame)]
    else:
        player_2.image = player_2_image[1]

    player_1.move_speed()
    player_2.move_speed()

    # TIMER
    timer_count -= 1
    if timer_count % 30 == 0 and game_over == False: #Every thirtieth tick/every second the timer goes down one
        timer -= 1
        if powered_up1:  #Powerup timer is set at 3 seconds and decreases by one each second once powerup is activated
            powerup_timer1 -= 1
        if powered_up2:  #Powerup timer is set at 3 seconds and decreases by one each second once powerup is activated
            powerup_timer2 -= 1

    # HEALTH
    camera.draw(uvage.from_text(tx + 300, 50, "Health " + str(int(health1)), 40, "Red", bold=True))
    camera.draw(uvage.from_text(tx + 300, 80, "Health " + str(int(health2)), 40, "Blue", bold=True))

    # POWERUPS
    for s_coin in speed_coins:
        s_coin.size = [30, 30]
        if player_1.touches(s_coin):
            speed_coins.remove(s_coin)
            powerup_timer1 = 2
            powered_up1 = True
            if powered_up1:
                speedup1 = 2
        if player_2.touches(s_coin):
            speed_coins.remove(s_coin)
            powerup_timer2 = 2
            powered_up2 = True
        camera.draw(s_coin)
    if powered_up1: #When powerup is activated the players speed doubles
        speedup1 = 2
        if powerup_timer1 <= 0: #When powerup ends the speed goes back to normal
            powered_up1 = False
            speedup1 = 1
    if powered_up2: #When powerup is activated the players speed doubles
        speedup2 = 2
        if powerup_timer2 <= 0: #When powerup ends the speed goes back to normal
            powered_up2 = False
            speedup2 = 1

    for warp_coin in warp_coins:
        warp_coin.size = [40, 40]
        if player_1.touches(warp_coin):
            warp_coins.remove(warp_coin)
            player_1.x = player_2.x   #Player warps to the other player once warp is collected
            player_1.y = player_2.y
        if player_2.touches(warp_coin):
            warp_coins.remove(warp_coin)   #Player warps to the other player once warp is collected
            player_2.x = player_1.x
            player_2.y = player_1.y
        camera.draw(warp_coin)

    for h_coin in health_coins:
        h_coin.size = [50, 50]
        if player_1.touches(h_coin): #Health increases by 1
            health_coins.remove(h_coin)
            health1 += 1
        if player_2.touches(h_coin): #Health increases by 1
            health_coins.remove(h_coin)
            health2 += 1
        camera.draw(h_coin)

    # TRAPS
    for lava in lavas:
        lava.size= [2000, 30]
        camera.draw(lava)
        player_1.move_to_stop_overlapping(lava)
        player_2.move_to_stop_overlapping(lava)
        if player_1.touches(lava) and timer_count % 10 == 0 and game_over == False: #Lava decreases health
            health1 -= 0.5
        if player_2.touches(lava) and timer_count % 10 ==0 and game_over == False: #Lava decreases health
            health2 -= 0.5

        if player_1.left_touches(lava) or player_1.right_touches(lava):
            player_1.move_to_stop_overlapping(lava)
        if player_1.bottom_touches(lava):
            if player_1.speedy == 0 and uvage.is_pressing("w"): #Prevents double jumping
                player_1.speedy = -20

        if player_2.bottom_touches(lava):
            if player_2.speedy == 0 and uvage.is_pressing("up arrow"): #Prevents double jumping
                player_2.speedy = -20
        if player_2.left_touches(lava) or player_2.right_touches(lava):
            player_2.move_to_stop_overlapping(lava)

    for bomb in bombs:
        bomb.size=[30, 30]
        camera.draw(bomb)
        if player_1.touches(bomb): #Removes powerup and decreases health by 2
            bombs.remove(bomb)
            health1 -= 2
        if player_2.touches(bomb): #Removes powerup and decreases health by 2
            bombs.remove(bomb)
            health2 -= 2
    
    #Off Screen
    if player_1.x < (player_2.x - 420) and timer_count % 10 == 0 and game_over == False: #If the player falls off screen their health depletes
        health1 -= 0.5
    if player_2.x < (player_1.x - 420) and timer_count % 10 ==0 and game_over == False: #If the player falls off screen their health depletes
        health2 -= 0.5

    # GAME OVER
    flag = uvage.from_image(11500, 450, 'flag.png')
    camera.draw(flag)
    flag.size = [20,20]
    player_1.move_to_stop_overlapping(flag)
    player_2.move_to_stop_overlapping(flag)
    if timer == 0 or player_1.touches(flag) or player_2.touches(flag):#Game over if one of the players reach the flag and game over if the timer runs out.
        game_over = True
        if game_over:
            timer -= 0
            if player_1.touches(flag) or player_1.x > player_2.x: #If the timer runs out the player that is ahead wins
                winner_1 = uvage.from_text(tx, 300, 'Player_letters Wins!', 50, 'Red', True, True)
                camera.draw(winner_1)
            elif player_2.touches(flag) or player_2.x > player_1.x:
                winner_2 = uvage.from_text(tx, 300, 'Player_arrows Wins!', 50, 'Blue', True, True)
                camera.draw(winner_2)
            elif player_1.x == player_2.x:
                draw = uvage.from_text(tx, 300, 'Tie!', 50, 'Purple', True, True)
                camera.draw(draw)

    if health2 <= 0 and health1 <= 0: #If both healths are zero the game is a tie
        game_over = True
        if game_over:
            draw = uvage.from_text(tx, 300, 'Tie!', 50, 'Purple', True, True)
            camera.draw(draw)
    elif health1 <= 0.5: #Game over if the player runs out of health
        game_over = True
        if game_over:
            winner_1 = uvage.from_text(tx, 300, 'Player_arrows Wins!', 50, 'Blue', True, True)
            camera.draw(winner_1)
    elif health2 <= 0.5:
        game_over = True
        if game_over:
            winner_2 = uvage.from_text(tx, 300, 'Player_letters Wins!', 50, 'Red', True, True)
            camera.draw(winner_2)
    if game_over:
        player_1.image = player_1_image[1]
        player_2.image = player_2_image[1]
    camera.display()


ticks_per_second = 30
uvage.timer_loop(ticks_per_second, tick)