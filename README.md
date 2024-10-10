# Physics Motion Simulation Tool
## Overview
This Python project provides an interactive command-line tool that simulates basic physics motion models, including projectile motion and two-dimensional motion. Users can input initial conditions such as position, velocity, acceleration, and time to generate real-time graphs of motion trajectories.
The project also includes unit tests to ensure the accuracy of the physics models.
## Features
Projectile Motion Simulation: Simulates the motion of a projectile, accounting for initial height, launch angle, and initial velocity.

Two-Dimensional Motion Simulation: Models motion in both the x and y directions with user-defined initial velocities, position and accelerations. It calculates and plots the path of the object over time.

Graphical Representation: Uses matplotlib to display motion trajectories
## Usage
1. When prompted, select one of the following options:
_1 for projectile motion simulation
2 for two-dimensional motion simulation
3 to exit the program_
2. Input the requested parameters (height, velocity, acceleration, etc.) and view the motion graph.
## Unit Tests
Unit tests for key functions are included in test_main.py and can be run using pytest:
```
pytest test_main.py
```
The tests check for a correct breakdown of velocity components, accurate displacement calculations and proper custom float range function functionality.
## Dependencies
- matplotlib
- pytest
Install them with:
```
pip install matplotlib pytest
```
