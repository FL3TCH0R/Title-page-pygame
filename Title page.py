# import pygame
import pygame

# initializing pygame
pygame.font.init()

# check whether font is initialized
# or not
pygame.font.get_init()

# create the display surface
display_surface = pygame.display.set_mode((500, 500))

# change the window screen title
pygame.display.set_caption('Dodge')

# Create a font file by passing font file
# and size of the font
font1 = pygame.font.SysFont('freesanbold.ttf', 70)
font2 = pygame.font.SysFont('chalkduster.ttf', 40)


# Render the texts that you want to display
text1 = font1.render('Dodge', True, (0, 255, 0))
text2 = font2.render('Press ENTER to start', True, (0, 255, 0))


# create a rectangular object for the
# text surface object
textRect1 = text1.get_rect()
textRect2 = text2.get_rect()
 


# setting center for the first text
textRect1.center = (250, 50)
textRect2.center = (250, 300)

# setting center for the second text

img=pygame.image.load("C:\\Users\\Alexander\\Desktop\\School\\Coding class\\Python\\New folder\\Creating very own game basics\\image\\dodge.jpeg").convert()


while True:

	# add background color using RGB values
	display_surface.fill((0, 0, 0))

	# copying the text surface objects
	# to the display surface objects
	# at the center coordinate.
	display_surface.blit(text1, textRect1)
	display_surface.blit(text2, textRect2)
	display_surface.blit(img, (105,110))
	

	# iterate over the list of Event objects
	# that was returned by pygame.event.get()
	# method.
	for event in pygame.event.get():
            

		if event.type == pygame.QUIT:
		
			# deactivating the pygame library
			pygame.quit()

			# quitting the program.
			quit()

		# update the display
		pygame.display.update()
