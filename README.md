# Sudoku Solver with Python and OpenCV
![Sudoku Solver](https://img.shields.io/badge/Sudoku%20Solver-Python%20%7C%20OpenCV-blue)

This Python project is designed to solve unsolved Sudoku puzzles that you upload in PNG format using a Telegram bot. It utilizes the power of computer vision and the OpenCV library to recognize and solve Sudoku puzzles from images. The solved puzzle is then sent back to you in PNG format.

## How to Use

1. **Start the Bot**: To begin using the Sudoku solver bot, start a chat with it on Telegram. Search for the bot by its username or use this link: [Sudoku Solver Bot](https://t.me/sudoku_master_bot).

2. **Send Your Sudoku Puzzle**: You can upload an unsolved Sudoku puzzle in PNG format to the bot. Make sure the image is clear and well-lit for better recognition.

3. **Receive the Solved Puzzle**: The bot will process the image and attempt to solve the Sudoku puzzle. Once it successfully solves the puzzle, it will send you back the solved puzzle in PNG format.

4. **Enjoy**: You now have a solved Sudoku puzzle! Feel free to share it with friends or use it for your own enjoyment.

## Installation

To run this project locally, you can follow these steps:

1. Clone the repository to your local machine: `git clone https://github.com/ozermehmett/sudoku-solver-with-python-opencv.git`
2. Install the required Python libraries using pip: `pip install -r requirements.txt` 
3. Create a Telegram bot and get the API token. You can do this by talking to the [BotFather](https://core.telegram.org/bots#botfather) on Telegram.
4. Replace the `TOKEN` variable in the `telegram_bot.py` file with your bot's API token.
5. Install Tesseract-OCR on your computer and add the file path to System Environment Variables as `PATH`
6. Run the `main.py` script to start the bot: `python main.py`


## Example

Here's an example of how you can use this bot:

1. Start a chat with the bot on Telegram.

2. Upload a Sudoku puzzle in PNG format.

3. Wait for the bot to process the image and send back the solved Sudoku puzzle in PNG format.

4. Enjoy your solved puzzle!


https://github.com/ozermehmett/sudoku-solver-with-python-opencv/assets/115498182/043459d0-105a-4c6c-9917-9251f4816622


## Credits

- This project uses the OpenCV library for image processing and recognition.
- The Sudoku solving logic is implemented using Python.


## Did you find this repository helpful?
Do not forget to give a start

## Didn't you?
Then fork this repo, make it BETTER and do not forget to give a STAR
