# Benjamin James
# scm6en

import uvage
import random

c_width = 600
c_height = 800
b_width = 50
b_height = 50
game_on = True
game_over = False
score = 0
ticker = 0

camera = uvage.Camera(c_width,c_height)
box = uvage.from_color(300, 400, 'red', b_width, b_height)

walls = [
    uvage.from_color(0, 400, "white", 0, 800),
    uvage.from_color(600, 400, "white", 0, 800),
    uvage.from_color(300, 800, "white", 800, 1),
    ]

floors = [[
        uvage.from_color(160,c_height-5,'black',320,40),
        uvage.from_color(640,c_height-5,'black',320,40)
        ]]

def tick():
    global game_on,c_width,c_height, box, ticker, walls, floors

    if game_on == True:
        ticker += 1
        camera.clear('white')
        box.yspeed += 1
        box.move_speed()
        if uvage.is_pressing('d'):
            box.x += 10
        if uvage.is_pressing('a'):
            box.x -= 10

        for wall in walls:
            box.move_to_stop_overlapping(wall)
            camera.draw(wall)
        camera.draw(box) 

        box.move_to_stop_overlapping(walls[2])

        for floor in floors:
            for each in floor:
                box.move_to_stop_overlapping(each)
                camera.draw(each)
        
        if floors[-1][0].y < 700:
            randx = random.randint(-270,220)
            floor = [
                uvage.from_color(randx, c_height+50, 'black', 550, 40),
                uvage.from_color((randx+650), c_height+50, 'black', 550, 40)
            ]
            floors.append(floor)
        for floor in floors:
            for each in floor:
                each.y -= 7
                camera.draw(each)
                box.move_to_stop_overlapping(each,-4)
        if len(floors) > 6:
            del(floors[0])
        
        score = str(ticker // 30)
        display_score = uvage.from_text(550,100,score,60,'blue',bold=False,italic=True)
        camera.draw(display_score)

    if box.y < 0:
        box.yspeed = 0
        game_on = False
        for floor in floors:
            for each in floor:
                camera.draw(each)
        camera.draw(uvage.from_text(300, 400, "GAME OVER", 50, "red"))

    camera.display()


tick_ps = 30

uvage.timer_loop(tick_ps,tick)



