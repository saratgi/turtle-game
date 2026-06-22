# Turtle Meadow 🐢🍓

A cozy Python/Pygame mini-game where a small turtle explores a meadow, collects strawberries, and unlocks a picnic basket as a quest reward.

## Current Preview

![Turtle Meadow gameplay preview](media/current-preview.gif)

## Status

First playable version complete.

## Gameplay

Use **WASD** or the **arrow keys** to guide the turtle through the meadow. Collect **10 strawberries** to unlock the picnic basket reward, then click **Claim Basket** to place it in the meadow. Extra strawberries can still be collected after the quest is complete.

## Features 

- Custom pixel-art game assets
- Tiled grass background with decorative flowers
- Smooth keyboard movement with delta time
- Normalized diagonal movement for consistent speed
- Screen borders to keep the turtle inside the window
- Turtle direction changes based on movement
- Turtle walking animation while moving
- Strawberry collection with improved random respawn placement
- Strawberry counter and cozy quest progress messages
- Flowers sway when touched by the turtle
- Quest completion reward pop-up with a claim button
- Picnic basket reward after completing the strawberry goal
- Cozy background music

## What I Learned

- Structuring a simple Pygame game loop
- Loading, scaling, and drawing custom pixel-art assets
- Drawing sprites in the correct layer order
- Using delta time and Pygame Vector2 for smoother, normalized movement
- Creating simple sprite animations with frame lists and timers
- Flipping sprites to reuse animation frames for left and right movement
- Using timers and math.sin to create temporary visual effects
- Storing multiple game objects as dictionaries inside a list
- Working with Rect objects, hitboxes, collision detection, and random respawns
- Rendering strawberry counter and quest messages with Pygame fonts
- Using a helper function to generate valid strawberry spawn positions
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