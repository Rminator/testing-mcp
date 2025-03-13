# testing-mcp
# Even Number Handler

A simple Python utility class for handling operations related to even numbers. This class provides functionality to find even numbers within a range and check if individual numbers are even.

## Features

- Find all even numbers within a specified range
- Check if a single number is even
- Store and retrieve previously calculated even numbers

## Installation

Clone this repository:
bash
git clone https://github.com/Rminator/testing-mcp.git
cd testing-mcp
python
from nlpractice import EvenNumberHandler


usage:

python
from nlpractice import EvenNumberHandler
Create an instance of EvenNumberHandler
handler = EvenNumberHandler()
Find even numbers in a range
even_numbers = handler.find_even_numbers(1, 20)
print("Even numbers between 1 and 20:", even_numbers)
Check if a specific number is even
number = 16
is_even = handler.is_even(number)
print(f"Is {number} even? {is_even}")
Get previously stored even numbers
stored_numbers = handler.get_stored_numbers()
print("Stored even numbers:", stored_numbers)



## Class Methods

### `find_even_numbers(start, end)`
Finds all even numbers in the range from `start` to `end` (inclusive).

### `is_even(number)`
Checks if a given number is even.

### `get_stored_numbers()`
Returns the list of previously calculated even numbers.

## Contributing

Feel free to open issues or submit pull requests with improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.


