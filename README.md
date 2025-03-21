Snake Game in Python using Turtle Graphics and OOP
Overview
This project is a classic Snake Game implemented in Python using the Turtle graphics library. The game is designed with Object-Oriented Programming (OOP) principles, making it modular, maintainable, and easy to extend. Players control a snake that grows in length as it consumes food, while avoiding collisions with the walls and itself.

Features
Simple and Intuitive Gameplay: Control the snake using keyboard arrows to navigate and eat food.
Dynamic Growth: The snake grows longer with each piece of food consumed.
Collision Detection: The game ends if the snake collides with the wall or itself.
Score Tracking: The current score is displayed on the screen, updating in real-time as the player eats food.
Restart Functionality: Players can restart the game after a collision.
Technologies Used
Python: The programming language used for the game logic.
Turtle Graphics: A built-in Python library for creating simple graphics and animations.
Object-Oriented Programming (OOP): The game is structured using classes and objects to encapsulate functionality and improve code organization.
Game Structure
The game is organized into several classes:

Game: The main class that initializes the game, manages the game loop, and handles user input.
Snake: A class representing the snake, responsible for its movement, growth, and collision detection.
Food: A class representing the food items that the snake can consume.
Scoreboard: A class that manages the display of the current score and game over messages.
Installation
