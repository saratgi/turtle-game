import pygame
import random
import math

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
PICNIC_BASKET_SIZE = 128

# Constant for quest goal
STRAWBERRY_GOAL = 10

# Load and scale images before loop
white_flower_image = pygame.image.load("assets/white-flower.png").convert_alpha()
white_flower_image = pygame.transform.scale(white_flower_image, (FLOWER_SIZE, FLOWER_SIZE))

pink_flower_image = pygame.image.load("assets/pink-flower.png").convert_alpha()
pink_flower_image = pygame.transform.scale(pink_flower_image, (FLOWER_SIZE, FLOWER_SIZE))

grass_tile_image = pygame.image.load("assets/grass-tile.png").convert()
grass_tile_image = pygame.transform.scale(grass_tile_image, (GRASS_TILE_SIZE, GRASS_TILE_SIZE))

strawberry_image = pygame.image.load("assets/strawberry.png").convert_alpha()
strawberry_image = pygame.transform.scale(strawberry_image, (STRAWBERRY_SIZE, STRAWBERRY_SIZE))

picnic_basket_image = pygame.image.load("assets/picnic-basket.png").convert_alpha()
picnic_basket_image = pygame.transform.scale(picnic_basket_image, (PICNIC_BASKET_SIZE, PICNIC_BASKET_SIZE))

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

# Decorative flowers
flowers = [
    {"image": white_flower_image, "position": (80, 120), "sway_timer": 0},
    {"image": white_flower_image, "position": (720, 90), "sway_timer": 0},
    {"image": white_flower_image, "position": (300, 500), "sway_timer": 0},
    {"image": white_flower_image, "position": (590, 560), "sway_timer": 0},

    {"image": pink_flower_image, "position": (80, 410), "sway_timer": 0},
    {"image": pink_flower_image, "position": (600, 360), "sway_timer": 0},
    {"image": pink_flower_image, "position": (820, 520), "sway_timer": 0},
    {"image": pink_flower_image, "position": (350, 70), "sway_timer": 0},
]

# Picnic basket reward position
picnic_basket_rect = picnic_basket_image.get_rect(topleft=(800, 170))

# Small shadow under the picnic basket so it feels grounded
basket_shadow = pygame.Surface((110, 24), pygame.SRCALPHA)
pygame.draw.ellipse(basket_shadow, (60, 80, 45, 80), basket_shadow.get_rect())


# Create a strawberry at a valid random position
# Avoids flowers and avoids the turtle if a turtle hitbox is provided
def create_strawberry_rect(turtle_hitbox=None):
    while True:
        new_strawberry_rect = strawberry_image.get_rect(
            topleft=(
                random.randint(0, WIDTH - strawberry_image.get_width()),
                random.randint(0, HEIGHT - strawberry_image.get_height())
            )
        )
        
        new_strawberry_hitbox = new_strawberry_rect.inflate(-16, -16)

        overlaps_flower = False
        for flower in flowers:
            flower_rect = flower["image"].get_rect(topleft=flower["position"])
            flower_hitbox = flower_rect.inflate(-20, -20)

            if new_strawberry_hitbox.colliderect(flower_hitbox):
                overlaps_flower = True
                break

        basket_hitbox = picnic_basket_rect.inflate(-20, -20)
        overlaps_basket = new_strawberry_hitbox.colliderect(basket_hitbox)
        
        overlaps_turtle = (
            turtle_hitbox is not None
            and new_strawberry_hitbox.colliderect(turtle_hitbox)
        )

        if not overlaps_flower and not overlaps_turtle and not overlaps_basket:
            return new_strawberry_rect

# Create a quest message based on the current score
def get_quest_message(score):
    if score == 0:
        return f"Quest: collect {STRAWBERRY_GOAL} strawberries for the meadow picnic."
    elif score < STRAWBERRY_GOAL - 1:
        return f"Basket: {score}/{STRAWBERRY_GOAL} strawberries collected."
    elif score < STRAWBERRY_GOAL:
        return f"Basket: {score}/{STRAWBERRY_GOAL} strawberries collected. Almost ready."
    elif score == STRAWBERRY_GOAL:
        return "Picnic basket complete! Extra strawberries unlocked."
    else:
        return f"Picnic basket complete! Extra strawberries: {score - STRAWBERRY_GOAL}"


# Grass tile dimensions used for background tiling
grass_tile_width = grass_tile_image.get_width()
grass_tile_height = grass_tile_image.get_height()

# Turtle dimensions used for screen border limits
turtle_width = turtle_image.get_width()
turtle_height = turtle_image.get_height()

# Start turtle in the center of the window
turtle_x = (WIDTH - turtle_width) / 2
turtle_y = (HEIGHT - turtle_height) / 2

