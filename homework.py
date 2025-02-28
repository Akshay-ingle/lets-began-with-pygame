import pygame

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My first game screen")

# Load and scale image
image = pygame.image.load("your_image.png")  # Replace with your image file
image = pygame.transform.scale(image, (300, 300))

# Get image position (centered)
image_rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Set background color
BG_COLOR = (58, 58, 58)

# Main loop
running = True
while running:
    screen.fill(BG_COLOR)  # Fill the screen with the background color
    screen.blit(image, image_rect)  # Draw the image at the center
    pygame.display.flip()  # Update the display
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()