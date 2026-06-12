import pygame

pygame.init()

WIDTH = 960
HEIGHT = 640

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Turtle Meadow")

turtle_image = pygame.image.load("assets/turtle.png").convert_alpha()
turtle_image = pygame.transform.scale(turtle_image, (112, 112))

turtle_speed = 300

turtle_x = 400
turtle_y = 260

turtle_width = turtle_image.get_width()
turtle_height = turtle_image.get_height()

running = True

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    delta_time = clock.tick(60) / 1000

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        turtle_x -= turtle_speed * delta_time

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        turtle_x += turtle_speed * delta_time

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        turtle_y -= turtle_speed * delta_time
    
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        turtle_y += turtle_speed * delta_time

    turtle_x = max(0, min(turtle_x, WIDTH - turtle_width))
    turtle_y = max(0, min(turtle_y, HEIGHT - turtle_height))

    
    screen.fill((142, 215, 144))

    screen.blit(turtle_image, (round(turtle_x), round(turtle_y)))

    pygame.display.update()

    

pygame.quit()