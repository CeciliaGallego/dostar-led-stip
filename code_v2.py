# type: ignore

import board
import busio
import adafruit_dotstar as dotstar
from time import sleep

N_DOTS = 72
BILATERAL = True # LEDs will turn on in both sides
LEDS_OFF = True # Flag to mantain the LEDs off when pycontrol is not running a task

dots = dotstar.DotStar(board.GP2, board.GP3, N_DOTS, brightness=0.1)

uart = busio.UART(board.GP0, board.GP1, baudrate=9600)

# # # INITIALIZATION
# dots.fill((0, 0, 0))
on_idx = 1

# # # MAIN LOOP
while True:
    
    # Keep LEDs off otherwise    
    if LEDS_OFF:
        dots.fill((0, 0, 0))
        sleep(0.1)
                            
    if uart.in_waiting:
        
        data= uart.read(1)
        uart_value = data[0]
        
        # Ignore uart value 0 to avoid errors
        if uart_value == 0:
            continue
        
        # Turn on all dots to red and start leds
        elif uart_value == 201:
            dots.fill((255, 0, 0)) 
            LEDS_OFF = False
        
        # Turn off all dots and stop leds
        elif uart_value == 200:
            dots.fill((0, 0, 0))
            LEDS_OFF = True
            
        # Turn on bilateral mode
        elif uart_value == 210:
            BILATERAL = True
                
        # Turn off bilateral mode
        elif uart_value == 211:
            BILATERAL = False
            
        # Turn on the corresponding LED
        elif 0 < uart_value <= 100:
            
            if BILATERAL:
                # Convert the UART value to an index for the dots
                index = int((uart_value / 100) * (N_DOTS/2 - 2))+1

                # # Set the dot at the calculated index to white
                if 0 < index < N_DOTS-1:
                    dots[on_idx-1] = (255, 0, 0) 
                    dots[on_idx] = (255, 0, 0) 
                    dots[-on_idx-1] = (255, 0, 0) 
                    dots[-on_idx] = (255, 0, 0) 
                    
                    on_idx = index
                    
                    dots[on_idx-1] = (255, 255, 255) 
                    dots[on_idx] = (255, 255, 255) 
                    dots[-on_idx-1] = (255, 255, 255) 
                    dots[-on_idx] = (255, 255, 255) 
                
            else:
                # Convert the UART value to an index for the dots
                index = int((uart_value / 100) * (N_DOTS - 3))+1

                # # Set the dot at the calculated index to white
                if 0 < index < N_DOTS-1:
                    dots[on_idx-1] = (255, 0, 0) 
                    dots[on_idx] = (255, 0, 0) 
                    dots[on_idx+1] = (255, 0, 0)
                    
                    on_idx = index
                    
                    dots[on_idx-1] = (255, 255, 255) 
                    dots[on_idx] = (255, 255, 255) 
                    dots[on_idx+1] = (255, 255, 255)