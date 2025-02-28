import pygame 
Initialize Pygame and screen dimensions 
pygame.init() 
SCREEN WIDTH, SCREEN HEIGHT = 500, 500 
Initialize display surface and set title 
display_surface pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
pygame.display.set_caption('Adding image and background image") 
Load and scale images directly 
background_image pygame.transform.scale( 
pygame.image.load('background.png").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT)) 
penguin image pygame.transform.scale( 
pygame.image.load('hello penguin.png').convert_alpha(), (200, 288)) 
penguin_rect penguin_image.get_rect(center=(SCREEN_WIDTH // 2, 
SCREEN HEIGHT //238)) 
Initialize font, render text, and set text position 
text pygame.font.Font(None, 36).render('Hello World', True, 
pygame.Color('black')) 
text_rect text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2118))