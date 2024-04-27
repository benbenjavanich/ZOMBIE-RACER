# import uvage

# c_width = 800
# c_height = 600
# camera = uvage.Camera(c_width, c_height)

# walker_images = uvage.load_sprite_sheet("walk_stand.png",1,6)
# walker = uvage.from_image(100,500,walker_images[-1])
# current_frame = 0

# def move_walker():
#     global current_frame
#     walker_move = False
#     # check which keys are being pressed
#     if uvage.is_pressing("w"):
#         walker.y -= 3
#         walker_move = True
#     if uvage.is_pressing("s"):
#         walker.y += 3
#         walker_move = True
#     if uvage.is_pressing("a"):
#         walker.x -= 3
#         walker_move = True
#     if uvage.is_pressing("d"):
#         walker.x += 3
#         walker_move = True
    
#     if walker_move:
#         current_frame += 0.35
#         if current_frame >= 4:
#             current_frame = 0
#         walker.image = walker_images[int(current_frame)]
#     else:
#         walker.image = walker_images[-1]

# def tick():
#     camera.clear('light blue')
#     move_walker()
#     camera.draw(walker)
#     camera.display()

# tick_ps = 30

# uvage.timer_loop(tick_ps,tick)

import uvage
import random
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
def setup():
    global camera, frame, facing_right, walker_images, walker, floor, walls, score, coins, score_display, badguy
    camera = uvage.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
    frame = 0 # Which is our current index/still image which we want to display
    facing_right = True # We use this to determine which way the stick figure should face. We start with True, because the sprite images are facing right
    walker_images = uvage.load_sprite_sheet("walk_stand.png", rows=1, columns=6)
    walker = uvage.from_image(100, 500, walker_images[-1])
    floor = uvage.from_color(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 5, "black", SCREEN_WIDTH, 10)
    # Step 1
    walls = [
    uvage.from_color(0, SCREEN_HEIGHT / 2, "black", 50, SCREEN_HEIGHT),
    uvage.from_color(SCREEN_WIDTH, SCREEN_HEIGHT / 2, "black", 50, SCREEN_HEIGHT)
    ]
    # Step 3
    score = 0
    # Let's choose random locations from x=50 to 90% of the screen width, we can use randint
    random_x1 = random.randint(50, int(.9*SCREEN_WIDTH))
    random_x2 = random.randint(50, int(.9*SCREEN_WIDTH))
    coins = [
    uvage.from_color(random_x1, 500, "yellow", 12, 12), # We could use uvage.from_image to change the way the coins look
    uvage.from_color(random_x2, 500, "yellow", 12, 12)
    ]
    score_display = uvage.from_text(40, 40, str(score), 50, "brown")
    # badguy = uvage.from_color(200, 500, "red", 40, 40)


def end_game():
    camera.draw(uvage.from_text(300, 300, "OUCH!", 70, "red"))
    # badguy.x = -1000
    for coin in coins:
        coin.x = -1000

def draw_environment():
    camera.draw(floor)
    for w in walls:
        camera.draw(w)

def handle_xmovement():
    global camera, walker, frame, facing_right, walls
    is_moving = False # We use this to determine if the stick figure should be standing or in a walking animation
    if uvage.is_pressing("right arrow"):
        if not facing_right:
            facing_right = True
            walker.flip()
        is_moving = True
        walker.x += 8
    if uvage.is_pressing("left arrow"):
        if facing_right:
            facing_right = False
            walker.flip()
        is_moving = True
        walker.x -= 8
    if not is_moving:
        walker.image = walker_images[5]
    else:
        frame += .3 # Every tick where we move, we are adding to our frame variable. Which represents which image we are currently at. e.g. if frame=1 then we will use the image at index = 1 in walker_images
        if frame >= 5: # Here we reset to the 0th image if we have finished our walking animation
            frame = 0
            walker.image = walker_images[int(frame)]
    # we use the "move_to_stop_overlapping" with each of the walls
    for w in walls:
        walker.move_to_stop_overlapping(w)
    
def handle_ymovement():
    global camera, walker, floor
    # We will set the update the walker's position based on it's speed and also add gravity
    walker.yspeed += 1 # The += 1 represents gravity adding downwards speed every tick; positive y means downward direction
    # We can only jump when the walker is on the ground. If the walker hits the ground it should stop moving.
    if walker.bottom_touches(floor):
        walker.yspeed = 0 # This stops us from falling through the floor
        if uvage.is_pressing("up arrow"): # Check if we should jump
    #walker.yspeed = -20
            walker.yspeed = - 30
    #print(walker.yspeed)
    walker.move_speed() # THIS IS REALLY IMPORTANT, or the walker won't move based on its speed
    camera.draw(walker)

# Step 3:
def handle_coins():
    global camera, coins, score, score_display
    # We need to check if the walker "touches" any coins and update the score
    for coin in coins:
        if walker.touches(coin):
            score += 1
            random_x = random.randint(50, int(.9 * SCREEN_WIDTH)) # Choose a location for a replacement coin
            coin.x = random_x
        camera.draw(coin)
    # Adds red text to the screen to display the player's current score
    score_display = uvage.from_text(40, 40, str(score), 50, "brown")
    camera.draw(score_display)

# def handle_badguy():
#     global camera, walker, badguy
#     # Our bad guy should follow us, the x position of our badguy will become closer to the walker's x position
#     if walker.x < badguy.x:
#         badguy.x -= 1
#     if walker.x > badguy.x:
#         badguy.x += 1
#     # If we hit our bad guy the game ends
#     if badguy.touches(walker):
#         end_game()
#     camera.draw(badguy)

# Our code will always have a tick function
def tick():
    camera.clear('light blue') # Quite often our tick function will end with a call to clear
    draw_environment()
    handle_xmovement()
    handle_ymovement()
    handle_coins()
    # handle_badguy()
    camera.display() # Our tick function will almost always end with a call to display


setup()
uvage.timer_loop(30, tick) # Our code will always call uvage.timer_loop


