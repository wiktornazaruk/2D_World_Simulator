# 2D World Simulator

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Game Details](#game-details)
  - [Organisms](#organisms)
    - [Animals](#animals)
    - [Plants](#plants)
  - [More Information](#more-information)
- [Gameplay](#gameplay)
  - [Adding Organisms](#adding-organisms)
  - [Controls](#controls)
- [Installation and Execution](#installation-and-execution)
- [Preview](#preview)
- [Acknowledgments](#acknowledgments)

## Overview

The 2D World Simulator is a desktop application developed in Python that simulates a virtual world composed of various organisms, including animals and plants. Each organism exhibits distinct behaviors and interactions within a two-dimensional grid environment.

## Features

- **Dynamic World Structure**: The simulation operates on an NxN grid where each cell can be occupied by a single organism.
- **Diverse Organisms**: Includes a variety of animals and plants, each with unique behaviors and characteristics.
- **Turn-Based Mechanics**: The simulation progresses in turns, with each organism performing actions based on its species-specific behavior.
- **Collision Handling**: Manages interactions between organisms, such as movement, reproduction, and combat scenarios.

## Game details

### Organisms

#### Animals

- **Wolf**
  - *Behavior*: Moves to a randomly selected neighboring cell. In case of a collision with another organism, the one with higher strength prevails.

- **Sheep**
  - *Behavior*: Similar to the wolf but with different strength and initiative values.

- **Fox**
  - *Behavior*: Moves to a neighboring cell only if it's not occupied by a stronger organism.

- **Turtle**
  - *Behavior*: Has a 75% chance to stay in the same place. Reflects attacks from animals with strength less than 5; the attacker returns to its previous cell.

- **Antelope**
  - *Behavior*: Moves two cells instead of one. Has a 50% chance to escape from a fight by moving to a free neighboring cell.

- **Human**
  - *Behavior*: Movement is controlled by the player using arrow keys. Possesses a special ability called "Immortality" which can be activated with the 'End' key.

#### Plants

- **Grass**
  - *Behavior*: Attempts to spread to a random neighboring free cell.

- **Sow Thistle**
  - *Behavior*: Performs three attempts to spread in each turn.

- **Guarana**
  - *Behavior*: When consumed by an animal, it permanently increases the animal's strength by 3.

- **Belladonna**
  - *Behavior*: Kills any animal that eats it.

- **Sosnowsky's Hogweed**
  - *Behavior*: Kills every animal in its immediate neighborhood except the cyber-sheep. Also kills any animal that eats it, apart from the cyber-sheep.
 
### More information

For more detailed information about the game, refer to the `Instruction.pdf` file included in the repository.

## Gameplay

### Adding Organisms

To add organisms to the grid:

1. Select the desired organism by clicking on one of the pink tiles.
2. Click on the grid tiles where you want to place the selected organism.

### Controls

- **Arrow Keys**: Move the human character in the desired direction and proceed to the next turn.
- **End Key**: Activate the human's special ability, "Immortality," and proceed to the next turn.
- **Home Key**: Save the current game state.
- **Insert Key**: Load a previously saved game state.
- **Escape Key**: Exit the game.
- **M Key**: Play background music.

## Installation and Execution

To run the program:

1. **Download the Repository**:
   - Click on the green "Code" button and select "Download ZIP."
   - Extract the contents of the ZIP file.

2. **Install Required Libraries**:
   - Ensure you have Python installed on your system.
   - Install the necessary libraries using pip:
     ```bash
     pip install pygame tkinter pillow
     ```

3. **Run the Program**:
   - Navigate to the extracted folder and run `main.py`:
     ```bash
     python main.py
     ```

## Preview

![alt text](https://github.com/wiktornazaruk/2D_World_Simulator_Python/blob/main/preview.png?raw=true)

## Acknowledgments

Music from Minecraft.
Icons inspired by Minecraft.
