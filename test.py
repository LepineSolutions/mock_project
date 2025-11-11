def calculate_square(number):
    """Calculate the square of a given number.

    Args:
        number (int | float): The number to square.

    Returns:
        int | float: The square of the input number.
    """
    return number * number
    """
def greet(name):
    """Generate a greeting message for the given name.

    Args:
        name (str): Name to greet.

    Returns:
        str: Greeting string in the format "Hello, {name}!".
    """
    return f"Hello, {name}!"
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