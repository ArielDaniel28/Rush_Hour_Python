
Rush Hour Game
This Python program implements the Rush Hour game, where the player needs to maneuver vehicles to clear a path for a specific car to exit the game board.

Introduction
Rush Hour is a sliding block puzzle game that challenges players to navigate a congested traffic jam by moving vehicles out of the way. The game consists of a 6x6 grid (although this implementation uses a 7x7 grid) with vehicles of varying lengths placed horizontally or vertically. The objective is to clear a path for the red car (marked as 'X') to exit the grid.

Usage
To play the Rush Hour game, follow these steps:

Run the Python script rush_hour.py.
Provide the path to a JSON file containing the initial configuration of vehicles on the game board as a command-line argument.
Follow the prompts to input your moves. Enter the name of the car you want to move and the direction (e.g., "A,2" to move car A two spaces to the right).
Continue making moves until you clear a path for the red car to exit or until no valid moves are possible.
Implementation Details
The program consists of several modules:

helper.py: Provides utility functions for loading JSON data.
board.py: Defines the game board and operations related to it.
car.py: Defines the properties and behavior of individual cars on the board.
rush_hour.py: The main program that orchestrates the Rush Hour game.
The Game class in rush_hour.py manages the game by handling user inputs, validating moves, and driving the game until completion.

The game board is represented as a 7x7 grid, and cars are represented as objects with properties such as name, length, location, and orientation.


## License

This program was written by a student of the Introduction to Computer Science course at the Hebrew University in Jerusalem as part of the course requirements.
