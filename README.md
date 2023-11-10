# Basketball Team Stats Tool

## Introduction
This command-line Python application manages basketball team statistics. It allows the user to display team stats, balance teams based on player experience, and organize player rosters.

## Features
- Import player and team data from a separate Python module.
- Clean and convert player data including height (int), experience (boolean), and guardians (list).
- Balance players across teams to ensure an equal number of experienced and inexperienced players.
- Display a menu with options to view team stats or quit the program.
- Present team stats in a readable format including the team's name, player count, experience level, average height, and guardians.

## Usage
Run `app.py` to start the program. The user is prompted with a menu to display team stats or quit. Team stats are presented in a clear, readable format and can be viewed for any team.

## Requirements
Python 3.x is required to run this application. No external libraries are needed.

## Installation
Clone the repository, navigate to the project directory, and run `python app.py`.

## Project Structure
- `app.py` - The main script with dunder main protection.
- `constants.py` - Contains players and teams data used in the program.

## BONUS Features
- Balance the teams with equal numbers of experienced and inexperienced players.
- Re-prompt the main menu until the user decides to quit.
- Display players sorted by height.
- Save team analysis with player counts, experience levels, and average height.