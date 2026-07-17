# dostar-led-stip

GP0 & GP1: UART port to pycontrol
    
    GP0 -> DIO_B
    
    GP1 -> DIO_A


GP2 & GP3: LED STRIP
    
    GP2 -> CI
    
    GP3 -> DI


To set up the code in a new Raspberry Pi Pico:
1. Connect Raspberry to computer via USB.
2. Copy de file "adafruit-circuitpython-raspberry_pi_pico-en_GB-9.2.8.uf2" to the drive that Raspberry drive. This will automatically close the window and reopen it with circuitpy loaded on the board.
3. Copy the file "adafruit_dotstar.mpy" to the "lib" folder.
4. Replace the "code.py" with the one in the repo.

<img width="800" height="733" alt="image" src="https://github.com/user-attachments/assets/37f4be2a-cb6b-42c9-9305-006b24367914" />
