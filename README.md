# Turtle Meadow 🐢🍓

A cozy Python/Pygame game in development where a small turtle explores a meadow and collects strawberries.

## Current Preview

![Turtle Meadow gameplay preview](media/current-preview.gif)

## Status

First playable version complete.

## Current Features 

- Custom pixel-art game assets
- Keyboard movement with WASD and arrow keys
- Delta time movement for consistent speed
- Screen borders to keep the turtle inside the window
- Tiled grass background with decorative flowers
- Strawberry collection with improved random respawn placement
- Strawberry counter displayed in the game window
- Consistent movement speed in all directions
- Turtle turns left and right based on movement direction
- Turtle walking animation while moving
- Flowers gently sway when touched by the turtle
- Cozy quest progress messages
- Quest completion reward pop-up with a claim button
- Picnic basket reward after completing the strawberry goal

## What I'm Learning

- Structuring a simple Pygame game loop
- Loading, scaling, and drawing custom pixel-art assets
- Drawing sprites in the correct layer order
- Using delta time and Pygame Vector2 for smoother, normalized movement
- Creating simple sprite animations with frame lists and timers
- Flipping sprites to reuse animation frames for left and right movement
- Using timers and math.sin to create temporary visual effects
- Storing multiple game objects as dictionaries inside a list
- Working with Rect objects, hitboxes, collision detection, and random respawns
- Rendering strawberry counter and quest text with Pygame fonts
- Using a helper function to generate valid strawberry spawn positions
- Using a while loop to retry random positions until they are valid
- Handling mouse clicks with Rect.collidepoint
- Using game state variables for reward pop-ups and unlockable items 
- Drawing a simple in-game reward pop-up with rectangles and transparency

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