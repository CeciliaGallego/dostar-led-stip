# type: ignore

import board
import busio
import adafruit_dotstar as dotstar
import time
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

N_DOTS = 72
BILATERAL = True  # LEDs will turn on in both sides
BIG_LED = False  # False: two LEDs per side; True: four LEDs per side

dots = dotstar.DotStar(board.GP2, board.GP3, N_DOTS, brightness=0.1)

uart = busio.UART(board.GP0, board.GP1, baudrate=9600)

# # # INITIALIZATION
dots.fill((120, 120, 120))
on_idx = 1

# # # MAIN LOOP
while True:

    if uart.in_waiting:

        data = uart.read(1)
        uart_value = data[0]

        # Ignore uart value 0
        if uart_value == 0:
            continue

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

        # Use four LEDs per side in bilateral mode
        if uart_value == 212:
            BIG_LED = True

        # Use two LEDs per side in bilateral mode
        if uart_value == 213:
            BIG_LED = False

        # Turn on the corresponding LED
        if 0 < uart_value <= 100:
            led.value = not led.value

            if BILATERAL:
                if BIG_LED:
                    # Leave room for four adjacent LEDs on each side.
                    index = int((uart_value / 100) * (N_DOTS / 2 - 4)) + 1

                    if 0 < index <= N_DOTS // 2 - 3:
                        # Restore the previous four-LED bilateral cue to red.
                        dots[on_idx - 1] = (255, 0, 0)
                        dots[on_idx] = (255, 0, 0)
                        dots[on_idx + 1] = (255, 0, 0)
                        dots[on_idx + 2] = (255, 0, 0)
                        dots[-on_idx - 3] = (255, 0, 0)
                        dots[-on_idx - 2] = (255, 0, 0)
                        dots[-on_idx - 1] = (255, 0, 0)
                        dots[-on_idx] = (255, 0, 0)

                        on_idx = index

                        dots[on_idx - 1] = (255, 255, 255)
                        dots[on_idx] = (255, 255, 255)
                        dots[on_idx + 1] = (255, 255, 255)
                        dots[on_idx + 2] = (255, 255, 255)
                        dots[-on_idx - 3] = (255, 255, 255)
                        dots[-on_idx - 2] = (255, 255, 255)
                        dots[-on_idx - 1] = (255, 255, 255)
                        dots[-on_idx] = (255, 255, 255)

                else:
                    # Convert the UART value to an index for the dots
                    index = int((uart_value / 100) * (N_DOTS / 2 - 2)) + 1

                    # # Set the dot at the calculated index to white
                    if 0 < index < N_DOTS - 1:
                        dots[on_idx - 1] = (255, 0, 0)
                        dots[on_idx] = (255, 0, 0)
                        dots[-on_idx - 1] = (255, 0, 0)
                        dots[-on_idx] = (255, 0, 0)

                        on_idx = index

                        dots[on_idx - 1] = (255, 255, 255)
                        dots[on_idx] = (255, 255, 255)
                        dots[-on_idx - 1] = (255, 255, 255)
                        dots[-on_idx] = (255, 255, 255)

            else:
                # Convert the UART value to an index for the dots
                index = int((uart_value / 100) * (N_DOTS - 3)) + 1

                # # Set the dot at the calculated index to white
                if 0 < index < N_DOTS - 1:
                    dots[on_idx - 1] = (255, 0, 0)
                    dots[on_idx] = (255, 0, 0)
                    dots[on_idx + 1] = (255, 0, 0)

                    on_idx = index

                    dots[on_idx - 1] = (255, 255, 255)
                    dots[on_idx] = (255, 255, 255)
                    dots[on_idx + 1] = (255, 255, 255)
    else:
        led.value = False
