import uvage

camera = uvage.Camera(800,600)


p2 = uvage.from_color(400, 400, "yellow", 100, 100)
p1 = uvage.from_color(400, 400, "red", 100, 100)


def tick():
    global p1, p2, camera
    camera.clear('black')
    camera.draw(p2)
    camera.draw(p1)
    camera.display()

ticks_per_second = 60

# keep this line the last one in your program
uvage.timer_loop(ticks_per_second, tick)