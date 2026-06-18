import pygame
import random

pygame.init()

# Window settings
WIDTH = 960
HEIGHT = 640

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Turtle Meadow")

# Constant image sizes
TURTLE_SIZE = 128
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

# Load right-facing turtle animation frames
turtle_frames_right = [
    pygame.transform.scale(
        pygame.image.load(path).convert_alpha(),
        (TURTLE_SIZE, TURTLE_SIZE)
    )
    for path in ["assets/turtle-idle.png", "assets/turtle-walk.png"]
]

# Create left-facing turtle animation frames
turtle_frames_left = [
    pygame.transform.flip(frame, True, False)
    for frame in turtle_frames_right
]

# Turtle starts in idle frame, facing right
turtle_image = turtle_frames_right[0]

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

# Grass tile dimensions used for background tiling
grass_tile_width = grass_tile_image.get_width()
grass_tile_height = grass_tile_image.get_height()

# Turtle dimensions used for screen border limits
turtle_width = turtle_image.get_width()
turtle_height = turtle_image.get_height()

# Start turtle in the center of the window
turtle_x = (WIDTH - turtle_width) / 2
turtle_y = (HEIGHT - turtle_height) / 2

# Strawberry position and hitbox
strawberry_rect = strawberry_image.get_rect(topleft=(700, 400))

# Game state and clock
score = 0

running = True

clock = pygame.time.Clock()

# Font for score display
score_font = pygame.font.Font(None, 36)

# Turtle animation settings
turtle_frames = turtle_frames_right
animation_index = 0
animation_timer = 0
animation_speed = 0.2

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

    # Get movement direction
    movement = pygame.Vector2(0, 0)

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        movement.x -= 1

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        movement.x += 1

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        movement.y -= 1
    
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        movement.y += 1

    # Update turtle facing direction
    if movement.x < 0:
        turtle_frames = turtle_frames_left
    elif movement.x > 0:
        turtle_frames = turtle_frames_right

    # Animate turtle while moving
    if movement.length() > 0:
        animation_timer += delta_time

        if animation_timer >= animation_speed:
            animation_timer = 0
            animation_index = (animation_index + 1) % len(turtle_frames)

        turtle_image = turtle_frames[animation_index]
    else:
        animation_index = 0
        animation_timer = 0
        turtle_image = turtle_frames[0]

    # Normalize movement so diagonal movement is not faster
    if movement.length() > 0:
        movement = movement.normalize()

        turtle_x += movement.x * turtle_speed * delta_time
        turtle_y += movement.y * turtle_speed * delta_time

    # Keep turtle inside the window
    turtle_x = max(0, min(turtle_x, WIDTH - turtle_width))
    turtle_y = max(0, min(turtle_y, HEIGHT - turtle_height))

    # Create turtle hitbox at current position
    turtle_rect = turtle_image.get_rect(topleft=(round(turtle_x), round(turtle_y)))

    # Smaller hitboxes for more accurate collision
    turtle_hitbox = turtle_rect.inflate(-50, -50)
    strawberry_hitbox = strawberry_rect.inflate(-16, -16)

    # Collect strawberry
    if turtle_hitbox.colliderect(strawberry_hitbox):
        score += 1

        strawberry_rect.topleft = (
            random.randint(0, WIDTH - strawberry_rect.width),
            random.randint(0, HEIGHT - strawberry_rect.height)
        )

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
    screen.blit(turtle_image, turtle_rect)

    # Draw score
    score_text = score_font.render(f"Score: {score}", True, (98, 65, 65))
    screen.blit(score_text, (28, 15))

    # Update the visible game window
    pygame.display.update()
    
# Shut down Pygame after the game loop ends
pygame.quit()