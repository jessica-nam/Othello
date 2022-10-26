import pygame


class Othello:
    """
    Simple interactive Othello game implemented with PyGame.
    Throughout the code, col = row = 0 means the lower-left corner.
    """

    def __init__(self):
        """Initializes the game"""

        # Import and initialize the PyGame library:
        pygame.init() # constructor, necessary

        # Set up the PyGame window:
        width = 660
        height = 660

	
	# from the point of view of encapsulation it is better to avoid global variables
	# we assign the PyGame window to an attribute self.screen of the class Othello

        self.screen = pygame.display.set_mode((width, height)) # attribute

	# pygame.display.set_mode((width, height)) 
	# creates a PyGame window with given width and height in pixels.



        # Set Pygame window title:
        pygame.display.set_caption("Othello")



        # Manage how frequently the screen will update:
	# we assign it to an attribute of the class Othello rather than making it a global variable
        self.clock = pygame.time.Clock()  # attribute

	# pygame.time.Clock()
	# creates an instance of PyGame Clock

	# Clock will be used to control the refresh rate of the display.



        # Draw the board:
	# draw the initial version of the game board (an empty square)
        self.draw_board()

    def draw_board(self):  # methods
        """Displays the grid"""




        # Fill the PyGame window with white color:
        color = (255, 255, 255)  # white
        self.screen.fill(color)




        # Draw the outer square of the board:
        color = (0, 0, 0)  # black
        lw = 4  # line width


	# the point with coordinates (0, 0) is in the upper-left corner of the PyGame window

        xstart = 10
        ystart = 10
        xend = 10
        yend = 650
        pygame.draw.line(self.screen, color, (xstart, ystart), (xend, yend), lw)

        xstart = 650
        ystart = 10
        xend = 650
        yend = 650
        pygame.draw.line(self.screen, color, (xstart, ystart), (xend, yend), lw)

        xstart = 10
        ystart = 10
        xend = 650
        yend = 10
        pygame.draw.line(self.screen, color, (xstart, ystart), (xend, yend), lw)

        xstart = 10
        ystart = 650
        xend = 650
        yend = 650
        pygame.draw.line(self.screen, color, (xstart, ystart), (xend, yend), lw)

    def start(self):  # methods
        """PyGame event loop"""

	#The event loop is an essential component of event-driven programming. 
	# It is an infinite while loop which waits for various types of events (mouse movement, mouse click, key press, etc.) and reacts to them.

        # Event loop:
        finished = False
        while not finished:

            # Process any new PyGame events:
            for event in pygame.event.get():

                # Mouse moved over the PyGame window:
                if event.type == pygame.MOUSEMOTION: # types of events
                    pass

                # Mouse button was released over the PyGame window:
                if event.type == pygame.MOUSEBUTTONUP: # types of events
                    pass

                # PyGame window was resized:
                if event.type == pygame.VIDEORESIZE: # types of events
                    pass

                # User closed the window:
                if event.type == pygame.QUIT:
                    finished = True #terminated loop

                # Some key was pressed:
                if event.type == pygame.KEYDOWN:
                    # If the pressed key was ESC, exit:
                    if event.key == pygame.K_ESCAPE:
                        finished = True # terminated loop

            # Limit refresh rate to 20 frames per second:
            self.clock.tick(20)

            # Refresh the screen:
            pygame.display.update()

        # Terminate PyGame:
        pygame.quit()


# Main program:
R = Othello() # Example of how encapsulation works in practice - The class othello contains the complete functionality of the game.
R.start()
