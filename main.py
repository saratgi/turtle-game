import pygame

pygame.init()

# Window settings
WIDTH = 960
HEIGHT = 640

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Turtle Meadow")

# Constant image sizes
TURTLE_SIZE = 112
FLOWER_SIZE = 64
STRAWBERRY_SIZE = 48
GRASS_TILE_SIZE = 64

# Load and scale images before loop
white_flower_image = pygame.image.load("assets/white-flower.png").convert_alpha()
white_flower_image = pygame.transform.scale(white_flower_image, (FLOWER_SIZE, FLOWER_SIZE))

pink_flower_image = pygame.image.load("assets/pink-flower.png").convert_alpha()
pink_flower_image = pygame.transform.scale(pink_flower_image, (FLOWER_SIZE, FLOWER_SIZE))

grass_tile_image = pygame.image.load("assets/grass-tile.png").convert()
grass_tile_image = pygame.transform.scale(grass_tile_image, (GRASS_TILE_SIZE, GRASS_TILE_SIZE))

strawberry_image = pygame.image.load("assets/strawberry.png").convert_alpha()
strawberry_image = pygame.transform.scale(strawberry_image, (STRAWBERRY_SIZE, STRAWBERRY_SIZE))

turtle_image = pygame.image.load("assets/turtle.png").convert_alpha()
turtle_image = pygame.transform.scale(turtle_image, (TURTLE_SIZE, TURTLE_SIZE))

# Turtle movement settings
turtle_speed = 300

# Decorative flower positions
white_flower_positions = [
    (80, 120),
    (720, 90),
    (300, 500),
    (590, 560)
]

pink_flower_positions = [
    (80, 410),
    (600, 360),
    (820, 520),
    (350, 70)
]

grass_tile_width = grass_tile_image.get_width()
grass_tile_height = grass_tile_image.get_height()

# Turtle dimensions used for screen border limits
turtle_width = turtle_image.get_width()
turtle_height = turtle_image.get_height()

# Start turtle in the center of the window
turtle_x = (WIDTH - turtle_width) / 2
turtle_y = (HEIGHT - turtle_height) / 2

# Strawberry position and collision box
strawberry_rect = strawberry_image.get_rect(topleft=(700, 400))

# Game state and clock
running = True

clock = pygame.time.Clock()

# Main game loop
while running:
    # Handle window events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Time since last frame, used for smooth movement
    delta_time = clock.tick(60) / 1000

    # Check which keys are currently being held down
    keys = pygame.key.get_pressed()

    # Move turtle with WASD or arrow keys
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        turtle_x -= turtle_speed * delta_time

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        turtle_x += turtle_speed * delta_time

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        turtle_y -= turtle_speed * delta_time
    
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        turtle_y += turtle_speed * delta_time

    # Keep turtle inside the window
    turtle_x = max(0, min(turtle_x, WIDTH - turtle_width))
    turtle_y = max(0, min(turtle_y, HEIGHT - turtle_height))

    # Draw everything in layer order
    # Fill base background color
    screen.fill((142, 215, 144))

    # Draw grass tile background
    for x in range(0, WIDTH, grass_tile_width):
        for y in range(0, HEIGHT, grass_tile_height):
            screen.blit(grass_tile_image, (x, y))

    # Draw flowers
    for position in pink_flower_positions:
        screen.blit(pink_flower_image, position)

    for position in white_flower_positions:
        screen.blit(white_flower_image, position)

    # Draw strawberry
    screen.blit(strawberry_image, strawberry_rect)

    # Draw turtle on top of decorations
    screen.blit(turtle_image, (round(turtle_x), round(turtle_y)))

    # Update the visible game window
    pygame.display.update()
    
# Shut down Pygame after the game loop ends
pygame.quit()