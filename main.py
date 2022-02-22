import curses
from random import randint as ran
import time
import threading
from copy import deepcopy


from charac import Dinosaur, Map, Cactus

std = curses.initscr()
key_pressed = None

dino = Dinosaur()
ground = Map(curses.COLS - 1)

cac = Cactus()

std.clear()
curses.noecho()

std.keypad(True)

GAME_OVER = "GAME OVER.. press space bar to play again"

GAME_BEGIN = "Press space bar to begin"

game_state = "start"

INITIAL_POS = [[150, False], [200, False] , [290, False], [350, False]] # initial postions for the

counter =  [[150, False], [200, False] , [290, False], [350, False]]
playing = False  # if the game is play

score = 0  # the current score
loop = True # the loop variable of the key handler

def detect_key_pressed():
    global key_pressed
    while loop:
        if key_pressed in [32, curses.KEY_UP]:
            time.sleep(0.9)
            key_pressed = 100
        else:
            key_pressed = std.getch()


def update_highscore(score):
    with open('data.txt', 'w') as data:
        data.write(str(score))


def main(high=0):
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
        global playing
        global score
        global game_state

        for i in range(len(counter)):
            
            counter[i][0] -= 3  if playing else 0
            if counter[i][0] < -15:
                del counter[i]
                num = ran(curses.COLS, 400)
                while  num - counter[-1][0] < 50:
                    num = ran(curses.COLS, 400)
                counter.append([num, False])
            elif counter[i][0] < 16:
                if counter[i][1]:
                    pass
                else:
                    dino_height = dino.get_height()
                    if ((dino_height["num"] in [5,6]) and dino_height["up"]):  # if the charcter is not high enough
                        counter[i][1] = True
                    else:
                        playing = False
                        game_state = "end"
                        # if score > high:
                        #     high = score
                        #     # update = threading.Thread(target=update_highscore, args=[hscore])
                        #     # update.start()
            draw_cactus(cac, counter[i][0])                

  
    while True:
        global score
        global playing
        global game_state
        global counter

        # give the keys that were pressed actions...
        if key_pressed == ord('q'):
            global loop
            loop = False
            curses.nocbreak()
            std.keypad(False)
            curses.echo()
            curses.endwin()
            break
        else:
            if playing: 
                if key_pressed == ord(' ') or key_pressed == curses.KEY_UP:
                    dino.set_state("jumping")
                elif key_pressed == ord('p'):
                    playing = False
                else:
                    dino.set_state("running")
            else:
                if key_pressed == ord(' ') or key_pressed == curses.KEY_UP:
                    if game_state == 'start':
                        game_state = "during"
                        playing = True
                    elif game_state == "end":
                        time.sleep(0.5)
                        score = 0
                        counter = deepcopy(INITIAL_POS)
                        game_state = 'start'
                    else:
                        playing = True
            
                    

        # screen drawing section
  
        std.addstr(0,0,(dino.draw(playing)))
        std.addstr(26, 0,ground.draw(playing)[0])
        std.addstr(27, 0,ground.draw(playing)[1])
        std.addstr(28, 0,ground.draw(playing)[2])
        std.addstr(8, curses.COLS - 17,f'scores : {score}')
        std.addstr(9, curses.COLS - 17,f'Hscores : {1049}')

        if game_state == "end":
            std.addstr(8, int(curses.COLS / 2) - int(len(GAME_OVER) / 2) ,GAME_OVER)
        elif game_state == "start":
            std.addstr(8, int(curses.COLS / 2) - int(len(GAME_BEGIN) / 2) ,GAME_BEGIN)


        draw_cactuses(counter)
        

        # score sddition
        score += 1 if playing else 0

        # refresh rate of the game
        std.refresh()
        time.sleep(0.1)



if __name__ == "__main__":
    main()
    print(counter, INITIAL_POS)