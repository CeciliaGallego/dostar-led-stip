import board
import busio
import adafruit_dotstar as dotstar
from time import sleep

N_DOTS = 72

dots = dotstar.DotStar(board.GP2, board.GP3, N_DOTS, brightness=0.1)

# # # INITIALIZATION
dots.fill((255, 0, 0))

# # # MAIN LOOP
while True:

    for i in range(N_DOTS):
        dots.fill((255, 0, 0))
        dots[i] = (255, 255, 255)
        
        sleep(0.5)
