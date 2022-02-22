from random import randint as ran
import time
'''
the major class to be used in the game
'''


class Dinosaur:

    normal =  '''
               ████████
              ███▄███████
              ███████████
              ███████████
              ██████
              █████████
    █       ███████
    ██    ████████████
    ███  ██████████  █
    ███████████████
    ███████████████
     █████████████
      ███████████
        ████████
         ███  ██
         ██    █
         █     █
         ██    ██

        '''
    
    left =  '''







               ████████
              ███▄███████
              ███████████
              ███████████
              ██████
              █████████ 
    █       ███████
    ██    ████████████  
    ███  ██████████  █
    ███████████████
    ███████████████
     █████████████
      ███████████
        ████████
         ███  ██
         ██    ██
         █     
         ██    

        '''
    
    right =  '''







               ████████
              ███▄███████
              ███████████
              ███████████
              ██████
              █████████
    █       ███████
    ██    ████████████
    ███  ██████████  █
    ███████████████
    ███████████████
     █████████████
      ███████████
        ████████
         ███  ██
         █     █
         ██    █
               ██

        '''
    
    def __init__(self):
        self.state = "running"
        self.left_now = True # alternates the leg to simulate running

        self.jump_params = {
            "num" : 0,
            "up": False
        }
    
    def draw(self, playing=True):
        if self.state == "running":
            self.left_now = not self.left_now if playing else self.left_now
            return self.left if self.left_now else self.right
        else:
            
            str_image = ('\n'*( 7 - self.jump_params["num"]) ) + self.normal + ('\n'*(self.jump_params["num"]))
            if self.jump_params["num"] == 0:
                self.state = "running"
            else:
                if self.jump_params["up"]:
                    self.jump_params["num"] += 1
                    if self.jump_params["num"] >= 7:
                        self.jump_params["up"] = False
                else:
                    self.jump_params["num"] -= 1


            return str_image

    def get_height(self):
        return self.jump_params

    def set_state(self, new_state):
        if(self.state == "jumping"):
            pass
        else:
            if new_state == "jumping":
                self.jump_params["num"] = 1
                self.jump_params["up"] = True
            self.state = new_state



class Map:

    def __init__(self,width):
        self.width = width
        self.layers = [
            ['_' for _ in range(self.width)],
            [f'{"-" if x % 7 == 0 else " "}' for x in range(self.width)],
            [f'{"-" if x % 9 == 0 else " "}' for x in range(self.width)]
        ]

    def draw(self, playing=True):
        return_val = [''.join(x) for x in self.layers]
        top_array, mid_array, bot_array = [],[],[]

        if playing:
            for i in self.layers:
                ind = self.layers.index(i)
                i.reverse()
                i.pop()
                i.reverse()


                if ind == 0:
                    top_array = i
                elif ind == 1:
                    mid_array = i
                else: bot_array = i

            top, middle , bottom = ran(0, 100), ran(0, 100), ran(0,100)

            if(top_array[self.width - 2] == '_'):
                if top > 95 :
                    top_array.append(',')
                else:
                    top_array.append('_')
            else:
                val = ''.join(top_array[self.width - 3: self.width - 1])
                if val == "_," or val == '-*':
                    top_array.append("-")
                elif val == ',-':
                    top_array.append('*')
                elif val == '*-':
                    top_array.append(",")
                else:
                    top_array.append("_")
            
            mid_array.append('-' if middle > 70 else " ")
            bot_array.append('-' if bottom > 70 else " ")

            self.layers = [top_array, mid_array, bot_array]

        return return_val



class Cactus:

    cactus_img = '''

      ██       
 █   ████    █
 ██  ████   ██
 ██  ████████
  ██ █████     
   ██████      
     ████      
     ████      
     ████      
    '''
    def __init__(self):
        pass

    def draw(self, offset=None):
        if offset is None:
            return self.cactus_img.split('\n')
        else:
            if offset > 0 :
                return [
                    x[:offset] for x in self.cactus_img.split('\n')
                ]
            else:
                offset = 0 - offset
                try:
                    return [
                        x[offset:] for x in self.cactus_img.split('\n')
                    ]
                except: 
                    return ['', '', '']


