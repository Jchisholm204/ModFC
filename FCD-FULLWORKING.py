from gpiozero import LED, Button
import pygame

# Define the GPIO
auto = LED(17)
enable = LED(27)

buttonD = Button(5)
buttonA = Button(24)
buttonS = Button(23)
buttonSA = Button(19)
buttonSD = Button(26)

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SCREENCOLOR = (235, 255, 0)


frame_count = 0
frame_rate = 60
start_time = 0

pygame.init()

# Set the height and width of the screen
# 0, 0 is fullscreen
size = [0,0]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("FC Timer")

# Set up Display
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

font = pygame.font.Font(None, 1010)

while True:
                        
    while done == True:
        frame_count = 0
        enable.off()
        if buttonA.is_pressed:
            auto.on()
            start_time = 15
            done = False
        if buttonD.is_pressed:
            auto.off()
            start_time = 105
            done = False
        if buttonSA.is_pressed:
            auto.on()
            start_time = 60
            done = False
        if buttonSD.is_pressed:
            auto.off()
            start_time = 60
            done = False

    while done == False:
        # Set the screen background
        screen.fill(SCREENCOLOR)
        # --- Timer going down ---
        # --- Timer going up ---
        # Calculate total seconds
        total_seconds = start_time - (frame_count // frame_rate)
        if total_seconds < 0:
            total_seconds = 0

        # Divide by 60 to get total minutes
        minutes = total_seconds // 60

        # Use modulus (remainder) to get seconds
        seconds = total_seconds % 60

        # Use python string formatting to format in leading zeros
        output_string =  "{0:02}:{1:02}".format(minutes, seconds)

        # Blit to the screen
        text = font.render(output_string, True, BLACK)

        screen.blit(text, [110, 100])

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # By default this number is (1) I have changed it to (7) to speed up the timer
        frame_count += 7

        # Limit frames per second
        clock.tick(frame_rate)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        enable.on()
        
        if buttonS.is_pressed:
            total_seconds = 0
            done = True
        if total_seconds == 0:
            done = True

