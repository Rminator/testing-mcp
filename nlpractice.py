class EvenNumberHandler:
    """A class to handle operations related to even numbers"""
    
    def __init__(self):
        self.even_numbers = []
    
    def find_even_numbers(self, start, end):
        """Find all even numbers in a given range"""
        self.even_numbers = []
        for num in range(start, end + 1):
            if num % 2 == 0:
                self.even_numbers.append(num)
        return self.even_numbers
    
    def is_even(self, number):
        """Check if a single number is even"""
        return number % 2 == 0
    
    def get_stored_numbers(self):
        """Return the last calculated even numbers"""
        return self.even_numbers

# Example usage
if __name__ == '__main__':
    handler = EvenNumberHandler()
    result = handler.find_even_numbers(1, 20)
    print("Even numbers between 1 and 20:", result)

    # Check if a number is even
    number_to_check = 16
    print(f"Is {number_to_check} even?", handler.is_even(number_to_check)) 