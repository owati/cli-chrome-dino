import sys
from main import main

is_there_curses = False
try:
    import curses
    is_there_curses = True
except:
    pass

if is_there_curses:
    if len(sys.argv) != 2:
        print("[ERROR]: only one command is needed\nto see help, run 'python dino_cli.py help'")
    else:
        command = sys.argv[1]

        if command in ["start", "help", "highscore"]:
            high = 0
            try:
                with open('data.txt', 'r') as data:
                    high = int(data.read())
            except:
                pass

            if command == 'highscore':
                if high == 0:
                    print("\nYou dont have any record, try playing to have an highscore")
                else:
                    print(f'\nyou current highscore is {high}.')
            elif command == 'help':
                print('''
*********HELP****************
python dino_cli.py <command>

start       : starts the game.
help        : displays this help message.
highscore   : displays the high score if any.
                ''')
            else:
                main(high)
            
        else:
            print(f"\n[ERROR]: '{command}' is not a valid command \nto see help, run 'python dino_cli.py help'")

else:
    print(
"\n[ERROR]: curses not found on this computer..\nIf windows run 'pip install windows-curses"
    )