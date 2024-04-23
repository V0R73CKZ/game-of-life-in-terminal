'''
Hello and welcome to CTHS's game for the python competition
the following code has been commented for ease of understanding
each comment should explain what the code does concisely
'''
# import all of the python modules

import time, math, os, sys, tty, termios

# setting 3 variables to global to be used in functions

global save2, save3, x_input, y_input

# get the input for every key press

def get_input():
    tty.setcbreak(sys.stdin.fileno())
    ch = sys.stdin.read(1)
    return ch

# assign all the needed variables



r, g, b = 255, 255, 255 # red, green, and blue values for the different write colors

black_bg = "\x1b[30m"
black = "\x1b[48;2;0;0;0m1 \033[0m"
red = "\x1b[48;2;255;0;0m2 \033[0m"
green = "\x1b[48;2;0;255;0m3 \033[0m"
blue = "\x1b[48;2;0;0;255m4 \033[0m"
yellow = "\x1b[48;2;255;255;0m5 \033[0m"
cyan = "\x1b[48;2;0;255;255m6 \033[0m"
magenta = "\x1b[48;2;255;0;255m7 \033[0m"
orange = "\x1b[48;2;255;128;0m8 \033[0m"
brown = "\x1b[48;2;100;60;25m9 \033[0m"
purple = "\x1b[48;2;155;0;190m0 \033[0m"

x = math.floor(os.get_terminal_size()[0]/2) # length and width of the canvas

y = os.get_terminal_size()[1]-2

if y <= 2 or x <= 2:
    print('sorry, your terminal is too small')
    exit()
pixel_func = "f" # making the default function the hover function

white_pixel = "\x1b[48;2;255;255;255m  \033[0m" # the string to print a white pixel

rgb_pixel = "\x1b[48;2;"+str(r)+";"+str(g)+";"+str(b)+"m  \033[0m" # the string to print a pixel based on the current r, g, and b values

save1, save2, save3 = [white_pixel]*3 # creating all 3 save variables the white pixel

x_input, y_input = 0, 0 # setting the initial coordinates for the cursor

listx = ([("\x1b[48;2;"+str(r)+";"+str(g)+";"+str(b)+"m  \033[0m")]*x)*y # creating the 2D array / grid for the pixels

listx[x_input+(y_input*x)] = "\x1b[48;2;192;192;192m  \033[0m" # assigning the cursor to be gray

r, g, b = 0, 0, 0 # changing the default write color to black

pixel_values = [] # used for showing where the cursor is when on colored pixels

counter = 0 # used for actions based on the first input

def pixel_set(pixel_func, func_x, func_y):
    global save3, save2, save1, x_input, y_input, funcx, funcy
    if counter != 1:
        save1 = listx[x_input+(y_input*x)]
    save3 = save2
    save2 = listx[(x_input+func_x)+((y_input+func_y)*x)]
    x_input += func_x
    y_input += func_y
    pixel_values = [int(num) for num in save2[save2.find(';')+1:save2.find('m')].split(';')][1:]
    listx[x_input+(y_input*x)] = "\x1b[48;2;"+str(round((128+pixel_values[0])/2))+";"+str(round((128+pixel_values[1])/2))+";"+str(round((128+pixel_values[2])/2))+"m  \033[0m"
    funcx = func_x
    funcy = func_y

# determines the color of where the cursor was previously 

def pixel_func_end(func, func_x, func_y):
    if func == "f":
        if counter == 1:
            listx[(x_input-(func_x))+((y_input-(func_y))*x)] = save1
        else:
            listx[(x_input-func_x)+((y_input-func_y)*x)] = save3
    elif func == "e":
        listx[(x_input-func_x)+((y_input-func_y)*x)] = white_pixel
    elif func == "r":
        listx[(x_input-func_x)+((y_input-func_y)*x)] = rgb_pixel

# chooses what the pixel function is based on earlier input

def pixel_func_start(func_x, func_y):
    if pixel_func == "f":
        pixel_set("f", func_x, func_y)
    if pixel_func == "e":
        pixel_set("e", func_x, func_y)
    if pixel_func == "r":
        pixel_set("r", func_x, func_y)