# Create initial turtle hitbox so the first strawberry does not spawn on the turtle
initial_turtle_rect = turtle_image.get_rect(topleft=(round(turtle_x), round(turtle_y)))
initial_turtle_hitbox = initial_turtle_rect.inflate(-50, -50)

# Strawberry position and hitbox
strawberry_rect = create_strawberry_rect(initial_turtle_hitbox)

# Game state and clock
score = 0

reward_popup_visible = False
basket_obtained = False

running = True

clock = pygame.time.Clock()

# Font for score display
score_font = pygame.font.Font(None, 36)

# Font for quest message
quest_font = pygame.font.Font(None, 24)

# Font for reward pop-up
reward_font = pygame.font.Font(None, 48)
button_font = pygame.font.Font(None, 30)

# Reward pop-up and button rectangles
reward_popup_rect = pygame.Rect(0, 0, 560, 320)
reward_popup_rect.center = (WIDTH // 2, HEIGHT // 2)

claim_button_rect = pygame.Rect(0, 0, 190, 44)
claim_button_rect.center = (WIDTH // 2, HEIGHT // 2 + 110)

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

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if reward_popup_visible and claim_button_rect.collidepoint(event.pos):
                reward_popup_visible = False
                basket_obtained = True

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

    # Trigger flower sway when turtle touches a flower
    for flower in flowers:
        flower_rect = flower["image"].get_rect(topleft=flower["position"])
        flower_hitbox = flower_rect.inflate(-20, -20)

        if turtle_hitbox.colliderect(flower_hitbox):
            flower["sway_timer"] = 0.4

        if flower["sway_timer"] > 0:
            flower["sway_timer"] -= delta_time

    # Collect strawberry
    if not reward_popup_visible and turtle_hitbox.colliderect(strawberry_hitbox):
        score += 1

        if score == STRAWBERRY_GOAL and not basket_obtained:
            reward_popup_visible = True

        strawberry_rect = create_strawberry_rect(turtle_hitbox)

    # Draw everything in layer order
    # Fill base background color
    screen.fill((142, 215, 144))

    # Draw grass tile background
    for x in range(0, WIDTH, grass_tile_width):
        for y in range(0, HEIGHT, grass_tile_height):
            screen.blit(grass_tile_image, (x, y))

    # Draw flowers
    for flower in flowers:
        x, y = flower["position"]

        sway_offset = 0
        if flower["sway_timer"] > 0:
            sway_offset = math.sin(flower["sway_timer"] * 30) * 2

        screen.blit(flower["image"], (round(x + sway_offset), y))

    # Draw picnic basket reward after claiming it
    if basket_obtained:
        screen.blit(basket_shadow, (picnic_basket_rect.x + 9, picnic_basket_rect.bottom - 18))
        screen.blit(picnic_basket_image, picnic_basket_rect)

    # Draw strawberry
    screen.blit(strawberry_image, strawberry_rect)

    # Draw turtle on top of decorations
    screen.blit(turtle_image, turtle_rect)

    # Draw score
    score_text = score_font.render(f"Strawberries: {score}", True, (98, 65, 65))
    screen.blit(score_text, (28, 15))

    # Draw cozy quest message
    quest_message = get_quest_message(score)
    quest_text = quest_font.render(quest_message, True, (98, 65, 65))
    screen.blit(quest_text, (28, 52))

    # Draw reward pop-up
    if reward_popup_visible:
        dim_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        dim_surface.fill((0, 0, 0, 90))
        screen.blit(dim_surface, (0, 0))

        pygame.draw.rect(screen, (255, 239, 191), reward_popup_rect, border_radius=18)
        pygame.draw.rect(screen, (98, 65, 65), reward_popup_rect, 4, border_radius=18)

        reward_title = reward_font.render("Quest completed!", True, (98, 65, 65))
        reward_subtitle = quest_font.render("Picnic basket unlocked.", True, (98, 65, 65))

        reward_title_rect = reward_title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 105))
        reward_subtitle_rect = reward_subtitle.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

        basket_preview_rect = picnic_basket_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 25))

        screen.blit(reward_title, reward_title_rect)
        screen.blit(picnic_basket_image, basket_preview_rect)
        screen.blit(reward_subtitle, reward_subtitle_rect)

        pygame.draw.rect(screen, (167, 206, 167), claim_button_rect, border_radius=10)
        pygame.draw.rect(screen, (98, 65, 65), claim_button_rect, 3, border_radius=10)

        button_text = button_font.render("Claim Basket", True, (98, 65, 65))
        button_text_rect = button_text.get_rect(center=claim_button_rect.center)
        screen.blit(button_text, button_text_rect)

    # Update the visible game window
    pygame.display.update()
    
# Shut down Pygame after the game loop ends
pygame.quit()