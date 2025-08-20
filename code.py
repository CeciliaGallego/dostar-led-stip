# Test with the light
import board
import busio
import adafruit_dotstar as dotstar


dots = dotstar.DotStar(board.GP10, board.GP11, 144, brightness=0.1)

uart = busio.UART(board.GP0, board.GP1, baudrate=9600)

# # # INITIALIZATION
dots.fill((255, 0, 0))
n_dots = len(dots)

# # # MAIN LOOP
while True:

    data = uart.read(1)

    if data and len(data) == 1:
        
        index = data[0]
        
        if 1 <= index < n_dots-1:
            dots[index-1] = (255, 255, 255) 
            dots[index] = (255, 255, 255) 
            dots[index+1] = (255, 255, 255) 
        # # Edge cases
        elif index == 0:
            dots[index] = (255, 255, 255) 
            dots[index+1] = (255, 255, 255) 
        elif index == n_dots-1:
            dots[index-1] = (255, 255, 255) 
            dots[index] = (255, 255, 255)