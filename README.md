# word-search
This program will generate a word search, and then show any words that match
a given list of valid words.

## Usage
1. Clone this repository and then change into the root of the project.
2. Run the script with the command `python3 app.py -l LENGTH -w WIDTH`.
  - You can show the gameboard with the flag `-sb` or `--show-board`.
  Example: `python3 app.py -l 5 -w 5 --show-board`
  - You can specify your own list of words to search for with the flag `-f` or
  `--file` Example: `python3 app.py -l 5 -w 5 -f custom_file.txt`.

## Assumptions
1. The length and width of the board must be of equal.

## Testing
1. Setup a virtual environment. Steps for setting up a virtual environment
in Python can be found [here](https://docs.python.org/3/library/venv.html).
2. Once your virtual environment is setup, install `Pytest` with the command
`pip install pytest`.
3. Set your python path to the root of this directory. If you are already
in this directory, this can be done by running `export PYTHONPATH='.'`.
Otherwise, do `export PYTHONPATH=/path/to/this/directory`.
4. Run the tests from the root of the directory with the command `pytest`.
