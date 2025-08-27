# type: ignore

import board
import busio
import adafruit_dotstar as dotstar

N_DOTS = 72
BILATERAL = True # LEDs will turn on in both sides
FIRST_ITER = True # To ignore the first UART value

dots = dotstar.DotStar(board.GP2, board.GP3, N_DOTS, brightness=0.1)

uart = busio.UART(board.GP0, board.GP1, baudrate=9600)

# # # INITIALIZATION
dots.fill((0, 0, 0))
on_idx = 1

# # # MAIN LOOP
while True:
    
    if uart.in_waiting:
        
        data= uart.read(1)
        uart_value = data[0]
        
        if FIRST_ITER:
            FIRST_ITER = False
            continue
            
        # Turn on the corresponding LED
        if 0 <= uart_value <= 100:
            
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
        
        # Turn off all dots
        if uart_value == 200:
            dots.fill((0, 0, 0))
            
        # Turn on all dots to red
        if uart_value == 201:
            dots.fill((255, 0, 0)) 
        
        # Turn on bilateral mode
        if uart_value == 210:
            BILATERAL = True
                
        # Turn off bilateral mode
        if uart_value == 211:
            BILATERAL = False