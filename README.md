# Turtle Meadow 🐢🍓

A cozy Python/Pygame game in development where a small turtle explores a meadow and collects strawberries.

## Status

In development. 

## Current Features 

- Custom pixel-art game assets
- Keyboard movement with WASD and arrow keys
- Delta time movement for consistent speed
- Screen borders to keep the turtle inside the window
- Tiled grass background with decorative flowers
- Strawberry collection with random respawn
- Score tracking displayed in the game window

## Planned Features

- Turtle walking and turning animation
- Movement polish for consistent diagonal speed
- Improved strawberry respawn placement
- Interactive flower movement

## What I'm Learning

- Structuring a simple Pygame game loop
- Loading, scaling and drawing custom pixel-art assets
- Drawing sprites in the correct layer order
- Using delta time for smoother movement
- Working with Rect objects, hitboxes, and collision detection
- Using random positions for collectible respawns
- Rendering score text with Pygame fonts

## Built With

- Python
- Pygame

## How to Run

> **Note:** This project was developed with Python 3.13. Pygame may not install correctly with Python 3.14 on Windows, so Python 3.13 is recommended.

Install the required package:

```bash
py -3.13 -m pip install -r requirements.txt
```

Run the game:

```bash
py -3.13 main.py
```