import curses
from random import randint as ran
import time
import threading

from charac import Dinosaur, Map, Cactus

std = curses.initscr()
key_pressed = None

dino = Dinosaur()
ground = Map(curses.COLS - 1)

cac = Cactus()

std.clear()
curses.noecho()

std.keypad(True)

counter = [150, 200, 290, 350]

score = 0
loop = True

def detect_key_pressed():
    global key_pressed
    while loop:
        if key_pressed in [32, curses.KEY_UP]:
            time.sleep(0.5)
            key_pressed = 100
        else:
            key_pressed = std.getch()



def main():
    key_press_thread  = threading.Thread(target=detect_key_pressed)
    key_press_thread.start()

    def draw_cactus(cac, dis):
        if dis >= curses.COLS:
            pass
        else:
            def image_draw(dis=None, col=0):
                count = 0
                for i in cac.draw(dis) : 
                    std.addstr(15 + count, col, i)
                    count += 1
            diff = curses.COLS - dis
            if diff < 15:
                image_draw(diff, dis)
            else:
                if diff > curses.COLS:
                    image_draw(dis=curses.COLS - diff)
                else:
                    image_draw(col=dis)
    
    def draw_cactuses(counter):
        for i in range(len(counter)):
            draw_cactus(cac, counter[i])
            counter[i] -= 3
            if counter[i] < -15:
                del counter[i]
                num = ran(curses.COLS, 400)
                while  num - counter[-1] < 50:
                    num = ran(curses.COLS, 400)
                counter.append(num)


    while True:
        global score
        if key_pressed == ord('q'):
            global loop
            loop = False
            curses.nocbreak()
            std.keypad(False)
            curses.echo()
            curses.endwin()
            break
        else:
            if key_pressed == ord(' ') or key_pressed == curses.KEY_UP:
                dino.set_state("jumping")
            else:
                dino.set_state("running")

        std.addstr(0,0,(dino.draw()))
        std.addstr(26, 0,ground.draw()[0])
        std.addstr(27, 0,ground.draw()[1])
        std.addstr(28, 0,ground.draw()[2])
        std.addstr(5, curses.COLS - 15, f'score: {score}')
        draw_cactuses(counter)
        score += 1
        std.refresh()
        time.sleep(0.1)



if __name__ == "__main__":
    main()
    print(counter)