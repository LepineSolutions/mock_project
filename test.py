def calculate_square(number):
    """
    Calculate the square of a given number
    """
    return number ** 2

def greet(name):
    """
    Return a greeting message
    """
    return f"Hello, {name}!"

# Example usage
if __name__ == "__main__":
    # Test the square function
    result = calculate_square(5)
    print(f"Square of 5 is: {result}")
    
    # Test the greeting function
    message = greet("World")
    print(message)
    
    # Additional simple tests
    assert calculate_square(0) == 0
    assert calculate_square(-3) == 9
    assert abs(calculate_square(2.5) - 6.25) < 1e-9
    assert greet("Alice") == "Hello, Alice!"
    print("All additional tests passed.")
    
    # Additional functions
    def add(a, b):
        """Add two numbers"""
        return a + b
    
    def multiply(a, b):
        """Multiply two numbers"""
        return a * b
    
    # Test new functions
    print(f"\n5 + 3 = {add(5, 3)}")
    print(f"5 * 3 = {multiply(5, 3)}")
    
    assert add(10, 20) == 30
    assert multiply(4, 7) == 28
    print("All tests passed successfully!")