while True:
    counter += 1
    os.system("clear")
    print((math.floor((os.get_terminal_size()[0]-71)/2)*" ")+"MOVE WITH WASD, PRESS F TO HOVER, R TO WRITE, E TO ERASE, AND C TO PLAY")
    for i in reversed(range(y)):
        for j in range(x):
            print(listx[j+(i*x)], end="")
            if i == x:
                break
        print("")
    input1 = get_input()
    rgb_pixel = "\x1b[48;2;"+str(r)+";"+str(g)+";"+str(b)+"m  \033[0m"
            
    # continues the while loop
    
    if input1 == "f":
        pixel_func = "f"
    elif input1 == "e":
        pixel_func = "e"
    elif input1 == "r":
        pixel_func = "r"
    elif input1 == "c":
        break
    elif input1 == "w":
        if y_input == (y-1):
            continue
        pixel_func_start(0, 1)
        pixel_func_end(pixel_func, 0, 1)
    elif input1 == "a":
        if x_input == 0:
            continue
        pixel_func_start(-1, 0)
        pixel_func_end(pixel_func, -1, 0)
    elif input1 == "s":
        if y_input == 0:
            continue
        pixel_func_start(0, -1)
        pixel_func_end(pixel_func, 0, -1)
    elif input1 == "d":
        if x_input == (x-1):
            continue
        pixel_func_start(1, 0)
        pixel_func_end(pixel_func, 1, 0)
pixels_list = []
for i in range(len(listx)):
    if listx[i] == '\x1b[48;2;192;192;192m  \x1b[0m':
        listx[i] = '\x1b[48;2;255;255;255m  \x1b[0m'
    if listx[i] == '\x1b[48;2;64;64;64m  \x1b[0m':
        listx[i] = '\x1b[48;2;0;0;0m  \x1b[0m'
    if listx[i] == '\x1b[48;2;0;0;0m  \x1b[0m':
        pixels_list.append(i)
#print(listx)
'''
print(x, y)
print(pixels_list)
'''
time_var = 0.1
os.system('clear')
print((math.floor((os.get_terminal_size()[0]-11)/2)*" ")+"NOW PLAYING")
for i in reversed(range(y)):
    for j in range(x):
        print(listx[j+(i*x)], end="")
        if i == x:
            break
    print('')
time.sleep(time_var)
new_list = list(listx)
global c
c = 0
def check_pixel(loop_i):
    if c < 2:
        new_list[loop_i] = '\x1b[48;2;255;255;255m  \x1b[0m'
    if c == 3:
        new_list[loop_i] = '\x1b[48;2;0;0;0m  \x1b[0m'
    if c > 3:
        new_list[loop_i] = '\x1b[48;2;255;255;255m  \x1b[0m'
#doesn't work when height or width is 1. still needs fixing
while True:
    for i in range(len(listx)):
        c = 0
        if i == 0:
            #print("bottom left")
            if listx[i+1] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i+x] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i+1+x] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            check_pixel(i)
        elif i > 0 and i < (x-1):
            #print("bottom")
            if listx[i-1] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i+1] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i-1+x] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i+x] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i+1+x] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            check_pixel(i)
        elif i == (x-1):
            #print("bottom right")
            if listx[i-1] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i-1+x] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i+x] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            check_pixel(i)
        elif (i-(x-1)) % x == 0 and i != (x-1) and i != (x*y)-1:
            #print("right")
            if listx[i-1-x] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i-x] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i-1] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i-1+x] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i+x] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            check_pixel(i)
        elif i == (x*y)-1:
            #print("top right")
            if listx[i-1-x] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i-x] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i-1] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            check_pixel(i)
        elif i > (x*y)-x and i < (x*y)-1:
            #print("top")
            if listx[i-1-x] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i-x] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i+1-x] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i-1] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i+1] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            check_pixel(i)
        elif i == (x*y)-x:
            #print("top left")
            if listx[i-1-x] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i-x] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i+1] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            check_pixel(i)
        elif i % x == 0 and i != 0 and i != (x*y)-x:
            #print("left")
            if listx[i-x] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i+1-x] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i+1] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i+x] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i+1+x] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            check_pixel(i)
        else:
            if listx[i-1-x] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i-x] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i+1-x] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i-1] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i+1] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i-1+x] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i+x] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            if listx[i+1+x] == '\x1b[48;2;0;0;0m  \x1b[0m':
                c += 1
            check_pixel(i)
    listx = list(new_list)
    print((math.floor((os.get_terminal_size()[0]-11)/2)*" ")+"NOW PLAYING")
    for i in reversed(range(y)):
        for j in range(x):
            print(listx[j+(i*x)], end="")
            if i == x:
                break
        print('')
    time.sleep(time_var)
    os.system('clear')