"""
 Show how to put a timer on the screen.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

"""
from gpiozero import LED, Button
import pygame

# Define the GPIO
auto = LED(17)
enable = LED(27)

buttonD = Button(5)
buttonA = Button(24)
buttonS = Button(23)

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SCREENCOLOR = (235, 255, 0)

pygame.init()

# Set the height and width of the screen
# 0, 0 is fullscreen
size = [0, 0]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("FC Timer")

# Loop until the user clicks the close button.
done = True

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

font = pygame.font.Font(None, 500)

frame_count = 0
frame_rate = 60

# MODIFY START_TIME VARIABLE TO 15 FOR AUTO AND 105 FOR DRIVER AND 60 FOR ALL SKILLS
start_time = 0

while True:
    while done:
        enable.off()
        if buttonA.is_pressed:
            auto.on()
            start_time = 15
            done = False
        if buttonD.is_pressed:
            auto.off()
            start_time = 105
            done = False

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

        # Set the screen background
        screen.fill(SCREENCOLOR)

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        # --- Timer going up ---
        # Calculate total seconds
        total_seconds = frame_count // frame_rate

        # Divide by 60 to get total minutes
        minutes = total_seconds // 60

        # Use modulus (remainder) to get seconds
        seconds = total_seconds % 60

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

        screen.blit(text, [30, 140])

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        frame_count += 1

        # Limit frames per second
        clock.tick(frame_rate)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        enable.on()
        if buttonS.is_pressed:
            start_time = 0
            done = True


# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
