# IS450-Assignment8: Git Development with AI

## Project Description
The F1 Lap Time Tracker is a console application that allows users to input multiple race lap times in seconds. The program stores the data in a list and calculates the session's fastest lap and average lap pace.

## Initial Version
The initial push included the core functionality:
* A `while` loop to continuously accept user input.
* A Python list to store all submitted lap times.
* A `calculate_average()` function to process the list data.
* Console output displaying total laps, fastest lap, and average lap.

## AI Tool Used
* Google Gemini

## AI Assistance
I asked the AI: "How do I prevent my Python program from crashing if a user types a word instead of a number for the lap time?"

## New or Modified Features
I added input validation using a `try-except` block (`ValueError`). If the user types invalid text, the program catches the error, prints a friendly warning, and allows them to try again instead of crashing. I also added a check to ensure lap times cannot be negative numbers.

## Evaluation of AI Output
I accepted the AI's recommendation to use a `try-except` block because it is the most Pythonic way to handle `float()` conversion errors. The AI provided a clean example, which I modified slightly to also block negative numbers (`if lap_time <= 0`), ensuring the data remains logically sound for racing.

## How to Run the Program
1. Open a terminal in the project directory.
2. Run the script using Python:
   ```bash
   python main.py

## Feature Development Comparison
For this dual-approach assignment, I created two distinct features for the F1 Lap Tracker. On the `manual-feature` branch, I added a "Total Session Time" calculation that sums all recorded laps and displays the total duration in seconds. I wrote this using Python's built-in `sum()` function. On the `ai-feature` branch, I used Google Gemini to implement a "Slowest Lap" tracker. I asked the AI to write a function that finds the highest value in the lap list.

The AI-produced feature worked correctly on the first attempt, utilizing the `max()` function. I did not have to modify or reject any of the AI's logic, though I did manually format the f-string to ensure it matched the visual style of the existing console output.

Ultimately, the manual approach gave me greater confidence. While the AI was instantly accurate for this simple list operation, writing the manual feature forced me to actively think about the data structure and how the new print statement integrated into the existing control flow. The AI approach felt like pasting a black box, whereas the manual approach reinforced my understanding of the program's architecture.